### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 7 - Zaawansowane techniki

#### 1. Monitorowanie uczenia modeli

TODO

#### 2. Wiele wejść / wiele wyjść

W naszej sieci VGG postanowiliśmy dodać drugie wyjście, będące predykcją datasetu z którego pochodzi zdjęcie. Dane COVIDx pochodzą bowiem z kilku źródeł i byliśmy ciekawi jak łatwo naszemu modelowi przewidzieć z którego dokładnie. Dla przypomnienia architektura VGG poniżej:

<p align="center">
<img src="https://i.imgur.com/L06GVDv.png" width="800">
</p>

Zaczęliśmy od dosyć naiwnego podejścia, w którym rozgałęzienie zrobiliśmy w części z warstwami Dense, czyli FC1, FC2 i softmax. Niestety, jak widać poniżej, w tym przypadku sieć radziła sobie poniżej przeciętnej z wykrywaniem Covida, a z rozróżnianiem pochodzenia zdjęcia bardzo słabo. Pewnym problemem było to, że klasa *rsna* była znacznie większa niż pozostałe klasy.

<p align="center">
<img src="https://i.imgur.com/b4iPP9Z.png" width="600">
</p>

<p align="center">
<img src="https://i.imgur.com/onNAaYf.png" width="600">
</p>

Postanowiliśmy więc sprawdzić jak mają się wyniki przy zrobieniu brancha trochę wcześniej - oddzieliliśmy także trzy ostatnie bloki konwolucyjne, a do tego zaimplementowaliśmy mechanizm *class weights*. Niestety nadal nie dało nam to pożądanych efektów - co prawda COVID rozpoznawany jest tutaj lepiej, ale model w przypadku klasyfikacji datasetu wrzucał wszystko do jednego worka.

<p align="center">
<img src="https://i.imgur.com/LVaVWkK.png" width="600">
</p>

<p align="center">
<img src="https://i.imgur.com/Q9g4cYn.png" width="600">
</p>

Zdecydowaliśmy się więc w końcu na rozdzielenie modelu od samego początku, czyli od pierwszego bloku konwolucyjnego oraz zrezygnowaliśmy z *class weights*, bo nawet przy bardzo niewielkich wartościach powtarzał się przypadek z wrzucaniem wszystkiego do jednej klasy.  Niestety nawet po zrezygnowaniu z wag klas nadal działo się to samo. Nie udało nam się więc zrobić trafnej predykcji datasetów, ale też jest to jakaś informacja - widocznie nie jest łatwo rozróżnić to, z jakiego dokładnie źródła pochodzą nasze zdjęcia.

<p align="center">
<img src="https://i.imgur.com/xKkGN9r.png" width="600">
</p>

#### 3. Ensemble

Jako wstępny przykład ensemblu spróbowaliśmy połączyć dwa modele z artykułu, które udało nam się w pewnym stopniu odtworzyć - VGG oraz ResNet. Niestety uzyskane w ten sposób były dość niekorzystne: 

<p align="center">
<img src="https://i.imgur.com/Pr70cKG.png " width="600">
</p>

Przyczyny powyższego rezultatu można dopatrywać się w prawdopodobnie nieodpowiednim sposobie wczytywania wag z ResNetu, który został udostępniony przez autorów w notatniku Jupyterowym. (Wiemy, że wagi VGG wczytują się poprawnie)

Z tego powodu zdecydowaliśmy się utworzyć prosty ensemble z różnych wersji modelu VGG, które stworzyliśmy podczas warsztatów badawczych (m.in. modele z dodaniem regularyzacji l1, l2). Uzyskane rezultaty okazały się być lepszymi od tych dla połączenia VGG i ResNet.

<p align="center">
<img src="https://i.imgur.com/hxCkDvN.png " width="600">
</p>

Za dość zdumiewający może być uznany fakt, że umieszczenie w ensemble modelu wytworzonego na zdjeciach po transformacji Fouriera (FFT) poprawia wyniki ensemble, nawet jeśli zdjęcia, którymi tym razem testowaliśmy, nie przeszły rzeczonej transformacji - poniższa confusion matrix pokazuje wyniki dla ensemble bez wspomnianego modelu.

<p align="center">
<img src="https://i.imgur.com/ZmNi91b.png " width="600">
</p>

