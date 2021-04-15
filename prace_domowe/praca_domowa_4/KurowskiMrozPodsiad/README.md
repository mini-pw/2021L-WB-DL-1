### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 4 - Metryki jakości modelu i regularyzacja

### 1. Miary jakości

TODO

### 2. Regularyzacja L1 i L2

Regularyzacja została wprowadzona przy pomocy regularyzatorów dostępnych od kerasa. Zmodyfikowaliśmy przy ich pomocy sieć VGG19 tworząc wersje z regularyzacją L1, L2 oraz obiema.

*Uzyskane rezultaty:*

L1:
<p align="center">
<img src="https://i.imgur.com/fmzHRsa.png" height="300">
</p>

L2:
<p align="center">
<img src="https://i.imgur.com/P0lZnMO.png" height="300">
</p>

L1 i L2:
<p align="center">
<img src="https://i.imgur.com/hqiP2x5.png" height="300">
</p>

Okazuje się, że najgorsze rezultaty otrzymujemy przy stosowaniu tylko regularyzacji L2.  Możemy zauważyć, że regularyzacja L1 i L2 daje najlepsze ocenianie zapalenia płuc, natomiast samo L1 daje dobre wyniki rozpoznawania normalnych płuc. Jedynym pozytywem w wynikach dla regularyzacji L2 jest to, że daje lepsze poprawne wychwytywanie płuc covidowych, ale regularyzacja L1 jest jedynie niewiele od niej gorsza.

Jednakże, dodawanie regularyzacji nie poprawia wyników:

Oryginalne VGG19:
<p align="center">
<img src="https://i.imgur.com/h0N7Uj7.png" height="300">
</p>

Jak widzimy, wersja oryginalna osiągnęła lepsze rezultaty zarówno w rozpoznawaniu płuc normalnych, jak i covidowych. Jedynym zadaniem, w którym sprawdziła się lepiej regularyzacja (tu L1 i L2) jest rozpoznawanie zapalenia płuc.

### 3. Mechanizm porzucania

W modelu VGG19 był już zaimplementowany dropout. Dla przypomnienia model ten składa się z pięciu bloków konwolucyjnych, po których występują 2 warstwy gęste (512 i 128 neuronów) z funkcją aktywacji *ReLU* i ostateczną warstwą *softmax*. *Dropout* 0.5 zaimplementowany jest pomiędzy wcześniej wspomnianymi warstwami *ReLU*. Jak widać było powyżej, tak zaprojektowana sieć działa dosyć dobrze. Po usunięciu mechanizmu *dropout* osiągamy już sporo gorsze wyniki:

Oryginalne VGG19:
<p align="center">
<img src="https://i.imgur.com/h0N7Uj7.png" height="300">
</p>

VGG19 bez Dropout 0.5:
<p align="center">
<img src="https://i.imgur.com/8rkPMMo.png" height="300">
</p>

Jest to zapewne spowodowane za pewne tym, że bez regularyzacji zapewnianej przez *dropout* dostajemy overfitting. 

Nie wyciągaliśmy już dokładnych wag po wykonaniu *dropouta*, bo przy takich ilościach neuronów są to naprawdę ogromne macierze które merytorycznie dużo nam nie dają (poza tym okazuje się, że wyciągnięcie samej maski dropoutowej - albo wag po jej zastosowaniu - to trochę czarna magia). Poniżej zamieściliśmy za to bardziej przejrzystą wizualizację tego mechanizmu. Nie jest on skomplikowany - przypadku *dropout* 0.5 losowo wyzerowuje on dokładnie połowę neuronów, co pomaga nam uniknąć overfittingu.

<p align="center">
<img src="https://i.imgur.com/ukqaJMa.png">
</p>

