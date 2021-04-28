

## 2 Skorzystanie z innych frameworków

### 2.1 tf_explain

Zdecydowaliśmy się na skorzystanie z biblioteki [tf_explain](https://github.com/sicara/tf-explain). Udostępnia ona kilka metod XAI, które nie są dostępne w poprzednich frameworkach. Niestety nie wszystkie z nich nadają się do wyjaśniania problemu segmentacji. Do naszego problemu można użyć co najmniej dwóch metod udostępnianych w tym pakiecie.

Pierwszą z nich autorzy nazwali GradCAM. Metoda opiera się na analizie gradientów w warstwach aktywacyjnych. Na danych z naszego modelu prezentuje się to następująco: 

!["GradCAM"](./img/grad_cam.png)

Jak widać model zwraca uwagę na wszystkie tkanki poza wewnątrz ciała człowieka. Ignoruje natomiast obszar poza nim. Większą uwagę poświęca też granicom między płucami a innymi częściami ciała.

Drugą metodą z tego pakietu, którą zastosowaliśmy jest Occlusion Sensitivity. Metoda ta polega na iteracyjnym przesłanianiu poszczególnych części obrazka wejściowego i sprawdzania wpływu tego przesłonięcia na wynik. Dla innego obrazka z naszych danych wyjaśnienie wygląda tak:

!["Occlusion Sensitivity"](./img/oc.png)

Jak widać, wyniki tej metody również wskazują na poprawne działanie modelu.