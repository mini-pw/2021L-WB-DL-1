import numpy as np

from keras.models import Sequential
from data import BalanceCovidDataset
from eval_keras_gen import Metrics
import os, argparse, pathlib, datetime
from Model import keras_model_build
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard


parser = argparse.ArgumentParser(description='COVID-Net Training Script')
parser.add_argument('--epochs', default=10, type=int, help='Number of epochs')
parser.add_argument('--lr', default=0.0002, type=float, help='Learning rate')
parser.add_argument('--bs', default=5, type=int, help='Batch size')
parser.add_argument('--loadweight', default=1, type=int, help='If 1 load model weight if zero no')
parser.add_argument('--weightspath', default='models/COVIDNet-CXR4-A', type=str, help='Path to output folder')
parser.add_argument('--metaname', default='model.meta', type=str, help='Name of ckpt meta file')
parser.add_argument('--ckptname', default='model-18540', type=str, help='Name of model ckpts')
parser.add_argument('--trainfile', default='labels/under.txt', type=str, help='Path to train file') #'labels/train_COVIDx7A_new.txt' #over bylo dla ostanich wykonan # moge chceic znowu tu miec labels/under.txt
parser.add_argument('--testfile', default='labels/test_COVIDx7A_new.txt', type=str, help='Path to test file')
parser.add_argument('--testfolder', default='data/test', type=str, help='Folder where test data is located')
parser.add_argument('--name', default='COVIDNet', type=str, help='Name of folder to store training checkpoints')
parser.add_argument('--datadir', default='data', type=str, help='Path to data folder')
parser.add_argument('--covid_weight', default=2., type=float, help='Class weighting for covid') #bylo 4 #a wzialem 2 do under over samplingu
parser.add_argument('--covid_percent', default=0.3, type=float, help='Percentage of covid samples in batch')
parser.add_argument('--input_size', default=224, type=int, help='Size of input (ex: if 480x480, --input_size 480)')
parser.add_argument('--top_percent', default=0.08, type=float, help='Percent top crop from top of image')
parser.add_argument('--in_tensorname', default='input_1:0', type=str, help='Name of input tensor to graph')
parser.add_argument('--out_tensorname', default='norm_dense_1/Softmax:0', type=str, help='Name of output tensor from graph')
parser.add_argument('--logit_tensorname', default='norm_dense_1/MatMul:0', type=str, help='Name of logit tensor for loss')
parser.add_argument('--label_tensorname', default='norm_dense_1_target:0', type=str, help='Name of label tensor for loss')
parser.add_argument('--weights_tensorname', default='norm_dense_1_sample_weights:0', type=str, help='Name of sample weights tensor for loss')

args = parser.parse_args()

# Parameters
learning_rate = args.lr
batch_size = args.bs
display_step = 1


generator_train = BalanceCovidDataset(data_dir=args.datadir,
                                csv_file=args.trainfile,
                                batch_size=batch_size,
                                input_shape=(args.input_size, args.input_size),
                                covid_percent=args.covid_percent,
                                class_weights=[1., 1., args.covid_weight],
                                top_percent=args.top_percent)

generator_test = BalanceCovidDataset(data_dir=args.datadir,
                                csv_file=args.testfile,
                                is_training = False,
                                batch_size=batch_size,
                                input_shape=(args.input_size, args.input_size),
                                covid_percent=args.covid_percent,
                                class_weights=[1., 1., 1],
                                top_percent=args.top_percent)



# loss_op = tf.compat.v1.reduce_mean(tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(
#     logits=pred_tensor, labels=labels_tensor) * sample_weights)
# optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate)
# train_op = optimizer.minimize(loss_op)


model = keras_model_build()

optimizer=tf.keras.optimizers.Adam(lr=learning_rate)

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['categorical_accuracy'])

#if args.loadweight == 1:
#  model.load_weights('models/model.h5') 

metrics = Metrics(generator_test, model)

logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard = TensorBoard(logdir, histogram_freq=1)

model.fit(x = generator_train,
                    epochs=args.epochs,
                    verbose=1,
                    callbacks=[tensorboard, metrics])

model.save('models/model_tensorbaord.h5')
