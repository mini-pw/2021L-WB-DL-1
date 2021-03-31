### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 3 - Preprocessing

### 1. Preprocessing w artykule 

Autorzy artykułu wykorzystują dwie metody preprocessingu:

* Wyrównanie histogramu
* Usunięcie adnotacji 

Pierwsza z metod polega na rozciągnięciu wartości pikseli będących reprezentacją zdjęcia w taki sposób, że zostaje zwiększony jego kontrast. Po przedstawieniu ich w formie histogramu proces rozszerza go w ten sposób, że wartości są bardziej równomiernie rozłożone na całej dostępnej skali jasności pikseli.

Natomiast usunięcie adnotacji to wykorzystanie biblioteki OpenCV do usunięcia najbardziej odstających od reszty obrazu artefaktów (takich jak litery L, R oznaczające strony klatki piersiowej widoczne na zdjęciu). Jest to wykonywane dla każdego obrazu dwa razy (sprawdzanie prawej i lewej strony), po uprzednim usunięciu szumu z wykorzystaniem funkcji anisotropic_diffusion z biblioteki medpy.

Przykładowy preprocessing obrazu zamieszczamy w notebooku *image_preprocessing.ipynb*.


### 2. Nasze 3 ulepszenia

TODO

### 3. Preprocessing w OCR

Preprocessing w OCR (optycznym rozpoznywaniu znaków) jest często stosowany żeby poprawić precyzję. Chcemy żeby obrazy, na których wykonywany jest OCR miały jak najbardziej czytelne znaki (wysoką ostrość, duży kontrast, dobre wypoziomowanie, małe szumy). Poniżej techniki które wykorzystywane są do polepszenia tak zdefiniowanej jakości zdjęć:

* **Binaryzacja**, czyli konwersja kolorowego zdjęcia na takie, które zawiera tylko białe i czarne piksele. Określony musi być odpowiedni *threshold*, według którego odpowiednio klasyfikowane są piksele. *Threshold* może być ustalony jeden dla całego obrazu albo może mieć różne wartości dla różnych części zdjęcia (*adaptive thresholding*).
* 
<p align="center">
<img src="https://miro.medium.com/max/2400/1*KTMCWiv4WZRlIpZSs5kupw.jpeg" height="400px">
</p>

* **Korekcja nachylenia**, czyli przekrzywienie obrazu w celu nadania mu właściwego formatu i kształtu - tekst powinien pojawiać się poziomo i nie powinien być pochylony pod żadnym kątem. Może to być wykonane w na przykład taki sposób:
    - rzutujemy binaryzowany obraz poziomo (czyli bierzemy sumę pikseli wzdłuż wierszy macierzy obrazu), aby uzyskać histogram pikseli wzdłuż wysokości obrazu
    - obracamy obraz w małym przedziale kątów i obliczamy różnicę między wierzchołkami histogramu. Kąt, przy którym mamy maksymalną różnicę między wierzchołkami to nasz kąt nachylenia.
    - po znalezieniu kąta nachylenia obracamy nasz obraz o kąt przeciwny do kąta nachylenia i otrzymujemy dobrze wypoziomowany obraz.

<div style="text-align:center">![Korekcja nachylenia](https://miro.medium.com/max/610/1*b76nvNcSUNwMnBdm1rd7WQ.gif)</div>

* **Odchudzanie i szkieletowanie**, których to używa się w przypadku gdy badamy tekst pisany ręcznie. Procesy te pomagają nam uzyskać jednolitą grubość kresek, co polepsza dokładność wyników OCR.

* **Usuwanie szumów**, którego głównym celem jest wygładzenie obrazu poprzez usunięcie małych kropek, które mają większą intensywność niż reszta obrazu. Usuwanie szumów może być wykonywane zarówno dla obrazów kolorowych jak i binarnych.

Poniżej przykład preprocessingu wykonanego na 3 próbkach odręcznie pisanego tekstu.

<div style="text-align:center">![Preprocessing](https://miro.medium.com/max/700/1*Yajazz-a5PwbFOYS9w7nlg.png)</div>


