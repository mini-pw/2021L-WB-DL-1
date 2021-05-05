import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
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
from tensorflow import keras
from tf_explain.core.grad_cam import GradCAM
from tf_explain.core.occlusion_sensitivity import OcclusionSensitivity




####################################  Load Data #####################################
folder    = './drive/MyDrive/processed_data/'
te_data   = np.load(folder+'data_test.npy')
FOV       = np.load(folder+'FOV_te.npy')
te_mask   = np.load(folder+'mask_test.npy')

te_data  = np.expand_dims(te_data, axis=3)


print('Dataset loaded')
#te_data2  = dataset_normalized(te_data)
te_data2 = te_data /255.

!pip install tf_explain
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
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
from tensorflow import keras
from tf_explain.core.grad_cam import GradCAM




####################################  Load Data #####################################
folder    = './drive/MyDrive/processed_data/'
te_data   = np.load(folder+'data_test.npy')
FOV       = np.load(folder+'FOV_te.npy')
te_mask   = np.load(folder+'mask_test.npy')

te_data  = np.expand_dims(te_data, axis=3)


print('Dataset loaded')
#te_data2  = dataset_normalized(te_data)
te_data2 = te_data /255.

explainer = GradCAM()


dataaa = (te_data2[1].reshape(1,512,512,1),None)
grid = explainer.explain(dataaa, model, class_index=1)  

explainer.save(grid, ".", "grad_cam.png")

explainer = OcclusionSensitivity()

grid = explainer.explain(dataaa, model, class_index=1)  

explainer.save(grid, ".", "occ_cam.png")
