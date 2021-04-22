### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 5 - Augmentacja danych i transfer learning

### 1. Augmentacja danych

Generative Adversarial Network (GAN) składa się z dwóch sieci neuronowych, jednej zwanej generatorem i drugiej zwanej dyskryminatorem.

Zadaniem generatora jest estymacja rozkładu prawdopodobieństwa rzeczywistych próbek w celu dostarczenia wygenerowanych próbek przypominających rzeczywiste dane. 

Dyskryminator z kolei jest trenowany do szacowania prawdopodobieństwa, że dana próbka pochodzi z prawdziwych danych, a nie została dostarczona przez generator.

Struktury te nazywane są generatywnymi sieciami przeciwstawnymi (Generative Adversarial Network), ponieważ generator i dyskryminator są trenowane tak, aby konkurować ze sobą: generator stara się coraz lepiej oszukiwać dyskryminator, podczas gdy dyskryminator stara się coraz lepiej identyfikować wygenerowane próbki.

W naszym przypadku planujemy zaimplementować generator i dyskryminator w kerasie oraz trenować go na naszym zbiorze danych. Uzyskany w ten sposób model będzie w stanie wygenerować dużą liczbę zdjęć płuc gotowych do dalszego wstępnego trenowania nienadzorowanego (Transfer Learning). Chcemy, żeby generator po dostaniu losowego szumu na wejściu tworzył wiarygodne zdjęcia płuc o rozmiarze 224x224.

<p align="center">
<img src="https://i2.wp.com/www.kdnuggets.com/wp-content/uploads/generative-adversarial-network.png?zoom=2" height="400">
</p>

### 2. Transfer learning (auxiliary task)

Metoda Transfer Learningu polega na wykorzystywaniu wiedzy z już wyszkolonym modelu uczenia maszynowego do innego, ale pokrewnego problemu. Dzięki temu próbujemy wykorzystać to, czego nauczyliśmy się w jednym zadaniu, aby poprawić generalizację w innym..
 
Głównymi  zaletami są:
- oszczędzanie  czasu treningu,
- sieć neuronowa działa lepiej w większości przypadków i nie potrzebuje dużej ilości danych.

Zazwyczaj się go stosuje gdy jest zbyt mało oznakowanych danych treningowych, aby szkolić swoją sieć od początku i / lub istnieje już sieć, która jest wcześniej przeszkolona w podobnym zadaniu, na ogromnej ilości danych. Innym przypadkiem, w którym jego zastosowanie byłoby odpowiednie, jest sytuacja, w której zadania A i zadanie B mają takie same dane wejściowe.

Jedną z form Tranfer Learningu jest auxiliary task, polegający na tym, że zadajemy modelowi dodatkowe zadanie, którego najważniejszym celem jest poprawienie rezultatu modelu na pierwotnym zadaniu. Wyszkolony w ten sposób model może posłużyć jako “zaczyn” do szkolenia modelu przede wszystkim starającego się rozwiązać zadanie pierwotne.
<p align="center">
<img src="https://i.imgur.com/SxPgqNg.png " height="300">
</p>

W naszym przypadku zamierzamy wykorzystać dodatkowe informacje pojawiające się w części naszego zbioru zdjęć pochodzącego od RSNA - zbiór ten pozwala podzielić zdjęcia płuc na te z pneumonia i normalne. Oprócz tego celem jest również określenie miejsca w płucach, w którym znajduje się pneumonia - i to tę informację wykorzystamy do auxiliary task. Znaczny rozmiar zbioru RSNA powinien zapobiec przeuczeniu się modelu na tych zdjęciach.
 
Pomysł polega zatem na wytrenowaniu modelu z klasyfikacją jak z RSNA i dodanie dodatkowego zadania w postaci znajdywania położenia wspomnianej wyżej pneumonii. Wytworzone w ten sposób wagi modelu będą następnie przełożone do modelu, który ma rozwiązywać zadanie pierwotne - i to one posłużą jako pierwotne wagi do uczenia.  

### 3. Transfer learning (unsupervised pretraining)

Nienadzorowane uczenie wstępne modelu zwykle wykorzystuje się jeśli nie mamy dużej ilości danych treningowych z etykietami i nie możemy znaleźć modelu wytrenowanego dla podobnego zadania. Jeśli mamy dostęp do dużej ilości danych bez etykiet możemy spróbować wytrenować warstwy po kolei, zaczynając od najniższej i idąc w górę, używając nienadzorowanego algorytmu wykrywania cech (np. autoenkoder). Wszystkie warstwy oprócz trenowanej są zamrożone. Po wytrenowaniu wszystkich warstw w ten sposób można dodać warstwę wyjściową i dostroić sieć używając uczenia nadzorowanego (można odmrozić wszystkie wstępnie wytrenowane warstwy albo tylko niektóre z górnych).

<p align="center">
<img src="https://i.imgur.com/zHg4GzI.png " height="350">
</p>

Zamierzamy zaimplementować nienadzoworane uczenie wstępne modelu zgodnie z procesem opisanym wyżej i przy użyciu autoenkoderów (enkoder-dekoder). Ich działanie polega na uczeniu się odtwarzania danego wejścia przy odpowiednich ograniczeniach (np. zmniejszanie rozmiaru, dodanie szumu). Dzięki nałożonych ograniczeniach uczymy odpowiednie warstwy efektywnych sposobów reprezentacji danych wejściowych z wykluczeniem prostego kopiowania inputu. 

W naszym przypadku pracujemy na wykorzystywanym przez autorów modelu VGG19. Uczenie wstępne zostanie wykonane na blokach konwolucyjnych sieci. Odpowiednie bloki konwolucyjne będą pełniły funkcję enkodera, do których trzeba będzie dołożyć odpowiednie dekodery, żeby można było określić skuteczność odwzorowania danych. 

Do trenowania użyte przez nas zostaną oryginalne dane COVIDx (z wyodrębnieniem małego zbioru do uczenia nadzorowanego), które w zależności od tego czy uda nam się zaimplementować GAN z pomyślnymi wynikami czy nie, mogą zostać uzupełnione wygenerowanymi danymi.
<p align="center">
<img src="https://i.imgur.com/L06GVDv.png " height="380">
</p>
