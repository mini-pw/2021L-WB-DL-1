Homework 05
===


## Scope of this homework

In this homework we will cover the following issues.

1. Data augmentation (with GAN)
2. Applying l1 and l2 regularization
3. Applying dropout





---


## Data Augmentation (with GAN)

Generative Adversarial Network is a pair of two specific neural networks - generator and discriminator, which train each other by generating by the generator data similar to the original training set and assessing the quality of the generated sample by the discriminator. 

![](https://i.imgur.com/w1No5Kf.png)

In paper titled 'Detection of Coronavirus (COVID-19) Associated Pneumonia based on Generative Adversarial Networks and a Fine-Tuned Deep Transfer Learning Model using Chest X-ray Dataset' the authors provide an analysis of how the use of GAN in various neural networks in issues related to the processing of x-ray images of the lungs (including the diagnosis of COVID-19) increased the efficiency of classification.

Architecture of generator from article:
- 5 transposed  convolutional  layers
- 4  ReLU layers
- 4  batch  normalization  layers
- 1 Tanh layer

Architecture of discriminator from article:
- 5 convolutional  layers
- 4 leaky ReLU layers
- 3  batch  normalization  layers

The use of GAN by the authors of the article universally increased the efficiency of the models, primarily contributing to the reduction of the risk of overfitting.

The above approach has been tested on simpler, relatively small models, in the case of COVIDNet it is possible that there is no clearly identifiable improvement in classification efficiency. 

It was our initial approach, but in the course of developing solution compatible with COVID-Net architecture we decided to define generator and discriminator as follows:

Generator architecture:

![](https://i.imgur.com/Jm619le.png)

Discriminator architecture:

![](https://i.imgur.com/VHdBLCD.png)

Designed Generative Adversarial Network was complete and operational, however in face of the limited time and resources and extensive computational requirements our network did not succeed in providing any actual images beyond simple patterns in random noise.





Transfer learning (unsupervised pretraining)
---

#### AutoEncoder

We used the autoencoder to obtain the unsupervised learning. We decieded to use the CNN autoencoder. Here is presented the architecture:

![](https://i.imgur.com/Rwg0rlG.png)

The autoencoder was learning for one epoch getting the result of 0.004 with MSE metric. Then we sectioned off the bottleneck layer. Our plan was to used this encoder model and combined it with our COVIDNET model. However, such an approach is invalid in our model, because the encoder part reduced the dimension of the input for the original one, causing the negative max pooling. So such an approach would integrate too much into the architecture of our model. Nevertheless, we were not sure how we could do it differently, because the complexity of the COVIDNET makes it Sisyphean job to pretrain every layer of the model. 

