# Opis naszej dotychczasowej pracy

Pracujemy z artykułem i kodem dostępnymi w repozytorium: [https://github.com/rezazad68/BCDU-Net](https://github.com/rezazad68/BCDU-Net), a w szczególności jego częścią dotyczącą segmentacji płuc.

### 05.03.2021

Każdemu z nas udało się uruchomić kod dostarczony przez autora artykułu.


**tu wpisałem swoje wersje, ale możemy uzgodnić, żebyśmy wszyscy na takich samych robili, albo po prostu najnowszych**

Program został uruchominy na wersjach:
- `python 3.8.7`
- `keras==2.4.3`
- `tensorflow==2.4.1`

Zmiany, których dokonaliśmy, aby się to nam udało:

- W pliku  `Prepare_data.py` na początku dodaliśmy linię `import os`, gdyż występował błąd przy zapisie; 
- W pliku `models.py` dodaliśmy linię `import numpy as np`, gdyż są tam użyte metody z tego pakietu;
- Również w pliku `models.py` przy definicji obiektu `model` zmieniliśmy nazwy parametrów w konstruktorze.zamiast `input, output` należało użyć `inputs, outputs`.

W ten sposób uzyskaliśmy działający program, ale wprowadziliśmy kolejne modyfikacje, aby w pełni użyć możliwości obliczeniowych naszych komputerów i przyspieszyć trenowanie modelu:

- W plikach `train_lung.py` oraz `evaluate_performance.py` dodaliśmy następujący kod:
```
import tensorflow as tf

config = tf.compat.v1.ConfigProto(gpu_options =
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
# device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)
```
- W pliku `train_lung.py` dodaliśmy parametr `save_weights_only=True` do tworzenia `ModelCheckpoint`

Dodatkowo zainstalowaliśmy `CUDA 11.2.1` oraz dodaliśmy bibliotekę `cuDNN 11.1`.



//Notatka robocza: Wymagane pakiet nibabel oraz scipy, oczywiście matplotlib i sklearn. Problem z evaluate? 
