import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import models as M
import models_l1 as M1
import models_l2 as M2
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
import surface_distance as sd # https://github.com/deepmind/surface-distance
import eval_metrics

import tensorflow as tf

config = tf.compat.v1.ConfigProto(gpu_options=
                                  tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
                                  )
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)
####################################  Load Data #####################################
folder = './processed_data/'
te_data = np.load(folder + 'data_test.npy')
FOV = np.load(folder + 'FOV_te.npy')
te_mask = np.load(folder + 'mask_test.npy')

te_data = np.expand_dims(te_data, axis=3)

print('Dataset loaded')
# te_data2  = dataset_normalized(te_data)
te_data2 = te_data / 255.
#model = M2.BCDU_net_D3(input_size = (512,512,1))
model = M.BCDU_net_D3(input_size=(512, 512, 1))
model.summary()


model.load_weights('weight_lung')
predictions = model.predict(te_data2, batch_size=2, verbose=1)

# Post-processing
predictions = np.squeeze(predictions)
predictions = np.where(predictions > 0.5, 1, 0)
Estimated_lung = np.where((FOV - predictions) > 0.5, 1, 0)

# Performance checking

y_scores = Estimated_lung.reshape(Estimated_lung.shape[0] * Estimated_lung.shape[1] * Estimated_lung.shape[2], 1)
print(y_scores.shape)

y_true = te_mask.reshape(te_mask.shape[0] * te_mask.shape[1] * te_mask.shape[2], 1)

y_pred = np.where(y_scores > 0.8, 1, 0)
y_true = np.where(y_true > 0.5, 1, 0)

output_folder = 'output_initial/'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Surface Distance Metrics:
hausdorff_list = np.array([0 for i in range(predictions.shape[0])])
avg_surf_dist = np.array([np.array([0, 0]) for i in range(predictions.shape[0])])
for i in range(len(predictions)):
    surface_dist_dict = sd.compute_surface_distances(predictions[i].astype(bool), Estimated_lung[i].astype(bool),
                                                     [1, 1])
    hausdorff_list[i] = sd.compute_robust_hausdorff(surface_dist_dict, 1)
    tmp_avg = sd.compute_average_surface_distance(surface_dist_dict)
    avg_surf_dist[i, 0] = tmp_avg[0]
    avg_surf_dist[i, 1] = tmp_avg[1]

print("\nMean of Hausdorff distances: " + str(np.mean(hausdorff_list)))
print("\nMean of Average Surface Distances (Original to predicted): " + str(np.mean(avg_surf_dist[:, 0])))
print("\nMean of Average Surface Distances (Predicted to original): " + str(np.mean(avg_surf_dist[:, 1])))

# Area under the ROC curve
fpr, tpr, thresholds = roc_curve((y_true), y_pred)
AUC_ROC = roc_auc_score(y_true, y_pred)
print("\nArea under the ROC curve: " + str(AUC_ROC))
roc_curve = plt.figure()
plt.plot(fpr, tpr, '-', label='Area Under the Curve (AUC = %0.4f)' % AUC_ROC)
plt.title('ROC curve')
plt.xlabel("FPR (False Positive Rate)")
plt.ylabel("TPR (True Positive Rate)")
plt.legend(loc="lower right")
plt.savefig(output_folder + "ROC.png")

# Precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_true, y_pred)
precision = np.fliplr([precision])[0]
recall = np.fliplr([recall])[0]
AUC_prec_rec = np.trapz(precision, recall)
print("\nArea under Precision-Recall curve: " + str(AUC_prec_rec))
prec_rec_curve = plt.figure()
plt.plot(recall, precision, '-', label='Area Under the Curve (AUC = %0.4f)' % AUC_prec_rec)
plt.title('Precision - Recall curve')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.legend(loc="lower right")
plt.savefig(output_folder + "Precision_recall.png")

# Confusion matrix
print("\nConfusion matrix:  Custom threshold (for positive) of " + str(0.8))
cm = eval_metrics.confusion_matrix(y_pred, y_true)
accuracy = eval_metrics.accuracy(None, None, cm)
precision = eval_metrics.precision(None, None, cm)
recall = eval_metrics.recall(None, None, cm)
specificity = eval_metrics.specificity(None, None, cm)
dice_coefficient = eval_metrics.dice_coefficient(None, None, cm)
gini_coefficient = eval_metrics.gini_coefficient(y_pred, y_true)

# Jaccard similarity index
jaccard_index = jaccard_score(y_true, y_pred)
print("\nJaccard similarity score: " + str(jaccard_index))

# F1 score
F1_score = f1_score(y_true, y_pred, labels=None, average='binary', sample_weight=None)
print("\nF1 score (F-measure): " + str(F1_score))

# Save the results
file_perf = open(output_folder + 'performances.txt', 'w')
file_perf.write("Area under the ROC curve: " + str(AUC_ROC)
                + "\nArea under Precision-Recall curve: " + str(AUC_prec_rec)
                + "\nJaccard similarity score(IoU): " + str(jaccard_index)
                + "\nF1 score (F-measure): " + str(F1_score)
                + "\nDice coefficient:" + str(dice_coefficient)
                + "\nGini coefficient:" + str(gini_coefficient)
                + "\n\nConfusion matrix:"
                + str(cm)
                + "\nACCURACY(pixel accuracy): " + str(accuracy)
                + "\nSENSITIVITY: " + str(recall)
                + "\nSPECIFICITY: " + str(specificity)
                + "\nPRECISION: " + str(precision)
                + "\nMean of Hausdorff distances: " + str(np.mean(hausdorff_list))
                + "\nMean of Average Surface Distances: " + str(np.mean(avg_surf_dist))
                + "\nMax of Hausdorff distances: " + str(np.max(hausdorff_list))
                + "\nMax of Average Surface Distances: " + str(np.max(avg_surf_dist))
                )
file_perf.close()

# Sample results
fig, ax = plt.subplots(5, 3, figsize=[15, 15])
all_ind = [1, 100, 200, 253, 193]  # random samples
all_ind = np.array(all_ind)
for idx in range(5):
    ax[idx, 0].imshow(np.uint8(np.squeeze(te_data[all_ind[idx]])))
    ax[idx, 1].imshow(np.squeeze(te_mask[all_ind[idx]]), cmap='gray')
    ax[idx, 2].imshow(np.squeeze(Estimated_lung[all_ind[idx]]), cmap='gray')

plt.savefig(output_folder + 'sample_results.png')

# surface distances
fig, ax = plt.subplots(1, 3, figsize=[45, 15])
ax[0].hist(hausdorff_list)
ax[0].set_title('Histogram of Hausdorff distances')
ax[1].hist(avg_surf_dist[:, 0])
ax[1].set_title('Histogram of Average surface distances (Original to predicted)')
ax[2].hist(avg_surf_dist[:, 1])
ax[2].set_title('Histogram of Average surface distances (Predicted to original)')
plt.savefig(output_folder + 'surface_distances.png')
