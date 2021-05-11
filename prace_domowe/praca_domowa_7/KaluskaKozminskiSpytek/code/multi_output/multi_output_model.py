from __future__ import division

from keras.layers import *

from keras.models import Model

from res_net import ResnetBuilder
from BDCU_model import BCDU_net_D3


class MultiOutputModel:
    @staticmethod
    def build_classification_branch(inputs):
        conv1 = Conv2D(64, (3, 3), padding='same', activation='relu')(inputs)
        conv1 = BatchNormalization()(conv1)
        conv1 = MaxPooling2D(pool_size=(3, 3))(conv1)
        conv1 = Dropout(0.25)(conv1)

        conv2 = Conv2D(64, (3, 3), padding='same', activation='relu')(conv1)
        conv2 = BatchNormalization()(conv2)
        conv2 = Dropout(0.25)(conv2)

        conv3 = Conv2D(64, (3, 3), padding='same', activation='relu')(conv2)
        conv3 = BatchNormalization()(conv3)
        conv3 = MaxPooling2D(pool_size=(2, 2))(conv3)
        conv3 = Dropout(0.25)(conv3)

        conv4 = Conv2D(64, (3, 3), padding='same', activation='relu')(conv3)
        conv4 = BatchNormalization()(conv4)
        conv4 = Dropout(0.25)(conv4)

        conv5 = Conv2D(64, (3, 3), padding='same', activation='relu')(conv4)
        conv5 = BatchNormalization()(conv5)
        conv5 = MaxPooling2D(pool_size=(2, 2))(conv5)
        conv5 = Dropout(0.25)(conv5)

        flat = Flatten()(conv5)
        dense = Dense(256, activation='relu')(flat)
        dense = BatchNormalization()(dense)
        dense = Dropout(0.5)(dense)
        dense2 = Dense(1)(dense)

        return Activation('sigmoid', name="classification_output")(dense2)

    @staticmethod
    def build_segmentation_branch(inputs):
        return BCDU_net_D3(inputs)

    @staticmethod
    def build(input_size):
        inputs = Input(shape=input_size)
        classification_branch = ResnetBuilder.build_resnet_50(inputs)
        segmentation_branch = MultiOutputModel.build_segmentation_branch(inputs)

        model = Model(inputs=inputs,
                      outputs=[classification_branch, segmentation_branch],
                      name='dual_net')
        return model
