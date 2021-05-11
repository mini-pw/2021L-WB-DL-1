# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:15:43 2019

@author: Reza Azad
"""
from __future__ import division
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
import models as M
import numpy as np
from keras.callbacks import ModelCheckpoint, TensorBoard, ReduceLROnPlateau, CSVLogger, TerminateOnNaN
from PredictImage import PredictImage
from keras import callbacks
import pickle
import datetime
import tensorflow as tf

#tf.debugging.set_log_device_placement(True)

config = tf.compat.v1.ConfigProto(gpu_options =
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8),
#device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)

policy = tf.keras.mixed_precision.experimental.Policy('mixed_float16')
tf.keras.mixed_precision.experimental.set_policy(policy)

####################################  Load Data #####################################
folder = './processed_data/'
tr_data    = np.load(folder+'data_train.npy')
tr_mask    = np.load(folder+'Train_maska.npy')

te_data   = np.load(folder+'data_test.npy')
FOV       = np.load(folder+'FOV_te.npy')
#FOV        = np.load(folder+'FOV_tr.npy')
fov01 = FOV[0:2]
tr_data    = np.expand_dims(tr_data, axis=3)
tr_mask    = np.expand_dims(tr_mask, axis=3)

tr_pixels = np.load(folder+'Train_pixels.npy').reshape(-1, 1)

print('Dataset loaded')

te_data2 = te_data /255.
#tr_data   = tr_data /255.
tr_data   = tr_data /255.
tr_mask = tr_mask
tr_pixels = tr_pixels
tr_pixels = np.divide(tr_pixels, max(tr_pixels))

print('dataset Normalized')

# Build model
#model = M.BCDU_net_D3(input_size = (512,512,1))
#model = M.BCDU_net_PD3(input_size = (512,512,1))
model = M.BCDU_net_PD5(input_size = (512,512,1))

model.summary()

print('Training')
batch_size = 1
#nb_epoch   = 50
nb_epoch   = 38

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
im_dir = "logs/images/"
csv_path = "logs/save/" + 'log_' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.csv'

mcp_save = ModelCheckpoint('weight_lung', save_best_only=True, monitor='val_loss', mode='min', save_weights_only=True)
reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=7, verbose=1, epsilon=1e-4, mode='min')

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0)

p_i_callback = PredictImage(te_data2[0:2], fov01, im_dir)

ton_callback = TerminateOnNaN()

if not os.path.isfile(csv_path):
    open(csv_path, 'a').close()

csv_log = CSVLogger(csv_path)

callbacks_list = [mcp_save, reduce_lr_loss, tensorboard_callback, p_i_callback, csv_log, ton_callback]

#callbacks_list = [mcp_save, reduce_lr_loss, tensorboard_callback, csv_log, ton_callback]


history = model.fit(tr_data,[tr_mask,tr_pixels],
              batch_size=batch_size,
              epochs=nb_epoch,
              shuffle=True,
              verbose=1,
              validation_split=0.2, callbacks=callbacks_list)
  
print('Trained model saved')
with open('hist_lung', 'wb') as file_pi:
        pickle.dump(history.history, file_pi)



