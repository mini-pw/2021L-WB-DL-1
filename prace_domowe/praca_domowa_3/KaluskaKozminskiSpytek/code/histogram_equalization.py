

import numpy as np
import scipy
import matplotlib.pyplot as plt


folder = './processed_data/'
tr_data    = np.load(folder+'data_train.npy')
tr_data    = np.expand_dims(tr_data, axis=3)


tr_data   = tr_data /255.


indexes = [1,100, 435]
counter = 0 
fig,ax = plt.subplots(6, 2, figsize=[20,30])
for sss in indexes:

    ax[0+counter,0].hist(np.reshape(tr_data[sss,: ,:, 0], (262144,)))
    ax[0+counter,0].title.set_text("Histogram {} przed modyfikacją".format(counter//2+1))

    ax[counter+0,1].imshow(np.uint8(np.squeeze(tr_data[sss]*255)), cmap="gray")
    ax[counter+0,1].title.set_text("Obrazek {} przed modyfikacją".format(counter//2+1))

    reshaped = np.reshape(tr_data[sss,: ,:, 0], (262144,))
    his, be = np.histogram(reshaped, range=(0,1), bins=256)
    his = his.astype(float)/sum(his)
    
    tr_data[sss,:, :, 0] = np.reshape(np.interp(reshaped, be, np.hstack((np.zeros((1)), np.cumsum(his)))), (512,512))


    ax[counter+1,0].hist(np.reshape(tr_data[sss,: ,:, 0], (262144,)))
    ax[counter+1,0].title.set_text("Histogram {} po modyfikacji".format(counter//2+1))

    ax[counter+1,1].imshow(np.uint8(np.squeeze(tr_data[sss]*255)), cmap="gray")
    ax[counter+1,1].title.set_text("Obrazek {} po modyfikacji".format(counter//2+1))
    counter+=2


plt.savefig("hist_eq.png")

