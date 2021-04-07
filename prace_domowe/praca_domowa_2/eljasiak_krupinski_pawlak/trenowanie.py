from myDense import myDenseNetv2
import scipy.io
import numpy as np
import csv

def main():
    print("test")

    #wczytywanie danych
    def import_data(t):
        t = 'dataset/' + t
        files = []
        positive = []
        with open(t + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                row = t + '/' + row[0]
                positive.append(row[-25])
                files.append(row[:-1])
        return files, positive

    train, Y_train = import_data('training')

    Y_train = np.array(Y_train)
    Y_train = np.where(Y_train == '+', 1, Y_train)
    Y_train = np.where(Y_train == '-', 0, Y_train)
    Y_train = Y_train.astype(np.float)

    X_train = []
    for fileName in train:
        mat = scipy.io.loadmat(fileName)
        data = mat['only_lung_zoomed_3std']
        data2 = mat['type']
        X_train.append(data)
    X_train = np.array(X_train)
    X_train = X_train[..., np.newaxis]
    X_train = np.swapaxes(X_train, 1, 3)
    X_train = np.swapaxes(X_train, 2, 3)

    #kompilacja modelu
    model = myDenseNetv2((48, 240, 360, 1))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    #trenowanie modelu
    model.fit(X_train,Y_train,
              epochs=10,verbose=1,
              batch_size=1,)



if __name__ == '__main__':
    main()