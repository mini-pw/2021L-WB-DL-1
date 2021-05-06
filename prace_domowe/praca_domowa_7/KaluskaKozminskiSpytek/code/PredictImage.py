import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

class PredictImage(keras.callbacks.Callback):
    def __init__(self, obs, fov, im_dir):
        super(PredictImage).__init__()
        self.obs = obs
        self.fov = fov
        self.im_dir = im_dir
        self.init_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    def on_epoch_end(self, epoch, logs=None):
        try:
            #predictions = self.model.predict(self.obs, batch_size=1, verbose=1)
            preds = self.model.predict(self.obs, batch_size=1, verbose=1)
            predictions = preds[0]
            #print(preds[1], preds[1].shape)
            #print(preds[0].shape)
            predictions = np.squeeze(predictions)
            predictions = np.where(predictions>0.5, 1, 0)
            Estimated_lung = np.where((self.fov - predictions)>0.5, 1, 0)
            for i in range(len(Estimated_lung)):
                plt.imshow(np.squeeze(Estimated_lung[i]), cmap='gray')
		plt.text(15, 35, str(epoch), bbox={'facecolor':'white', 'pad': 3})
                pathIm = self.im_dir + 'image_' + str(i+1) + "_epoch_" + str(epoch) + '_' + self.init_time + '.png'
                if not os.path.isfile(pathIm):
                    open(pathIm, 'a').close() 
                plt.savefig(pathIm)
        except Exception as e:
            print(f'Epoch {epoch} - image not produced.')
            print(e)

