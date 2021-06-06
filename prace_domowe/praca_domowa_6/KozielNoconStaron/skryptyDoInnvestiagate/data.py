import tensorflow as tf
from tensorflow import keras

import numpy as np
import os
import cv2

from tensorflow.keras.preprocessing.image import ImageDataGenerator



"""
crop_top takes as an input img which is an array of shape (x, y, 3) and 
percentage of picture to crop
"""
def crop_top(img, percent=0.15):
    offset = int(img.shape[0] * percent) #cut the top portion of image
    return img[offset:] # return image

"""
central_crop takes as an input img which is an array of shape (x, y, 3)
"""
def central_crop(img):
    size = min(img.shape[0], img.shape[1]) # min of x and y
    offset_h = int((img.shape[0] - size) / 2) # horizontal len
    offset_w = int((img.shape[1] - size) / 2) # vertical
    return img[offset_h:offset_h + size, offset_w:offset_w + size] # makes square image and centered

"""
process_image_file take as an input path of the photo for example data/train/1-s2.0-S0929664620300449-gr2_lrg-a.jpg, 
top_percante for e.g top_percante = 0.08, and size of on axis of the image. In our case it will be 480
"""
def process_image_file(filepath, top_percent, size):
    img = cv2.imread(filepath) # load image as array of shape (x, y , 3)
    img = crop_top(img, percent=top_percent) # use function define above
    img = central_crop(img) # use function define above
    img = cv2.resize(img, (size, size)) # resize image from (min(x, y), min(x,y)) to (480,480). noticed that it remains
                                        # of the shape with 3 chanels (480,480,3)
    return img

"""
random_ratio_resize takes as an input image path, prob ,the probability of rotation if the random value is bigger than
prob do nothing and delta set as default to 0.1. As this function is used in code after central_crop which squares the image
ration will be 1. So we take then random value between segmet form [1-dleta, 1+ dleta]  
"""

def random_ratio_resize(img, prob=0.3, delta=0.1):
    if np.random.rand() >= prob: # bigger do nothing
        return img
    ratio = img.shape[0] / img.shape[1] # in our case 1
    ratio = np.random.uniform(max(ratio - delta, 0.01), ratio + delta) # random value form [1-delta, 1+delta]. if delta
                                                                        # change we prevent from left end of segment being non positve
    if ratio * img.shape[1] <= img.shape[1]:
        size = (int(img.shape[1] * ratio), img.shape[1]) # e.g shape of (474, 480) after this operation
    else:
        size = (img.shape[0], int(img.shape[0] / ratio)) #e.g shape of (480, 472) after this operation

    dh = img.shape[0] - size[1] # could be zero or (480 - less number than 480)
    top, bot = dh // 2, dh - dh // 2 # could be zeros ot the sum up to dh e.g dh = 9 then top = 4, bot = 5
    dw = img.shape[1] - size[0] # similar to above
    left, right = dw // 2, dw - dw // 2

    if size[0] > 224 or size[1] > 224: #should not happen casue one of the coordinates should always be 480
        print(img.shape, size, ratio)

    img = cv2.resize(img, size) # resize image
    img = cv2.copyMakeBorder(img, top, bot, left, right, cv2.BORDER_CONSTANT,
                             (0, 0, 0)) # this function makes image back to shape of (480, 480, 3) however it add black famre
                                        # around the image

    ##moja mizna tutaj teraz na 224
    if img.shape[0] != 224 or img.shape[1] != 224: # should have happned since the ouput shape after copyMakeBorder supposed to be
                                                    # (480,480, 3)
        raise ValueError(img.shape, size) # in case of error raise exception
    return img

_augmentation_transform = ImageDataGenerator(
    featurewise_center=False,            # Boolean. Set input mean to 0 over the dataset, feature-wise.
    featurewise_std_normalization=False, # Boolean. Divide inputs by std of the dataset, feature-wise.
    rotation_range=10,                   # Int. Degree range for random rotations.
    width_shift_range=0.1,               # Float, 1-D array-like or int
                                            # float: fraction of total width, if < 1, or pixels if >= 1.
                                            # 1-D array-like: random elements from the array.
                                            # int: integer number of pixels from interval (-width_shift_range, +width_shift_range)
                                            # With width_shift_range=2 possible values are integers [-1, 0, +1], same as
                                                # with width_shift_range=[-1, 0, +1], while with width_shift_range=1.0 possible values are
                                                # floats in the interval [-1.0, +1.0).
    height_shift_range=0.1,             # Float, 1-D array-like or int
                                            # float: fraction of total height, if < 1, or pixels if >= 1.
                                            # 1-D array-like: random elements from the array.
                                            # int: integer number of pixels from interval (-height_shift_range, +height_shift_range)
                                            #With height_shift_range=2 possible values are integers [-1, 0, +1], same as
                                                # with height_shift_range=[-1, 0, +1], while with height_shift_range=1.0 possible values are
                                                # floats in the interval [-1.0, +1.0).
    horizontal_flip=True,               # Boolean. Randomly flip inputs horizontally.
    brightness_range=(0.9, 1.1),        # Tuple or list of two floats. Range for picking a brightness shift value from.
    zoom_range=(0.85, 1.15),            # Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range].
    fill_mode='constant',               # One of {"constant", "nearest", "reflect" or "wrap"}. Default is 'nearest'. Points outside
                                        # the boundaries of the input are filled according to the given mode:
                                            #'constant': kkkkkkkk|abcd|kkkkkkkk (cval=k)
                                            #'nearest': aaaaaaaa|abcd|dddddddd
                                            #'reflect': abcddcba|abcd|dcbaabcd
                                            #'wrap': abcdabcd|abcd|abcdabcd
    cval=0.,                            # Float or Int. Value used for points outside the boundaries when fill_mode = "constant".
)

"""
apply_augmentation takes as input img which is an array of shape (x, y, 3)
"""
def apply_augmentation(img):
    img = random_ratio_resize(img) #defina above
    img = _augmentation_transform.random_transform(img) # Applies a random transformation to an image.
    return img

"""
_process_csv_file take as an input a file in our case these are train_split.txt and test_split.txt (names may differ)
"""

def _process_csv_file(file):
    with open(file, 'r') as fr: # open file
        files = fr.readlines() # read lines
    return files


class BalanceCovidDataset(keras.utils.Sequence):
    'Generates data for Keras'

    def __init__(
            self,
            data_dir,
            csv_file,
            is_training=True,
            batch_size=8,
            input_shape=(224, 224), # here default shape is (224, 224) becasue these values were for former models,
                                    # In another file we set it for (480, 480)
            n_classes=3, # normal, pneunomia, COVID-19
            num_channels=3, # depth of image. Although the images are grey we keep this chanel (with possibility to delete this)
            mapping={
                'normal': 0,
                'pneumonia': 1,
                'COVID-19': 2
            },
            shuffle=True,
            augmentation=apply_augmentation,
            covid_percent=0.3,
            class_weights=[1., 1., 6.], # default weight of classes. The less numbered class gets is more worthy than the others
                                        # in this case COVID_19
            top_percent=0.08 # here set to 0.08, though in above functions was set to 0.15
    ):
        'Initialization' # seeting values in constructor
        self.datadir = data_dir
        self.dataset = _process_csv_file(csv_file)
        self.is_training = is_training
        self.batch_size = batch_size
        self.N = len(self.dataset)
        self.input_shape = input_shape
        self.n_classes = n_classes
        self.num_channels = num_channels
        self.mapping = mapping
        self.shuffle = True
        self.covid_percent = covid_percent
        self.class_weights = class_weights
        self.n = 0
        self.augmentation = augmentation
        self.top_percent = top_percent

        datasets = {'normal': [], 'pneumonia': [], 'COVID-19': []} #dictionary for classes
        for l in self.dataset: # iterate for dataset
            datasets[l.split()[2]].append(l) # the second argument describes the name of the class e.g l.split()[2] - normal
                                            # append the whole line to dictionary.
        self.datasets = [
            datasets['normal'] + datasets['pneumonia'],
            datasets['COVID-19'],
        ] # set dataset to list of list where the first one is the conctaenation of lists 'normal' and 'pneumonia', and the
         # second one is COVID_19
        print(len(self.datasets[0]), len(self.datasets[1]))

        self.on_epoch_end() # is triggered once at the very beginning as well as at the end of each epoch.
                            # If the shuffle parameter is set to True, we will get a new order of exploration at
                            # each pass (or just keep a linear exploration scheme otherwise).

    def __next__(self): # mothod that need to be implement, keras generator
        # Get one batch of data
        batch_x, batch_y, weights = self.__getitem__(self.n) # if the numer of batch is less than number of batches we call the
                                                            # __getitem__ methdd
        # Batch index
        self.n += 1

        # If we have processed the entire dataset then
        if self.n >= self.__len__(): # it means that we fed all of our training exmaples in this epoch
            self.on_epoch_end() # schuffle traing set
            self.n = 0 # set to zero

        return batch_x, batch_y, weights

    def __len__(self):
        return int(np.ceil(len(self.datasets[0]) / float(self.batch_size))) # returns the numer of batches that we will have

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        if self.shuffle == True:
            for v in self.datasets:
                np.random.shuffle(v) #shuffle afetr each epoch. This is done becouse we want our model to generalzie as much as we can
                                    # it shuffles the concatenated list of normal and pneunomia, and shuffles the COVID_19 list

    def __getitem__(self, idx):
        batch_x, batch_y = np.zeros(
            (self.batch_size, *self.input_shape,
             self.num_channels)), np.zeros(self.batch_size) # batch_x has a shape of (8, 480, 480. 3) and batch_y = (8), the * is used beacuse
                                                            # the input_shape is a tuple which len don't have to be 2 (in our case yes, but the python
                                                            # languages requries this)

        batch_files = self.datasets[0][idx * self.batch_size:(idx + 1) *
                                       self.batch_size]  # we take a batch_size of training examples from concatenated list of normal and pneunomia
                                                         # len of batch files is equal to batch_size = 8

        # upsample covid cases
        covid_size = max(int(len(batch_files) * self.covid_percent), 1) # we would like to have at lest 1 exmaple of COVID-19 in our batch_size
                                                                        # setting the proper value of covid_percent gives us more. In case of
                                                                        # covid_percent = 0.3 and batch_size = 8, it returns int(2.4) = 2
        covid_inds = np.random.choice(np.arange(len(batch_files)), # chose covid_size (2) random indexes from range 0 to batch_files - 1.
                                      size=covid_size,
                                      replace=False)
        covid_files = np.random.choice(self.datasets[1], # chose random COVID_19 examples (in our case 2) from list of COVID_19 records
                                       size=covid_size,
                                       replace=False)
        for i in range(covid_size):
            batch_files[covid_inds[i]] = covid_files[i] # change chosen examples with those COVID-19 ones. Noticed that in case of batch_size = 8
                                                        # we have 2 COVID-19 exmaples but the rest 6 is in unkown ratio. eg it could be 6:0, 1:5 etc

        for i in range(len(batch_files)):
            sample = batch_files[i].split() # take sample form batch

            if self.is_training: # if is_training = true this i an training sample. We do not make augmentation for test set
                folder = 'train'
            else:
                folder = 'test'

            x = process_image_file(os.path.join(self.datadir, folder, sample[1]), # preprocess an image
                                   self.top_percent,
                                   self.input_shape[0])

            if self.is_training and hasattr(self, 'augmentation'): # if traing sample we do augmentation
                x = self.augmentation(x)

            x = x.astype('float32') / 255.0 # we normalized the values to be [0,1] the format is png and jpeg not dicom
            y = self.mapping[sample[2]] # label sample second argument in sample is class name

            batch_x[i] = x # bulid X batch
            batch_y[i] = y # build y batch

        class_weights = self.class_weights # use class weight to denote its importance
        weights = np.take(class_weights, batch_y.astype('int64')) # e.g we have a y batch of np.array([2, 2, 0, 1, 0, 0, 1, 0]) and
                                                                  # class_weights = [1,1,6] we get for each sample te result of
                                                                  # array([6, 6, 1, 1, 1, 1, 1, 1])

        return batch_x, keras.utils.to_categorical(batch_y, num_classes=self.n_classes), weights # to categorcial makes one_hot_encding in our case
    """
    Worthy note: The class ImageDataGenerertor wroks like this. We feed it e.g with 8 samples of our training set(batch). Then we use our define
    transofrmation. As a result we get new 8 samples of that have never been seen by our model. We feed it with this not with the orgnial 8 examples.
    The motivation behind this is to genelrize the model. In each epoch we feed model with difent batches with slitly chanhes to images caused by our
    trasformations.
    """

