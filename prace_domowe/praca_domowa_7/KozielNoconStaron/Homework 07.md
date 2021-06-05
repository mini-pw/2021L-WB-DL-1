---
title: 'Homework 07'
disqus: hackmd
---

Homework 07
===


## Scope of this homework

In this homework we will cover the following issues.

1. TensorBoard
2. Multiple outputs/inputs
3. Ensemble of models




TensorBoard
---


### TensorBoard

We used tensorBoard to visualize some statistics and the dataset. Starting with the first one we showed on the plots the increase in the accuracy of the model on the training set after 20 epochs and the decrease of the loss

![](https://i.imgur.com/COeQkhr.png)

This tool has given us a handful of opportunities to test some behavior of our model. We could also smoothen the curve if we wanted to see better results. Furthermore, we had an access to the distribution of the values of the weight matrixes (kernel) and the bias after each iteration. Here is an example for the PEPX layer

![](https://i.imgur.com/cklxwxZ.png)

Also to show the complexity of the model we could display the graph of it. The TensorBoard gave us such a possibility:

![](https://i.imgur.com/KEjsiqg.png)

We now move on to review the dataset. To our surprise, TensorBoard performed very well. We were able to use the PCA and T-SNE algorithm to see the dataset in the 3D world. It also gave us some information about the similarities of the individual samples, as both are clustering methods. Here we display the screen of that experiment:

![](https://i.imgur.com/V70Olvx.png)


Multiple inputs/outputs
---

For this exercise, we decided to modify COVID-Net architecture so it would accept multiple different types of input training data, particularly numerical and encoded categorical data apart from images.


![](https://i.imgur.com/wp4hCmw.png)

We decided that additional data will be represented as a vector and processed by new branch added to COVID-Net consisting of two Dense layers, implemented in Keras.

![](https://i.imgur.com/5itfxCK.png)

The most prominent problem with this modification are imperfections of the dataset. Metadata regarding x-ray images utilized during training are scarce at best, and above all incomplete beyond imputation.

The richest set of metadata is covid-chestxray-dataset, from which after encoding categorical values we extracted additional data describing the patient's age, sex and information about intubation.

However, the amount of data was still far too limited to perform complex analysis of the performance of this modified model in relation to original COVID-Net.



## Ensemble of models

It is common to observe an ensemble of models to perform significantly better than the single model on the given task, especially in the image recognition field. For this exercise, we devised a simple stacking ensemble.

![](https://i.imgur.com/dAeSeKS.png)

It was composed of two models - COVID-Net and ConvPool-CNN-C and trained to combine the predictions of both of the models, which in this case was simply averaging outputs, which in problem of classification on images is acceptable approach.

However, just as in previous exercises we cannot determine how effective is this approach in terms of enhancing initial COVID-Net performance.

What we can observe and what can provide even remote insight in the hypothetical performance of proposed ensemble is "side-by-side" performance of both models individually after one epoch on subset of data with over 1500 samples:

COVID-Net:
![](https://i.imgur.com/y6verJS.png)

ConvPool-CNN-C:
![](https://i.imgur.com/y6verJS.png)

Unfortunately, both models of an ensemble trained during this experiment simply classified all samples into one category, which isn't a base for any further conclusions.
