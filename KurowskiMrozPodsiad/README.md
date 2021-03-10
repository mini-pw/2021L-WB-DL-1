### Grupa: Kurowski Mróz Podsiad

## Instrukcje odpalenia DeepCOVIDExplainer

1. Stworzenie wirtualnego środowiska
	- Wersja Pythona 3.6 (3.6.9 lub nowsza)
	- numpy 1.18.1
	- tensorflow 1.14.0
	- keras 2.3.1
	- najnowsze kompatybilne wersje: 
		- matplotlib, scipy, scikit-learn, pandas, pydicom, ipython, jupyter, ipykernel, opencv, torch, PIL, xlrd, openpyxl, weightwatcher, innvestigate
2. Instalacja CUDA (?)
3. Dodanie przy imporcie plików z folderów *Classifiers* oraz *utils* żeby importowały się bez problemu
	> import sys  
	> sys.path.insert(0, '..')
4. Stworzenie datasetu COVIDx zgodnie z instrukcjami zawartymi w https://github.com/lindawangg/COVID-Net/blob/master/docs/COVIDx.md
5. Własnoręczny preprocessing datasetu wyżej do odpowiedniej formy:
	- X: zdjęcia w wymiarach 224x224x3 gdzie ostatni wymiar to skala RGB
	- y: etykiety normal/COVID-19/pneumonia jako 0/1/2
   
Robimy to za pomocą skryptu image_loader.ipnb
