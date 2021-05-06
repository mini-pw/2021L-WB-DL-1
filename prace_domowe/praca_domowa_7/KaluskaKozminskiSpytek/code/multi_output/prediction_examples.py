import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import numpy as np
import matplotlib.pyplot as plt
from multi_output_model import MultiOutputModel
import tensorflow as tf

config = tf.compat.v1.ConfigProto(gpu_options=
                                  tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
                                  )
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)

#===============================================
folder = 'C:\\Users\\marys\\OneDrive\\Dokumenty\\STUDIA\\Semestr 4\\Warsztaty badawcze\\BCDU-Net\\Lung Segmentation\\processed_data\\'
te_data = np.load(folder + 'data_test.npy')
FOV = np.load(folder + 'FOV_te.npy')
te_mask = np.load(folder + 'mask_test.npy')
te_labels = np.load(folder + 'test_labels.npy')

te_data = np.expand_dims(te_data, axis=3)
te_data2 = te_data / 255.
print('Dataset loaded')

model = MultiOutputModel().build(input_size=(512, 512, 1))

model.load_weights('weights/wagi_multi.h5')

labels = {1: 'upper',
          0: 'lower'}
fig, ax = plt.subplots(4, 2, figsize=[10, 20])
row = 0
indices = [4, 100, 209,250]
predictions = model.predict(te_data2[indices])
clf_pred = predictions[0].squeeze()
clf_pred = np.where(clf_pred > 0.5, 1, 0)

seg_pred = predictions[1].squeeze()
seg_pred = np.where(seg_pred > 0.5, 1, 0)
Estimated_lung = np.where((FOV[indices] - seg_pred) > 0.5, 1, 0)

for i in indices:
    ax[row, 0].imshow(te_data2[i].squeeze(), cmap='bone')
    ax[row, 0].title.set_text(labels[clf_pred[row]])
    ax[row, 1].imshow(Estimated_lung[row].squeeze())
    row += 1
plt.savefig('examples_multi_output_model.png')