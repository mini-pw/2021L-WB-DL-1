import numpy as np


from data import BalanceCovidDataset
import os, argparse, pathlib
from keras_model import keras_model_build
import tensorflow as tf


parser = argparse.ArgumentParser(description='COVID-Net Training Script')
parser.add_argument('--epochs', default=10, type=int, help='Number of epochs')
parser.add_argument('--lr', default=0.0002, type=float, help='Learning rate')
parser.add_argument('--bs', default=4, type=int, help='Batch size')
parser.add_argument('--weightspath', default='models/COVIDNet-CXR4-A', type=str, help='Path to output folder')
parser.add_argument('--metaname', default='model.meta', type=str, help='Name of ckpt meta file')
parser.add_argument('--ckptname', default='model-18540', type=str, help='Name of model ckpts')
parser.add_argument('--trainfile', default='labels/under.txt', type=str, help='Path to train file') #'labels/train_COVIDx7A_new.txt' #over bylo dla ostanich wykonan # moge chceic znowu tu miec labels/under.txt
parser.add_argument('--testfile', default='labels/test_COVIDx7A_new.txt', type=str, help='Path to test file')
parser.add_argument('--testfolder', default='data/test', type=str, help='Folder where test data is located')
parser.add_argument('--name', default='COVIDNet', type=str, help='Name of folder to store training checkpoints')
parser.add_argument('--datadir', default='data', type=str, help='Path to data folder')
parser.add_argument('--covid_weight', default=4., type=float, help='Class weighting for covid') #bylo 4 #a wzialem 2 do under over samplingu
parser.add_argument('--covid_percent', default=0.3, type=float, help='Percentage of covid samples in batch')
parser.add_argument('--input_size', default=224, type=int, help='Size of input (ex: if 480x480, --input_size 480)')#zmiana na 224 z 480
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


generator_test = BalanceCovidDataset(data_dir=args.datadir,
                                csv_file=args.testfile,
                                is_training = False,
                                batch_size=1,
                                input_shape=(args.input_size, args.input_size),
                                covid_percent=args.covid_percent,
                                class_weights=[1., 1., 1.],
                                top_percent=args.top_percent)


model = keras_model_build()

optimizer=tf.keras.optimizers.Adam(lr=learning_rate)

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])# loss nie jest poprawiony i metryka jeszcze


model.load_weights("./checkpoints_douczany_2/model.20/")

## Odtąd jest logika XAI

import innvestigate
import innvestigate.utils
import matplotlib.pyplot as plt


model = innvestigate.utils.model_wo_softmax(model)
analyzer = innvestigate.create_analyzer("lrp.epsilon", model)

image, x, _ = next(generator_test)
x=image

plt.imshow(x[0])
plt.show()


a = analyzer.analyze(x)

a=a["input"][0]
a = a.sum(axis=np.argmax(np.asarray(a.shape) == 3))
a /= np.max(np.abs(a))


plt.imshow(a, cmap="seismic", clim=(-1,1))
plt.show()

print("End")