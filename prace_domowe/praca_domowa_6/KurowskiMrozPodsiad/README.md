### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 6 - Wyjaśnialna sztuczna inteligencja (XAI)

#### 1. Użyć biblioteki iNNvestigate

Poprawiliśmy implementację wykorzystania iNNvestigate zaproponowaną przez autorów. 
Sama wizualizacja działa, ale nie byliśmy w stanie zweryfikować, jak poprawnie.


Niestety natrafiliśmy na poważny problem, którego na razie nie udało nam się rozwiązać.
Mianowicie nie jesteśmy w stanie załadować poprawnie modelu, który wytrenowaliśmy i zapisaliśmy za pomocą funkcji model.save() lub model.save_weights() z biblioteki keras.
Po wczytaniu modelu i uruchomieniu predykcji na zbiorze testowym dostajemy zupełnie inne wyniki niż uruchamiając ten sam kod na modelu zaraz po wytrenowaniu.
Czytaliśmy o tym problemie w internecie, niestety nie znaleźliśmy na razie żadnego sensownego rozwiązania. Przypuszczamy, że może to być niezgodność bibliotek keras i tensorflow.
Na razie przedstawiamy wyniki na błędnych modelach.  

Porównanie dla modeli przedstawia trzy metody: LRP, GradCAM oraz GradCAM+. W modelu ResNet bez względu na poprawność wag nie da się uruchomić metody LRP, ponieważ nie toleruje on warstw softmax, które są w tym modelu.
