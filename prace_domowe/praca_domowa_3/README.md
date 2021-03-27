## Praca domowa nr 3 * Preprocessing

##### 1. Jaki preprocessing jest stosowany w Twoim artykule?
* Wymienić i opisać na czym polegają te metody
* Wskazać miejsca w artykule i miejsce w kodzie, gdzie jest napisane o preprocessingu (fragmenty artykułu + fragmenty kodu)

##### 2. Pozmieniaj zaimplementowane obecnie techniki preprocessingu – po trzy różne ulepszenia, w tym:
* dla klasyfikacji: transformata np. Fouriera
* dla segmentacji: operacje na histogramie

##### 3. Sprawdzić, jaki preprocessing jest często stosowany do:
* [**PiatyszekMarciniakFrej**] Klasyfikacji zdjęć histopatologicznych
* [**KaluskaKozminskiSpytek**] CT głowy (z kontrastem i bez)
* [**KurowskiMrozPodsiad**] OCR
* [**eljasiak_krupinski_pawlak**] Rozpoznawania znaków drogowych
* [**KoziełNocońStaroń**] Detekcji różnorodnych obiektów na zdjęciach

##### 4. Tematy do zbadania:

* [**PiatyszekMarciniakFrej**] Czy można karmić sieć obrazkami prostokątnymi, a nie kwadratowymi? Co trzeba zrobić, aby to móc zrobić.
Jaka była największa rozdzielczość obrazków jakimi karmiona sieć (dla danych niemedycznych i medycznych)?
* [**KaluskaKozminskiSpytek**] Wyszukaj informacji o sieciach, które biorą obrazki z wartościami pikseli większymi niż 0-255 (8-bitów). Napisz, co zostało zmodyfikowane, aby móc się posługiwać takimi obrazkami i dlaczego.
* [**KurowskiMrozPodsiad**] Napisz, jak wykrywać i pozbywać się liter z obrazków? Opisz i porównaj różne techniki + które kiedy stosować. Jak wykrywać i lokalizować obecność innych artefaktów na zdjęciach? Jak je usuwać?
* [**eljasiak_krupinski_pawlak**] Porównaj techniki odszumiania zdjęć i usuwania rozmazania (blur removal, deblur). Kiedy stosować które techniki (dla danych niemedycznych i medycznych) + konkretne przykłady.
* [**KoziełNocońStaroń**] Jakie są techniki zwiększania rozdzielczości zdjęcia? Opisz techniki. Znajdź artykuły, które stosowały taki zabieg w preprocessingu.


##### 5. Prezentacja wyników na zajęciach
Oprócz odpowiedzi na zadania 3 i 4, proszę zaprezentować je na kolejnych zajęciach.
Chciałabym, abyście zastanowili się, dlaczego podane operacje się robi, albo się ich nie robi i ewentualnie kiedy można z nich skorzystać. Ponadto chciałabym, aby każdy z grupy coś powiedział.
