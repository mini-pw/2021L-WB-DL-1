Znajdują się tu pliki: train\_pixels.npy oraz test\_pixels.npy, do umieszczenia w folderze processed\_data, zawierające etykiety dla dodatkowego zadania (regresja liczby pikseli o wartości 1). Zostały one utworzone za pomocą kodu w pliku new_labels.ipynb.

Plik models_PD5_auxiliary_task.py zawiera funkcję zwracającą model, delikatnie zmieniony w celu rozwiązywania dodatkowego zadania,

Plik log...csv to wartości funkcji straty i metryk w 20 epokach po dodaniu zadania dodatkowego.

~Paweł

Notatnik GAN_for_images_with_masks.ipynb pokazuje alternatywne podejście do generowania zdjęć, które wymaga bardzo długiego trenowania.

~Marysia


Po komentarzu w PR zmieniłem nazwy plików. Teraz w pliku unsupervised_autoencoder_architecture znajduje się cała architektura potrzebna do wykonania pretrainingu (zadanie 3), natomiast w pliku model_training_with_unsupervised_pretraining znajduje się skrypt, który stosuje ten pretraining do modelu z wyjściowego artykułu.

~Mikołaj
