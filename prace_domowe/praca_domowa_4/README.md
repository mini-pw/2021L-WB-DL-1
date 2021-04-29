## Praca domowa nr 4 - Metryki jakości modelu i regularyzacja

#### 1. Miary jakości
Zaimplementuj podane metody ewaluacji jakości modelu. Opisz, co z nich wynika oraz z czym model radzi sobie lepiej, a z czym gorzej.

Dla segmentacji:
* confusion matrix z dobranym progiem IoU ≥ α np. α=0.4 dla segmentacji zmian w płucach, α=0.8-0.9 dla segmentacji płuc
* dokładność
* precyzja
* czułość
* swoistość
* Dice Coefficient
* ROC
* współczynnik Giniego
* pole pod wykresem krzywej ROC (AUC)​
* pixel accuracy
* Intersection over Union
* Hausdorff distance
* mean / average surface distance

Dla klasyfikacji:
* confusion matrix
* dokładność
* precyzja
* czułość
* swoistość
* ​F1
* ROC
* współczynnik Giniego
* pole pod wykresem krzywej ROC (AUC)​
* Cohen Kappa


#### 2. Regularyzacja L1 i L2
Wprowadź regularyzację L1 oraz L2. Porównaj uzyskane wyniki - bez regularyzacji, z regularyzacją L1 oraz regularyzacją L2. Która jest lepsza w Twoim przypadku i dlaczego?

Jeśli masz ciekawy pomysł na napisanie własnego regularyzatora, który może będzie działał lepiej dla Twojego modelu, to możesz zamienić L1 lub L2 (tą, która Twoim zdaniem będzie się gorzej sprawowała) i przetestować swój pomysł. Koniecznie omów wyniki i opisz swój pomysł :)


#### 3. Mechanizm porzucania
(Całe zadanie tylko dla klasyfikacji) Zaimplementuj mechanizm porzucania. Porównaj wyniki przed i po. Jak mechanizm porzucania wpływa na wagi sieci? Pokaż wagi tego fragmentu sieci i omów zaobserwowane zmiany. Jeśli w Twojej sieci już jest Dropout to możesz go zmienić o znaczącą wartość (np. 30-40), albo usunąć go.

