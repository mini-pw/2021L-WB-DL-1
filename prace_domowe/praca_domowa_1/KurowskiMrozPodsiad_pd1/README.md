### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 1 - Zbiory danych

### 1. Format Datasetu

Zdjęcia CXR, format png (większość i te są w grayscale w 1024 x 1024) i jpg,  kolory 8-bitowe, format RGB: większość to grayscale ale jest w datasecie kilka fioletowych (i czarno-białych) w sRGB i autorzy konwertują na RGB, różne liczby pikseli (finalnie przekonwertowane na 50176), rozdzielczość: różne, są zdjęcia w 1024 x 1024 (większość), są w 500x500, itd.  - wszystkie finalnie przekonwertowane na 224x224.

Autorzy w fazie preprocessingu danych starali się usunąć artefakty obrazów CXR (np. Oznaczenia R, L na kolejno, prawe i lewe strony klatki piersiowej) poprzez ustawienie górnej granicy jasności pikseli w celu usunięcia tych najjaśniejszych. Usunięte miejsca zostały potem uzupełnione.

Zdjęcia zostały następnie wystandaryzowane - każdy piksel został pomniejszony o wartość średnią pikseli, a następnie podzielony przez odchylenie standardowe. Średnia i odchylenie standardowe jest obliczane na całym zbiorze danych. Dla normalizacji zdjecia, wartości pikseli są podzielone przez 255 tak, by wartość każdego z nich zawierała się w przedziale [0,1].
	
Na sam koniec (przed trenowaniem) dokonano wspomnianego wcześniej przekonwertowania zdjęć na rozdzielczość 224 x 224 x 3 (3, bo do RGB)

### 2. Zbalansowanie Datasetu

Autorzy w artykule umieścili opisy wykorzystywanych datasetów, jednak wydaje nam się że nie są one w 100% poprawne. Zgodnie z artykułem w datasecie ‘COVIDx v1.0’ jest “13,975 zdjęć CXR”, w czym podział na klasy wygląda następująco: “358 COVID19; 8,066 normal; 5,538 non-COVID19 pneumonia”. Niestety gdzieś autorzy musieli się pomylić bo te liczby dodają się do 13,962 przypadków w sumie, a nie 13,975. Poza tym ‘COVIDx v1.0’ to dataset który jest cały czas niezależnie aktualizowany, a ich wersja (v1.0 czy modyfikowana przez nich v2.0) nie została umieszczona na repozytorium więc nie będziemy w stanie raczej zreprodukować dokładnie ich wyników.

Modyfikowana przez nich wersja datasetu COVIDx v2.0 zawiera “15,959 zdjęć CXR”, gdzie podział na klasy wygląda następująco: przynajmniej 553 COVID19; przynajmniej 8,636 normal; przynajmniej 6,038 non-COVID19 pneumonia. Do tego zostało dodane 660 zdjęć CXR (frontal view) ale autorzy nie napisali jakich klas były te obrazy. Nie mniej jednak te liczby nadal dodają się do 15,887 a nie 15,959 więc ewidentnie coś gdzieś nie zostało zanotowane poprawnie. Widać jednak wyraźnie że oba używane przez autorów datasety są mocno niezbalansowane.

Wygenerowany przez nas dataset COVIDx ma następujący skład, który sumarycznie zbalansowaniem jest podobny do zbioru autorów:

	Final stats
	Train count:  {'normal': 7966, 'pneumonia': 5475, 'COVID-19': 1670}
	Test count:  {'normal': 885, 'pneumonia': 594, 'COVID-19': 100}
	Total length of train:  15111
	Total length of test:  1579

> “We consider 2 different versions of the datasets: first, we used the ‘COVIDx v1.0’ dataset by Wang et al. used to train and evaluate the COVID-Net, comprised of a total of 13,975 CXR images across 13,870 patient cases. COVIDx is mainly based on RSNA Pneumonia Detection Challenge, ActualMed COVID-19 Chest X-ray Dataset Initiative, COVID-19 radiography database, giving 219 COVID-19 positive images, 1,341 normal images, and 1,345 viral pneumonia images. This gives 358 CXR images from 266 COVID-19 patient cases and total of 8,066 patient cases who have no pneumonia (i.e.,normal) and 5,538 patient cases who have non-COVID19 pneumonia. The updated dataset, which we refer to ‘COVIDx v2.0’ is categorized as normal (i.e., no-findings), pneumonia, and COVID-19 viral are enriched with CXR images of adult subjects of COVID-19, pneumonia, and normal examples, leaving 15,959 CXR images across 15,854 patients:
> - COVID chest X-ray-dataset: Joseph P.C. et al.: 660 PA (i.e., frontal view) CXR images.
> - COVID-19 patients lungs X-ray images: 70 COVID-19 and 70 normal CXR images.
> - Chest X-ray images by Ozturk et al.: 125 COVID-19, 500 normal, and 500 pneumonia CXR images.”


### 3. Metody do poradzenia sobie z niezblansowaniem danych

Autorzy użyli “wag klasowych” (class weighting), które pozwala na ocenę modelu, gdy błędnie zaklasyfikuje on próbkę pozytywną. Użyli też miar Precision, Recall, F1 i Positive Predictive Value (PPV) do dobrego przedstawienia wyników przy niezrównoważonych klasach uzyskanych przez random search i 5-krotną crossvalidację.

“Class weighting” polega na tym, że modyfikujemy obecny algorytm treningowy tak, aby uwzględniał niezbalansowanie klas. Osiągamy to poprzez nadanie różnych wag klasom większościowym i mniejszościowym. Różnica w wagach będzie miała wpływ na klasyfikację klas podczas fazy szkolenia. Celem jest ukaranie błędnej klasyfikacji dokonanej przez klasę mniejszościową poprzez ustawienie wyższej wagi dla klasy i jednoczesne zmniejszenie wagi dla klasy większościowej.

Można to zaimplenetować na przykład przypisując wagi klasom odwrotnie proporcjonalnie do ich częstości, czyli wg wzoru:

w<sub>j</sub> = n<sub>sample</sub> / (n<sub>klas</sub>\*n<sub>sample<sub>j</sub></sub>)

w<sub>j</sub> - waga dla każdej klasy (j oznacza klasę)  
n<sub>sample</sub> - całkowita liczba próbek (wierszy) w zbiorze danych  
n<sub>klas</sub> - całkowita liczba unikalnych klas w zbiorze danych  
n<sub>sample<sub>j</sub></sub> - całkowita liczba próbek (wierszy) danej klasy

<!---
<img src="https://render.githubusercontent.com/render/math?math=w_j = \frac{n_{sample}}{n_{klas} * n_{sample_j}}">
<img src="https://render.githubusercontent.com/render/math?math=w_j"> - waga dla każdej klasy (j oznacza klasę)
<img src="https://render.githubusercontent.com/render/math?math=n_{sample}"> - całkowita liczba próbek (wierszy) w zbiorze danych
<img src="https://render.githubusercontent.com/render/math?math=n_{klas}"> - całkowita liczba unikalnych klas w zbiorze danych
<img src="https://render.githubusercontent.com/render/math?math=n_{sample_j}"> - całkowita liczba próbek (wierszy) danej klasy --->

> “To tackle the class imbalance issue, we apply class weighting to penalize a model when it missclassifies a positive sample. Although accuracy is an intuitive evaluation criterion for many bio-imaging problems, e.g., osteoarthritis severity prediction, those evaluation criteria are most suitable for balanced class scenarios. Keeping in mind the imbalanced scenario with widely different class distributions between classes, we report precision, recall, F1, and positive predictive value (PPV) produced through random search and 5-fold cross-validation tests, i.e., for each hyperparameter group of the specific network structure, 5 repeated experiments are conducted.”

### 4. Over-sampling i Under-sampling

W używanym przez nas datasecie COVIDx występuje dosyć spore niezbalansowanie klas, bo około 8800:6000:1700. Do poradzenia sobie z tym może zostać wykorzystany over-sampling (powielenie naszej najmniejszej klasy aż jest równa z pozostałymi) albo under-sampling (wybranie losowo mniejszej ilości próbek z większych klas żeby były porównywalne wielkością z tą mniejszą).

W notebooku *preprocess_data_COVIDx.ipynb* został umieszczony skrypt który generuje pliki .npy z datasetu COVIDx gotowe do załadowania do sieci neuronowych autorów.

Over-sampling został zrobiony w oparciu o kod autorów artykułu. Zaszła jednak potrzeba zmiany części kodu, więc piszemy nowe funkcje. Wykorzystujemy: *imblearn.over_sampling.RandomOverSampler*. Kod generujący datasety umieszczony został w notebooku: *random_over_sampling.ipynb*.

Under-sampling został zrobiony przy użyciu *imblearn.under_sampling.RandomUnderSampler* przy zadaniu *sampling strategy* tak, by wartości wszystkich klas były równe najmniejszej. Ustawienie *random_state* czyni proces powtarzalnym. Kod generujący podzielone pliki .npyowe umieszczony jest w notebooku *random_under_sampler.ipynb*. (Należy znaznaczyć, że ścieżki w tym pliku są lokalne - wymagają zatem manualnej zmiany).   

Niestety mieliśmy duże trudności z poprawnym wygenerowaniem datasetu COVIDx. W dokumentacji wspomniane jest że próbek z COVID19 powinno być w okolicach 1700 jednak skrypt generujący ten dataset w naszym przypadku mówił o około 4100 próbkach z COVID19 i nadal nie jesteśmy pewni z czego to wynika. Na szczęście udało nam się w końcu pozyskać poprawną wersję i zrobić na niej over-sampling i under-sampling ale nie zdążyliśmy już przepuścić wszystkich zbiorów przez sieci neuronowe. 
