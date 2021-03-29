### Grupa: Kurowski Mróz Podsiad

## Instrukcje odpalenia DeepCOVIDExplainer

1. Stworzenie wirtualnego środowiska
	- Wersja Pythona 3.6 (3.6.9 lub nowsza)
	- numpy 1.18.1
	- tensorflow 1.14.0 (opcjonalnie też tensorflow-gpu 1.14.0)
	- keras 2.3.1
	- h5py 2.10.0
	- weightwatcher 0.2.7
	- najnowsze kompatybilne wersje: 
		- matplotlib, scipy, scikit-learn, pandas, pydicom, ipython, jupyter, ipykernel, opencv, torch, PIL, xlrd, openpyxl, innvestigate
2. Dodanie przy imporcie plików z folderów *Classifiers* oraz *utils* żeby importowały się bez problemu
	> import sys  
	> sys.path.insert(0, '..')
3. Stworzenie datasetu COVIDx zgodnie z instrukcjami zawartymi w https://github.com/lindawangg/COVID-Net/blob/master/docs/COVIDx.md (create_COVIDx.ipynb).
4. Własnoręczny preprocessing datasetu wyżej do odpowiedniej formy za pomocą notebooka preprocess_data.ipynb:
	- X: zdjęcia w wymiarach 224x224x3 gdzie ostatni wymiar to skala RGB
	- y: etykiety normal/COVID-19/pneumonia jako 0/1/2
5. (Opcjonalnie) Instalacja CUDA 10.0 i cuDNN 7.4.2

<!--- Notebook z kodem: https://nbviewer.jupyter.org/github/z-mrozu/2021L-WB-DL-1/blob/main/KurowskiMrozPodsiad/preprocess-data.ipynb  --->
VGG19 i przykłady z wizualizacją samego VGG19 udało się odpalić. Nie zostało zamieszczone DenseNet161, więc przykład z weightwatcherem da się odpalić tylko po zakomentowniu części kodu z brakującą siecią i poprawie błędów w kodzie (results->resultsResNet etc). W przykładzie z wizualizacją ResNet-18 nadal są błędy (wczytywanie wag, wywoływanie modelu z więszką ilością argumentów niż przyjmuje), ale sam network odpala się pomyślnie. Wydaje nam się że może być to spowodowane tym, że autorzy w tej wizualizacji wczytują wcześniejszy/późniejszy model ResNet-18 który nie został zamieszczony w repozytorium.
