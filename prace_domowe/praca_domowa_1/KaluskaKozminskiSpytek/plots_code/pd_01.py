import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import models as M
import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import jaccard_score
from sklearn.metrics import f1_score
from scipy.ndimage.morphology import binary_erosion
import tensorflow as tf

config = tf.compat.v1.ConfigProto(gpu_options =
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.85)
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)

policy = tf.keras.mixed_precision.experimental.Policy('mixed_float16')
tf.keras.mixed_precision.experimental.set_policy(policy)


####################################  Load Data #####################################
folder    = '../BCDU-Net/Lung Segmentation/processed_data/'
te_data   = np.load(folder+'data_test.npy')
FOV       = np.load(folder+'FOV_te.npy')
te_mask   = np.load(folder+'mask_test.npy')

te_data  = np.expand_dims(te_data, axis=3)

print('Dataset loaded')
#te_data2  = dataset_normalized(te_data)
te_data2 = te_data /255.
model = M.BCDU_net_D3(input_size = (512,512,1))
model.summary()


model.load_weights('../BCDU-Net/Lung Segmentation/weight_lung')
predictions = model.predict(te_data2, batch_size=1, verbose=1)

# Post-processing
predictions = np.squeeze(predictions)
predictions = np.where(predictions>0.5, 1, 0)
plt.imshow(np.uint8(np.squeeze(predictions[0])))
plt.savefig("test.png")
exit()
Estimated_lung = np.where((FOV - predictions)>0.5, 1, 0)

print(Estimated_lung)
print(Estimated_lung.shape)
print(Estimated_lung.dtype)
exit()
# Sample results
#fig,ax = plt.subplots(5, 5, figsize=[15,15])
all_ind = [1, 100, 200, 253, 193, 24, 32, 49, 21, 29, 121, 114, 135, 123, 198, 210, 231, 228, 239, 201, 145, 148, 152, 161, 169] # random samples
all_ind = np.array(all_ind)
for idx in range(25):
    with open("CT" + str(idx) + ".txt", 'wb') as f:
        for line in np.uint8(np.squeeze(te_data[all_ind[idx]])):
            np.savetxt(f, line, fmt = '%d')
    with open("Estimated" + str(idx) + ".txt", 'wb') as f:
        for line in np.squeeze(Estimated_lung[all_ind[idx]]):
            np.savetxt(f, line, fmt = '%d')



#print(np.uint8(np.squeeze(te_data[all_ind[5]])))
#print(np.uint8(np.squeeze(te_data[all_ind[5]])).shape)
#exit()





#for idx in range(5):
#    for idxx in range(5):
#        ax[idx, idxx].imshow(np.uint8(np.squeeze(te_data[all_ind[5*idx+idxx]])), alpha=0.4)
#        ax[idx, idxx].imshow(np.squeeze(Estimated_lung[all_ind[5*idx+idxx]]), cmap='gray', alpha = 0.4)          
#plt.savefig('sample_results.png')#
#
#fig,ax = plt.subplots(25, 2, figsize=[20,20])
#fig.suptitle("CT and Estimated masks")
#for idx in range(10):
        ax[idx, 0].imshow(np.uint8(np.squeeze(te_data[all_ind[idx]])))
        ax[idx, 1].imshow(np.squeeze(Estimated_lung[all_ind[idx]]), cmap='gray')          
plt.savefig('sample_results2.png')

