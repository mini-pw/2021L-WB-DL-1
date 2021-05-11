from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
import pickle
import tensorflow as tf
import numpy as np

from multi_output_model import MultiOutputModel

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)
# ===============================================================================

folder = '//content/drive/MyDrive/WarsztatyBadawcze/processed_data/'
tr_data = np.load(folder + 'data_train.npy')
tr_mask = np.load(folder + 'Train_maska.npy')
tr_data = np.expand_dims(tr_data, axis=3)
tr_mask = np.expand_dims(tr_mask, axis=3)
tr_labels = np.load(folder + 'train_labels.npy')
print('Dataset loaded')

tr_data = tr_data / 255.

print('dataset Normalized')
# Build model
model = MultiOutputModel().build(input_size=(512, 512, 1))

print('Training')
batch_size = 2 # było 2
nb_epoch = 2 # było 50


losses = {'segmentation_output': 'binary_crossentropy', 'classification_output': 'binary_crossentropy'}
lossWeigths = {'segmentation_output': 1, 'classification_output': 1}
model.compile(optimizer=Adam(lr=1e-4), loss=losses, metrics=['accuracy'], loss_weights=lossWeigths)


mcp_save = ModelCheckpoint('weight_lung_multi.h5', save_best_only=True, monitor='val_loss', mode='min')
reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=7, verbose=1, min_delta=1e-4, mode='min')
print('fitting')
history = model.fit(tr_data, y={'segmentation_output': tr_mask, 'classification_output': tr_labels},
                    batch_size=batch_size,
                    epochs=nb_epoch,
                    shuffle=True,
                    verbose=1,
                    validation_split=0.2, callbacks=[mcp_save, reduce_lr_loss])
print('after fitting')

model.save_weights("weights/wagi_multi.h5")

print('Trained model saved')
with open('hist_lung_multi', 'wb') as file_pi:
    pickle.dump(history.history, file_pi)