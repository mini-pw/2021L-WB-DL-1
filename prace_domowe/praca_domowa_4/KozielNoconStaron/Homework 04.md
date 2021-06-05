Homework 04
===

## Scope of this homework

In this homework we will cover the following issues.

1. Various metrices
2. Applying l1 and l2 regularization
3. Applying dropout




Various metrices
---


### Various metrices

Besides the metrics used in the original script, we added the extra ones. First of all we took advantage of the built-in method in the sci-kit learn library. There we have metrics such as precision, recall, different types of accuracy and the most interesting one - the f1-score. Since we deal with medical task, that type of score is the most important one. Moreover, we have ROC_AUC score which also defines in a good manner how well our model is predicting.

Here is the snippet of code with some results:
![](https://i.imgur.com/L63naXG.png)

![](https://i.imgur.com/YJqVwN6.png)






Applying L2 norm
---

#### Results achieved with original architecture.

The following metrices and confusion matrix was achieved by training for 30 epochs on undersampled dataset. 


![](https://i.imgur.com/3oPg23v.png)

We can see a bit poor sensitivity for Normal class, this issue could be also observed in previous epochs with other metrices being fairly stable. 



#### L2 regularization


L2 norm was applied to the TensorFlow graph provided by COVID-Net team. This is motivated due to the fact that results achieved using this model were far more satisfying. Whole process was performed by adding regularization to each trainable parameter separately. Chunk of code used is provided below.

![](https://i.imgur.com/Ff593Pn.png)

We did not want to include "bias" parameter in the regularization. 

Let's take a look at the output and the process of learning and compare it with the original results.

Although it says that epochs are from 1 to 20 in fact the interval is from 11 to 30 with starting weights restored after 10 epochs of training.

![](https://i.imgur.com/j7AxtbA.png)


![](https://i.imgur.com/Q3fA5XK.png)

We can observe poor performance after applying l2 regularization. This method caused our model to be unable to recognize any class of images. Our classifier became completely random with no promises of improvement.

#### L1 regularization

L1 regularization is the second method used to influence the performance of our model. 

The following code presents the implementation.

![](https://i.imgur.com/j38j6PW.png)

Achieved results were similar to the ones after L2 regularization. Model used only one label to classify all cases what induces complete randomness of the network.

#### Summary

Applying l1 or l2 regularization has provided significantly worse results than without any type of regularization. It was rather easy to predict. COVID-Net network is big and we suffer from underfitting, not overfitting, thus adding regularization only could worsen overall performance. Further manipulations with alpha parameter and setting it to negligible values allowed model to learn again with an effect similar to starting results (achieved without regularization) with no noticeable difference.


## Dropout

This method in contrast to the previous was applied to the model architecture implemented in Keras because it was much easier to perform. However, there is an issue with this model, which will be covered in detail in other homework or article. It is completely random. Even the author of this architecture achieved only 65% accuracy on (overfitted) model after 100 epochs and the dataset a bit different from ours. Restoring these weights is time-consuming and any network modifications cannot be later compared if this process will have to be repeated. Also, this accuracy is nothing in comparison to the results presented in COVID-Net article.

Being familiar with the circumstances we can move to the dropout method implementation.

![](https://i.imgur.com/06NowEt.png)

Dropout with the rate set to 0.3 was applied to two out of three dense layers.


Results with no dropout:

![](https://i.imgur.com/yihdbjW.png)

Results with dropout:

![](https://i.imgur.com/mAiurcY.png)

As we can see in both cases the network acts just as a random classifier, therefore it is hard to come up with any reasonable conclusions. However, we are able to compare results on training dataset. We can observe increased value of loss function and accuracy falling from 70% to 60%. This provides us with arguments to state that this method of regularization is also going to have negative influence on model performance.
