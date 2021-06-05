---
title: 'Homework 02'
disqus: hackmd
---

Homework 02
===



## Table of Contents

[TOC]

## Scope of this homework

In this homework, we will cover the following issues.

1. Modifying the model
2. Downsizing model architecture




Modifying the model
---


### The first try

We used the Keras model because we had access to its architecture. However, according to the author of this model, he may have created this model based on his assumptions. This means that this model is not equivalent to the COVIDNET original model. According to the author, his model achieves an accuracy of 100% during training and only 65% during testing. This is a rather poor result. Our baseline result after 10 episodes is even worse. The final result is not obvious because the metric is very wobbly. However, our goal was to see any improvement over these 10 epochs. Our first attempt was to add batch normalization, as we saw its absence in the Keras implementation. Frankly, this step gave us some positive feedback. The model seemed less overfitted. With a higher learning rate these results could have been even better. What was noticeable was a higher classification of the number of covid instances we care most about.

The snippet of code with batch normalization:

![](https://i.imgur.com/2yeYf2e.png)

Baseline results:

![](https://i.imgur.com/X010As5.png)

With batch normalization. Noticed that the accuracy is much lower and the number of epochs does not matter. The base model ended up with the score on the level of 74% whereas with batch normalization on 60% on the training

![](https://i.imgur.com/X7ZssMM.png)

Downsizing model architecture
---

#### Motivations

Working with this architecture has shown us that the model is probably heavily underfitted. Having considered this, it seems very reasonable to reduce the number of parameters.

We have decided to get rid off the very last group of PEPX modules. Architecture before and after the change is presented below.

Original:
![](https://i.imgur.com/O55R4La.png)

After cutting 4th group of PEPX modules:
![](https://i.imgur.com/fCuvMOd.png)


#### Change


Removal of those PEPX modules consisting of relatively large layers and the 4th convolution that is presented above them allowed for a noticeable reduction of the number of parameters. The difference is presented below by providing output of model.summary() method. 

At he beginning:
![](https://i.imgur.com/B2NWqFe.png)

After:
![](https://i.imgur.com/XhfioO3.png)

Very last layers of new model implementation:
![](https://i.imgur.com/TGnKvwD.png)



#### Results

Original result

After 20 epochs (weights loaded from additional 10 epochs not added to the counter):
![](https://i.imgur.com/RdABlJi.png)

After 30 epochs:
![](https://i.imgur.com/XqenmJE.png)


New results


After 27 epochs (here also 10 epochs need to be added):
![](https://i.imgur.com/4NbioTJ.png)

After 30 epochs:
![](https://i.imgur.com/NRCtJ7J.png)


#### Summary

Although average accuracy from all epochs was a bit higher for changed model the difference was too small to claim that this model is no longer random. Results vary around 33%. Accuracy on the training set - although a bit lower - is still comparable to achieved with original architecture.




We don't present 3rd change, because teams that had to create training script were excluded (as far as we remember). In our case, moving to Keras implementation resulted in a need to create a completely new script for model training and evaluation using generators.