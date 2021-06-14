from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, accuracy_score, recall_score

import numpy as np
import pandas as pd
import tensorflow as tf
import os, argparse
import cv2

from data import process_image_file
from tensorboard_images import plot_projector

mapping = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}


def eval(sess, graph, testfile, testfolder, input_tensor, output_tensor, input_size):
    image_tensor = graph.get_tensor_by_name(input_tensor)
    pred_tensor = graph.get_tensor_by_name(output_tensor)

    y_test = []
    pred = []

    normal = []
    pneumonia = []
    covid = []

    

    """I ADD MY COD"""
    pred1 = []
    """END OF MY CODE"""

    for i in range(len(testfile)):
        line = testfile[i].split()
        x = process_image_file(os.path.join(testfolder, line[1]), 0.08, input_size)
        x = x.astype('float32') / 255.0
        y_test.append(mapping[line[2]])
        res = np.array(sess.run(pred_tensor, feed_dict={image_tensor: np.expand_dims(x, axis=0)})).argmax(axis=1)
        if res == 0:
          normal.append(line)
        elif res == 1:
          pneumonia.append(line)
        else:
          covid.append(line)
        pred.append(np.array(res))
        #"""I ADD MY COD"""
        # get the probability of each class
        #pred1.append(np.array(sess.run(pred_tensor, feed_dict={image_tensor: np.expand_dims(x, axis=0)})))
        #"""END OF MY CODE"""
    pred = np.array(pred)
    y_test = np.array(y_test)

    normal = pd.DataFrame(np.matrix(normal))
    pneumonia = pd.DataFrame(np.matrix(pneumonia))
    covid = pd.DataFrame(np.matrix(covid))
    normal.to_csv("normal.txt", sep = " ", columns = None, header = False, index = False)
    pneumonia.to_csv("pneunomia.txt", sep = " ", columns = None, header = False, index = False)
    covid.to_csv("covid.txt", sep = " ", columns = None, header = False, index = False)
    #pred = np.array(pred)

    #"""I ADD MY COD"""
    #pred1 = np.array(pred1).reshape(-1, 3)
    #"""END OF MY CODE"""

    matrix = confusion_matrix(y_test, pred)
    matrix = matrix.astype('float')
    #cm_norm = matrix / matrix.sum(axis=1)[:, np.newaxis]
    print(matrix)
    #class_acc = np.array(cm_norm.diagonal())

    #""" I ADD MY CODE """

    #print(f"Accuracy of model: {accuracy_score(y_test, pred)}")

    #class_spec = [(np.sum(matrix) - np.sum(matrix[i, :]) - np.sum(matrix[:, i]) + matrix[i, i]) / (
    #            np.sum(matrix) - np.sum(matrix[i, :])) if np.sum(matrix[i, :]) else 0 for i in range(len(matrix))]

    #print('Spec Normal: {0:.3f}, Pneumonia: {1:.3f}, COVID-19: {2:.3f}'.format(class_spec[0],
    #                                                                           class_spec[1],
    #                                                                           class_spec[2]))

    print(f"Built in methood\n {classification_report(y_test, pred)}")

    #print(f"Roc_auc_score: {roc_auc_score(y_test, pred1, multi_class='ovr')}")

    #print(pred1[:10])

    #"""END OF MY CODE"""

    # changed class_acc na class_sens
    #class_sens = [matrix[i,i]/np.sum(matrix[i,:]) if np.sum(matrix[i,:]) else 0 for i in range(len(matrix))]
    #print('Sens Normal: {0:.3f}, Pneumonia: {1:.3f}, COVID-19: {2:.3f}'.format(class_sens[0],
    #                                                                           class_sens[1],
    #                                                                           class_sens[2]))
    #ppvs = [matrix[i,i]/np.sum(matrix[:,i]) if np.sum(matrix[:,i]) else 0 for i in range(len(matrix))]
    #print('PPV Normal: {0:.3f}, Pneumonia {1:.3f}, COVID-19: {2:.3f}'.format(ppvs[0],
    #                                                                         ppvs[1],
    #                                                                         ppvs[2]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='COVID-Net Evaluation')
    parser.add_argument('--weightspath', default='models/COVIDNet-CXR4-A', type=str, help='Path to output folder')
    parser.add_argument('--metaname', default='model.meta', type=str, help='Name of ckpt meta file')
    parser.add_argument('--ckptname', default='model-18540', type=str, help='Name of model ckpts')
    parser.add_argument('--testfile', default='test_COVIDx5.txt', type=str, help='Name of testfile')
    parser.add_argument('--testfolder', default='data/test', type=str, help='Folder where test data is located')
    parser.add_argument('--in_tensorname', default='input_1:0', type=str, help='Name of input tensor to graph')
    parser.add_argument('--out_tensorname', default='norm_dense_1/Softmax:0', type=str, help='Name of output tensor from graph')
    parser.add_argument('--input_size', default=480, type=int, help='Size of input (ex: if 480x480, --input_size 480)')

    args = parser.parse_args()

    sess = tf.Session()
    tf.get_default_graph()
    saver = tf.train.import_meta_graph(os.path.join(args.weightspath, args.metaname))
    saver.restore(sess, os.path.join(args.weightspath, args.ckptname))

    graph = tf.get_default_graph()

    file = open(args.testfile, 'r')
    testfile = file.readlines()

    eval(sess, graph, testfile, args.testfolder, args.in_tensorname, args.out_tensorname, args.input_size)
