

import numpy as np
import scipy
import matplotlib.pyplot as plt


folder = './processed_data/'
tr_data    = np.load(folder+'data_train.npy')
tr_data    = np.expand_dims(tr_data, axis=3)

tr_data   = tr_data /255.



indexes = [1,100, 435]
counter = 0 
fig,ax = plt.subplots(6, 2, figsize=[30,80])
for sss in indexes:

    ax[0+counter,0].hist(np.reshape(tr_data[sss,: ,:, 0], (262144,)))
    # ax[0,0].title("Histogram of image before transformation")
    # plt.hist()
    # plt.show()

    ax[counter+0,1].imshow(np.uint8(np.squeeze(tr_data[sss]*255)), cmap="gray")

    reshaped = np.reshape(tr_data[sss,: ,:, 0], (262144,))
    mini = reshaped.min()
    print(mini)
    maxi = reshaped.max()
    print(maxi)
    diff = maxi - mini
    temp = np.array([None for i in range (512*512)])
    for i in range(512*512):
        temp[i] = (reshaped[i] - mini)/(diff)
    tr_data[sss,:, :, 0] = np.reshape(temp, (512,512))


    ax[counter+1,0].hist(np.reshape(tr_data[sss,: ,:, 0], (262144,)))

    ax[counter+1,1].imshow(np.uint8(np.squeeze(tr_data[sss]*255)), cmap="gray")
    counter+=2


plt.savefig("contrast_stretching.png")


