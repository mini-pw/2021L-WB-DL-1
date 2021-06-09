Homework 06
===

## Scope of this homework

In this homework we will cover the following issues.

1. Usage of iNNvestigate
2. Usage of GradCAM




Usage of iNNvestigate
---

After many hours spent, finally we could run this framework. The training script with the requirements will be attached. It required lots of modifications in packages' versions in order to be able to compile model and simultaneously investigate it. Despite issues with running the framework, the second drawback is that the only model available for TensorFlow >2.0 at this moment is LRP (Layer-Wise Relevance Propagation). Basically, LRP attributes recursively to each neuron's input relevance proportional to its contribution of the neuron output.


Let's check on results of this XAI method. However, we need to remember the model is just a random classifier.

The scheme will be as follows: firstly will be chest x-ray photo provided, then the LRP analyzer output will be shown.

![](https://i.imgur.com/MDn23Lb.png)

![](https://i.imgur.com/BZ9xfKx.png)

![](https://i.imgur.com/VGV7niG.png)

![](https://i.imgur.com/SW4Esm4.png)

![](https://i.imgur.com/T08qxGn.png)

![](https://i.imgur.com/34LYRak.png)

#### Summary

Due to poor model performance, it is really hard to make any conclusions about LRP analyzer as one of the XAI methods and its application to chest X-Ray images. The only thing that can be deduced from previous outputs is the fact that this model is truly not trained properly



Usage of GradCAM
---

After modifying code found here https://gist.github.com/RaphaelMeudec/e9a805fa82880876f8d89766f0690b54 (GradCAM with TensorFlow 2)
we were able to use also a GradCAM. However, the results are disappointing. Badly scaled pallet of colors also doesn't help to notice any differences in any areas of the image.

![](https://i.imgur.com/EGHvuWs.png)


Conclusions are similar to the ones described for iNNvestigate.