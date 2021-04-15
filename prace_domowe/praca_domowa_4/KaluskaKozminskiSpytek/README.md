# Zadanie domowe nr 4 - Metryki jakości modelu i regularyzacja

## Metryki jakości

Celem weryfikacji skuteczności modelu zaimplementowaliśmy funkcje mierzące wartości metryk jakości. Zadanie rozwiązywane przez badany obiekt jest zadaniem segmentacji - próbujemy opisać dokładny kształt przestrzenie płuc w obrazie tomografii komputerowej. Osiągnięte przez model wyniki zostały zaprezentowane w poniższej tabeli.


| Metryka                               | Wartość       |
| ------------------------------------- |:-------------:|
| Dokładność                            | 0.994         |
| Precyzja                              | 0.985         |
| Czułość                               | 0.981         |
| Swoistość                             | 0.997         |
| Dice Coefficient                      | 0.983         |
| Współczynnik Giniego                  | 0.978         |
| ROC (AUC)                             | 0.989         |
| Pixel Accuracy                        | 0.994         |
| Intersection over Union               | 0.967         |
| Średni Hausdorff distance             | 0             |
| Średni Average surface distance       | 4.79          |

Wartości metryk obliczone na testowym zbiorze ograzów z tomografu wskazują na wysokie umiejętności segmentacji modelu. Spośród miar przyjmujących wartość od 0 do 1, gdzie pożądana jest 1, najniższą wartość osiągnęła metryka Intersection over Union, zwana również indeksem Jaccarda. Bardzo wysoka wartość swoistości nie powinna zaskakiwać - oznacza ona, że 99.7% czarnych pikseli została poprawnie zidentyfikowana. Biorąc pod uwagę, że znaczną część obrazów stanowi czarne tło, nie jest to dziwne.

Należy zwrócić uwagę na zaskakujące wartości metryk opierających się na odległości obrysu segmentowanych tkanek płucnych - Haudorff distance oraz average surface distance. Ponieważ obie metryki są obliczane dla każdego z obrazów testowych (a było ich 307), przedstawiona powyżej wartość jest średnią z wartości na obserwacjach testowych. Metryki zostały zmierzone przy pomocy funkcji z pakietu [surface-distance](https://github.com/deepmind/surface-distance) (tam znajduje się też instrukcja instalacji).

Graficzne metryki, takie jak krzywa ROC, krzywa Precyzja - Czułość oraz histogram z wartości metryk surface-distance i przykładowe wyniki segmentacji zostały dołączone do poniższego pliku w folderze [performance](./performance). Kod wyznaczający wartości metryk znajduje się w [code](./code)
