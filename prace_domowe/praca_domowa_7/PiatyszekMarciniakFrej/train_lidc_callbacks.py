'''
This is a part of the supplementary material uploaded along with 
the manuscript:
    "Semantic Segmentation of Pathological Lung Tissue with Dilated Fully Convolutional Networks"
    M. Anthimopoulos, S. Christodoulidis, L. Ebner, A. Christe and S. Mougiakakou
    IEEE Journal of Biomedical and Health infomatics (2018)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For more information please read the README file. The files can also 
be found at: https://github.com/intact-project/LungNet
'''
import os
import sys
import glob
import uuid
import numpy as np
import LungNet as LN
from keras.utils import plot_model
from keras.callbacks import ModelCheckpoint, EarlyStopping, CSVLogger, TerminateOnNaN, LearningRateScheduler, Callback
from tensorflow.python.keras.utils import tf_utils
import tensorflow as tf
import datetime

# debug
from ipdb import set_trace as bp

class CustomTerminateOnNaN(Callback):
  def __init__(self):
    super(CustomTerminateOnNaN, self).__init__()
    self._supports_tf_logs = True

  def on_batch_end(self, batch, logs=None):
    logs = logs or {}
    loss = logs.get('loss')
    if loss is not None:
      loss = tf_utils.to_numpy_or_python_type(loss)
      if np.isnan(loss) or np.isinf(loss):
        print('Batch %d: Invalid loss, terminating training' % (batch))
        sys.exit(1)

if __name__ == '__main__':

    class_weights = [1516.560586059309, 1.0006598220781007]

    # get model
    model = LN.get_model(2, class_weights, unsuper_weight=0)
    print(model.outputs)
    
    # save model image
    modeldir = 'model-'+str(uuid.uuid4())
    print(modeldir)
    log_dir = 'tensorboard/' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    print(log_dir)
    if not os.path.exists(modeldir):
        os.makedirs(modeldir)
        os.makedirs(log_dir)
    open(modeldir+'/architecture.json', 'w').write(model.to_json())
    plot_model(model, to_file=modeldir+'/model.png', show_shapes=True)

    train_gen = LN.sample_generator('lidc-equalized-train.npz')
    val_gen = LN.sample_generator('lidc-equalized-val.npz', augment=False)

    # Callbacks
    checkpoints = ModelCheckpoint(modeldir+'/weights.{epoch:02d}-{val_waccOA:.2f}.hdf5', monitor='val_waccOA', verbose=1, mode='max', save_best_only=True)
    earlystopping = EarlyStopping(monitor='val_waccOA', min_delta=0.001, patience=25, verbose=1, mode='max')
    logger = CSVLogger(modeldir+'/training.log')
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
    terminate_on_nan = CustomTerminateOnNaN()
    def schedule_lr(epoch, lr):
        return lr * 1
    lr_scheduler = LearningRateScheduler(schedule_lr)

    # fit model
    model.fit_generator(train_gen, 800, 1000, validation_data=val_gen, validation_steps=200,
                        callbacks=[checkpoints, earlystopping, logger, tensorboard_callback, terminate_on_nan, lr_scheduler])