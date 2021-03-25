### Grupa: Kurowski Mróz Podsiad

## Praca domowa nr 2 - Architektura sieci neuronowych

### Wybrana sieć

Zdecydowaliśmy się na zmodyfikowanie sieci VGG ze względu na jej przejrzystą strukturę i to że zwracała najlepsze wyniki w naszych poprzednich testach.
Postanowiliśmy nie modyfikować funkcji aktywacji oraz kształtu inputu, żeby ułatwić testowanie. Oprócz tego funkcja ReLu jest uważana za najskuteczniejszą przy sieciach neuronowych o takiej liczbie warstw i skomplikowanej architekturze.

### Modyfikacje:

1. zmiana wartości filtra z 16 na 32 w ostatniej warstwie
2. dodanie nowej warstwy konwolucyjnej na końcu sieci 
3. dodanie gęstej warstwy wyjściowej 

### Co się zmieniło:

1. więcej osób jest zaklasyfikowanych jako zdrowe
2. a
3. a
 
 Zmodyfikować sieć neuronową używaną w artykule. Można to zrobić całościowo, albo częściowo.

Rekomendowane podejścia:
- samemu
- poszukać rozwiązań z innych artykułów.

Chciałabym, aby każda osoba zrobiła swoją zmianę w sieci, co daje w sumie trzy różne zmiany na grupę. Wyjątkiem jest grupa, która musi napisać jeszcze trenowanie sieci - ona ma o jedną zmianę mniej do zrobienia.

Jeśli komuś uda się osiągnąć lepsze wyniki od aktualnych, to ekstra. Jeśli nie, to normalne. Przecież uczymy się na tych przykładach. Co chciałabym to, aby wyniki były lepsze od losowych.

Proszę uzasadnić wybrany pomysł na zmianę i dlaczego taką zmianę zdecydowało się wprowadzić.

Prócz wprowadzenia zmiany, chciałabym, abyście pokazali / napisali co ona zmieniła np. metryki jakości modelu, czas trenowania.
