### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 6 - Wyjaśnialna sztuczna inteligencja (XAI)

#### 1. Użyć biblioteki iNNvestigate

Poprawiliśmy implementację wykorzystania iNNvestigate zaproponowaną przez autorów. 
Sama wizualizacja działa, ale nie mogliśmy zweryfikować, jak poprawnie.


Niestety natrafiliśmy na poważny problem, którego na razie nie udało nam się rozwiązać.
Mianowicie nie jesteśmy w stanie załadować poprawnie modelu, który wytrenowaliśmy i zapisaliśmy za pomocą funkcji model.save() lub model.save_weights() z biblioteki keras.
Po wczytaniu modelu i uruchomieniu predykcji na zbiorze testowym dostajemy zupełnie inne wyniki niż uruchamiając ten sam kod na modelu zaraz po wytrenowaniu.
Czytaliśmy o tym problemie w internecie, niestety nie znaleźliśmy na razie żadnego sensownego rozwiązania. Przypuszczamy, że może to być niezgodność bibliotek keras i tensorflow.
Na razie przedstawiamy wyniki na błędnych modelach.  

Porównanie dla modeli przedstawia trzy metody: LRP, GradCAM oraz GradCAM+. W modelu ResNet bez względu na poprawność wag nie da się uruchomić metody LRP, ponieważ nie toleruje on warstw softmax, które są w tym modelu.

Krótki opis metod:

- Layer-wise Relevance Propagation (LRP) to ogólne podejście do wyjaśnienia przewidywań AI. Jego interpretacja matematyczna to Głęboka Dekompozycja Taylora sieci neuronowej.
- Gradient-weighted Class Activation Mapping (Grad-CAM), wykorzystuje gradienty wag między warstwami, przeyłając informację do końcowej warstwy konwolucyjnej w celu wytworzenia zgrubnej mapy lokalizacyjnej, podkreślającej ważne regiony w obrazie dla przewidywania konceptu.
- Grad-CAM+ to uogólniona technika wizualizacji do wyjaśniania decyzji CNN, która poprawia wyżej wymienioną metodę i zapewnia bardziej ogólne podejście.

Implementacja dla ResNet:

<p align="center">
<img src="https://i.imgur.com/z8pbgtr.png" width="800">
</p>

<p align="center">
<img src="https://i.imgur.com/7qh708h.png" width="800">
</p>

Implementacja dla VGG:

<p align="center">
<img src="https://i.imgur.com/8hx1hyt.png" width="800">
</p>

<p align="center">
<img src="https://i.imgur.com/dNFcgef.png" width="800">
</p>

<p align="center">
<img src="https://i.imgur.com/qkg4clw.png" width="800">
</p>

#### 2. Znaleźć dwa inne frameworki i uruchomić na swojej sieci

##### 2.1. tf-explain

Użyliśmy biblioteki *tf-explain* ( https://github.com/sicara/tf-explain ) głównie ze względu na to, że jest tam zaimplementowane Occlussion Sensitivity, którego nie mamy w iNNvestigate. 

Metoda ta polega na wizualizacji wpływu części obrazu na pewność sieci neuronowej poprzez iteracyjne zasłanianie części obrazu. W praktyce dostajemy heatmapę dla wybranej etykiety która pokazuje nam, które obszary dają nam większą pewność tej etykiety, a które mniejszą. Z powodu losowości wag przy ładowaniu modelu możemy tylko pokazać że faktycznie się odpala:

<p align="center">
<img src="https://i.imgur.com/8LtO2Fo.png " width="800">
</p>
