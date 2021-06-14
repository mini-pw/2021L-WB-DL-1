from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, accuracy_score, recall_score
from tensorflow.python.keras.callbacks import Callback
import numpy as np
import tensorflow as tf
import os, argparse
import cv2

from data import process_image_file


class Metrics(Callback):

    def __init__(self, generator, model):
        self.model = model
        self.generator = generator

    def on_epoch_end(self, epoch, logs={}):
      gen_len = len(self.generator)
    
      y_test = []
      y_hat = []

      for i in range(gen_len):
        _ , y_batch, _ = next(self.generator)
        y_test.append(y_batch)
      
      y_test = np.array(y_test)
      n, m, _ = y_test.shape
      y_test = y_test.reshape(n*m, -1)
      y_test = np.argmax(y_test, axis = 1)
      y_hat = self.model.predict(self.generator, verbose = 1)
      y_hat = np.array(y_hat)
      y_hat_prob = y_hat
      y_hat = np.argmax(y_hat, axis = 1)
      
      matrix = confusion_matrix(y_test, y_hat)
      matrix = matrix.astype('float')
      print(matrix)
      print(f"Accuracy of model: {accuracy_score(y_test, y_hat)}")
      print(f"Built in methood\n {classification_report(y_test, y_hat)}")
      print(f"Roc_auc_score: {roc_auc_score(y_test, y_hat_prob, multi_class='ovr')}")
      return

