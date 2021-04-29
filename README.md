## Warsztaty Badawcze - grupa 2021L-WB-DeepLearning-1

Tematem zajęć jest uczenie głębokie (deep learning). Podczas laboratoriów zapoznamy się z najważniejszymi elementami uczenia głębokiego.

### Zakres tematyczny
Na zajęciach każda grupa dostanie artykuł naukowy z dołączonym do niego kodem do analizy i pracy na nim. Będziemy pracować z językiem Python i biblioteką Keras do tworzenia oraz trenowania sieci neuronowych. Artykuł będzie skupiał się na zagadnieniu segmentacji lub kategoryzacji medycznych zdjęć płuc. Temat został wybrany ze względu na wciąż aktualny temat pandemii COVID-19.<br/>
Zajęcia będą prowadzone na podstawie książki Francois Cholleta "Deep Learning. Praca z językiem Python i biblioteką Keras".

### Terminy i tematy zajęć

<table>
<thead>
  <tr>
    <th>ZAJĘCIA</th>
    <th>DATA</th>
    <th>TEMAT</th>
    <th>ZAKRES</th>
    <th>ZADANIE</th>
    <th>PUNKTY</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>2021-02-26</td>
    <td>Organizacja pracy. Wprowadzenie do tematyki zajęć.</td>
    <td>Przydzielenie projektów (artykuł naukowy z kodem).</td>
    <td>Uruchomienie kodu.</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>2021-03-04</td>
    <td>Wprowadzenie do DL (rozdz. 1)</td>
    <td>Deep Learning – co to takiego?</td>
    <td>Uruchomienie kodu c.d.</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>2021-03-11</td>
    <td>Podstawy sieci neuronowych (rozdz. 2)</td>
    <td>Rozpoznawanie typowych struktur danych w kodzie. Zbiory danych do trenowania głębokich sieci neuronowych.</td>
    <td>Przygotowanie informacji o wykorzystywanych zbiorach danych. Sprawdzenie zbalansowania danych.</td>
    <td>5 pkt.</td>
  </tr>
  <tr>
    <td>4</td>
    <td>2021-03-18</td>
    <td>Budowa sieci neuronowych (rozdz. 3)</td>
    <td>Omówienie i rozpoznawanie w kodzie poszczególnych elementów sieci neuronowej.</td>
    <td>Architektura sieci neuronowej.</td>
    <td>5 pkt.</td>
  </tr>
  <tr>
    <td>5</td>
    <td>2021-03-25</td>
    <td>Podział danych na zbiory. Preprocessing danych (rozdz. 4.1-4.3, 4.5.3, 4.5.4)</td>
    <td>Jakie są typowe podziały na zbiór treningowy, walidacyjny i testowy. W jaki sposób i po co obrabiamy zdjęcia przed treningiem.</td>
    <td>Podział na zbiór treningowy, walidacyjny, testowowy. Preprocessing danych.</td>
    <td>6 pkt.</td>
  </tr>
  <tr>
    <td>6</td>
    <td>2021-04-01</td>
    <td>Omówienie prac domowych</td>
    <td>Prezentacja przeprowadzonego researchu literaturowego.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td>2021-04-08</td>
    <td>Jak długo trenować sieć (rozdz. 4.4-4.5) </td>
    <td>Jak uniknąć nadmiernego dopasowania się sieci do zbioru treningowego. Jakie mamy miary oceny jakości modelu.</td>
    <td>Ocena dopasowania modelu - co zrobili, aby ograniczyć nadmierne dopasowanie. Obliczyć pole pod ROC + inne metryki.</td>
    <td>5 pkt.</td>
  </tr>
  <tr>
    <td>8</td>
    <td>2021-04-15</td>
    <td>Gdy danych do trenowania jest mało (rozdz. 5.1-5.2) Transfer learning (rozdz. 5.3-5.4)</td>
    <td>Techniki augmentacji danych. Jak korzystać z sieci neuronowych wytrenowanych na ogromnych zbiorach danych.</td>
    <td>Wypisanie jakie techniki augmentacji są stosowane + dodać nowe/zmodyfikować obecne. Załadować wagi z innego modelu.</td>
    <td>9 pkt.</td>
  </tr>
  <tr>
    <td>9</td>
    <td>2021-04-22</td>
    <td>Wizualizacja</td>
    <td>Wizualizacja efektów trenowania sieci</td>
    <td>Zwizualizować efekty trenowania.</td>
    <td>5 pkt.</td>
  </tr>
  <tr>
    <td>10</td>
    <td>2021-04-29</td>
    <td>Najlepsze praktyki (rozdz. 7)</td>
    <td>Co zrobić by w pełni korzystać z możliwości modeli i lepiej monitorować ich trenowanie.</td>
    <td>Rozszerzenie isniejącej implementacji o zaawansowane techniki.</td>
    <td>5 pkt.</td>
  </tr>
  <tr>
    <td>11</td>
    <td>2021-05-06</td>
    <td>Podsumowanie nauki DL (rozdz. 9). Konsultacje prezentacji</td>
    <td>Posumowanie, czego się nauczyliśmy. Konsultacje przed prezentacją końcową. </td>
    <td>Przygotowanie prezentacji końcowej.</td>
    <td></td>
  </tr>
  <tr>
    <td>12</td>
    <td>2021-05-13</td>
    <td>Konsultacje raportu</td>
    <td>Dyskusja na temat raportu.</td>
    <td>Łączenie dotychczasowych prac w raport.</td>
    <td></td>
  </tr>
  <tr>
    <td>13</td>
    <td>2021-05-20</td>
    <td>Konsultacje raportu</td>
    <td></td>
    <td>Wstępne oddanie raportu - dla chętnych. </td>
    <td></td>
  </tr>
  <tr>
    <td>14</td>
    <td>2021-05-27 </td>
    <td colspan="3"> Prezentacja projektu (max. 15 min na grupę)  </td>
    <td>20 pkt.</td>
  </tr>
  <tr>
    <td></td>
    <td>2021-06-04 </td>
    <td colspan="3"> Oddanie projektu.</td>
    <td>40 pkt.</td>
  </tr>
  <tr>
    <td>15</td>
    <td>2021-06-10</td>
    <td>Podsumowanie przedmiotu</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>


### Zasady oceniania (suma 100 pkt)

-   raport końcowy - 40 pkt.
	- wstęp, motywacja [0-8 punktów]
	- literatura [0-4 punktów]
	- główne wyniki pracy [0-16 punktów]
	- wnioski [0-8 punktów]
	- jakość wykresów/wizualizacji/diagramów [0-4 punktów]
-   prezentacja - 20 pkt.
	- prezentacja wyników projektu podczas wykładu (oceniana przez wszystkich prowadzących)
-   praca na laboratoriach - 40 pkt.


### Krótka instrukcja uzupełniania rozdziałów książki

Link do [książki](https://github.com/mini-pw/2021L-WB-Book)

Dodając pliki, obrazki, pozycje w bibliografii i pull requesty proszę oznaczać je według następującego schematu: `numeru grupy_numeru zespołu_dalsza nazwa`.

Obrazki wrzucamy do folderu *images*.

* [PiatyszekMarciniakFrej] - zespół nr **1**, czyli `3_1_...`
* [KaluskaKozminskiSpytek] - zespół nr **2**, czyli `3_2_...`
* [KurowskiMrozPodsiad] - zespół nr **3**, czyli `3_3_...`
* [eljasiak_krupinski_pawlak] - zespół nr **4**, czyli `3_4_...`
* [KoziełNocońStaroń] - zespół nr **5**, czyli `3_5_...`


### Niezbędna literatura:
- Francois Chollet "Deep Learning. Praca z językiem Python i biblioteką Keras" (pol)
- [François Chollet "Deep Learning with Python" (ang)](http://faculty.neu.edu.cn/yury/AAI/Textbook/Deep%20Learning%20with%20Python.pdf)
- [Jupyter notebooks do książki wspomnianej wyżej (pol)](https://ftp.helion.pl/przyklady/delepy.zip)
- [Jupyter notebooks for the book mentioned above (ang)](https://github.com/fchollet/deep-learning-with-python-notebooks)

