## Praca domowa nr 6 - Wyjaśnialna sztuczna inteligencja (XAI)

W przypadku jeśli będziemy podawać zdjęcie do modelu, to proszę o pokazanie działania modelu na przykładach dobrze zaklasyfikowanych, jak i tych źle.

Gdy mówimy o klasyfikacji COVID-19, to można stwierdzić, że wszystkie obszary istotne powinne być zaznaczone wewnątrz płuc.

Sprawdźcie też Wasz model na przypadkach wizualnie trudnych lub zawierających artefakty pojawiające się w bazie danych.


#### 1. Użyć biblioteki iNNvestigate


Jeśli nie działa [iNNvestigate](https://github.com/albermax/innvestigate) sprawdź np. issues na Githubie.

Dla grupy, która miała już iNNvestigate zaimplemenotowany, to poproszę ją o uruchomienie iNNestigate również na drugim modelu i pokazanie różnic między wyjaśnieniami dwóch modeli. Proszę sprawdzić, czy otrzymane wyjaśnienia zależą od pewności modelu w klasyfikacji do danej klasy.


#### 2. Znaleźć dwa inne frameworki i uruchomić na swojej sieci
Chciałabym, aby te frameworki do wyjaśnień sieci nie zawierały dokładnie takich samych metod XAI co iNNvestigate.

Można użyć [explAIner](https://arxiv.org/pdf/1908.00087.pdf).

Można też poszukać ich np. [tutaj](https://github.com/pbiecek/xai_resources/blob/master/README.md#tools) lub po prostu w Internecie.

Jeśli ktoś chciałby, to jeden z dwóch frameworków do wyjaśnień można zamienić na jakąś metodę ataku na sieć (adversarial attacks).


#### 3. Zadanie dla tych, którym mimo starań coś nie działa

Przede wszystkim należy napisać, co nie działa i co dokładnie jest tego powodem - zapewnić, że tego nie da się obejść.

Następnie proszę zaimplementować po dwie metody XAI.

Proszę, aby w miarę możliwości te metody nie pojawiały się one w poprzednich zadaniach i nie były bardzo podobne do siebie.

Proszę też bez LIME - nie jest on moim zdaniem metodą dobrze pokazującą wyjaśnienia dla płuc.
