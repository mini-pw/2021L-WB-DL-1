### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 2 - Architektura sieci neuronowych

### Wybrana sieć
Zdecydowaliśmy się na zmodyfikowanie sieci VGG ze względu na jej przejrzystą strukturę i to że zwracała najlepsze wyniki w naszych poprzednich testach. Ogółem VGG19 składa się z 5 bloków konwolucyjnych (warstwy konwolucyjne + MaxPooling) i bloku klasyfikacji z dwoma Dense Layerami (512 neuronów + Dropout 0.5 oraz 128 neuronów). Na outpucie mamy oczywiście Dense Layera z funkcją aktywacji softmax. Poza ostatnią warstwą wszystkie warstwy (gdzie jest to aplikowalne) mają funkcję aktywacji ReLu, czego zdecydowaliśmy się nie zmieniać.

### Modyfikacje
Postanowiliśmy zainspirować się podejściem “lepiej więcej niż mniej”. Poniżej wykonane przez nas zmiany w architekturze:

1. zmiana wartości filtra z 16 na 32 w ostatnim (piątym) bloku konwolucyjnym 
2. dodanie nowego (szóstego) bloku konwolucyjnego na końcu sieci z wartościami takimi jak pozostałe bloki, z wyjątkiem filtra który ustawiony został na 32
3. dodanie kolejnej gęstej warstwy (256 neuronów + Dropout 0.25 pomiędzy pierwszą a drugą gęstą warstwą) w bloku klasyfikującym

Wyniki tych zmian zamieszczone są odpowiednio w notebookach *VGG-19_zmiana1.ipynb*, *VGG-19_zmiana2.ipynb* i *VGG-19_zmiana3.ipynb*. Dla porównania umieściliśmy też *VGG-19.ipynb* w którym architektura pozostała bez zmian. Wszystkie notebooki zawierają metryki precision, recall oraz F1-score a także Confusion Matrix.

### Co się zmieniło
Poniżej krótkie podsumowanie tego, co zmieniło się po każdej wykonanej przez nas zmianie:

1. Więcej osób jest klasyfikowanych jako zdrowe lub covid;  nieznaczne zwiększenie trafności przewidywania, poza wykrywaniem pneumonii
2. Nieznacznie gorzej niż po zmianie 1; więcej ludzi zakwalifikowanych jako zdrowych, ogółem mały ale zauważalny spadek trafności sieci
3. Niewielki wzrost trafności klasyfikacji COVID19 i pacjentów bez chorób, nadal jednak porównywalnie do sieci bez zmian

W każdym przypadku wystąpił porównywalny czas trenowania sieci. Trenowanie odbyło się na danych, na których wykonany został undersampling z poprzedniej pracy domowej.

Ogólnie nasze zmiany nie polepszyły znacząco jakości klasyfikacji sieci neuronowej, ale dały nam wgląd w możliwości dostosowywania architektury sieci. Doszliśmy do wniosku, że nasze zmiany powodują nieznaczne zmiany w wynikach klasyfikacji, ale miary trafności pozostają w tym samym przedziale ~ 75-80%.

