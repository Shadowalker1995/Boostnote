# Algorithms for Image Comparison

## 1. Overview

In this tutorial, **we’ll present some algorithms for image comparison.** First, we’ll make an overview of the problem and then we’ll introduce three algorithms from the simplest to the most complex.

## 2. Problem Description

In image comparison, **we have two input images $I_A$ and $I_B$ and our goal is to measure their similarity $S(I_A, I_B).$ **First, we have to realize that the concept of similarity is not strictly defined and can be interpreted in many ways. Specifically, two images $I_A$ and $I_B$ can be considered **similar if:**

- **they differ only in terms of contrast, brightness and rotation**
- **they are semantically identical, meaning that they depict the same objects**

Below, we can see different interpretations of image similarity. The left image is a rotated version of the original image with a distinct contrast, while the right image depicts the same dog but in a different background:

<img src="Algorithms%20for%20Image%20Comparison.assets/similarity.webp" alt="similarity" style="zoom: 50%;" />

We realize that it is much easier to implement an image comparison system for the left case since the dog’s pose and background surface remain the same.

**In this tutorial, we’ll present algorithms that compare images based on the content starting from the simplest to the most complex.**

## 3. Naive Approach

A naive approach would be to use a metric that takes as input the raw pixels of the images and outputs their similarity. **We can use the classical Mean Squared Error in this case to compute the mean value of the square of the differences between the pixels of the two images:**
$$
\text{MSE}(I_A, I_B) = \frac{1}{mn}\sum_{i=0}^{m-1}\sum_{j=0}^{n-1}|I_A(i,j) - I_B(i,j)|^2
$$
We can assume that the lower the value of MSE, the higher the similarity. Despite its speed and simplicity, this method comes with many problems. **Large [Euclidean](https://www.baeldung.com/cs/euclidean-distance-vs-cosine-similarity) distance between pixel intensities does not necessarily mean that the image’s content is different.**

As we can see below, if we just change the contrast of the image, the final MSE value will increase a lot, although we did not change the content:

<img src="Algorithms%20for%20Image%20Comparison.assets/mse-1024x502.webp" alt="mse-1024x502" style="zoom:50%;" />

## 4. Image Matching

Pixel-based methods like MSE are not effective when the input images are taken under different angles or lighting conditions. To deal with these cases, image matching is the appropriate method.

**The first step in image matching is to detect some points in the input images** that contain rich visual information. These points usually correspond to the edges and the corners of the objects in the image. The most well-known key point detectors are [Harris corner detector](https://en.wikipedia.org/wiki/Harris_corner_detector), [SIFT](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) and [SURF](https://en.wikipedia.org/wiki/Speeded_up_robust_features).

Below, we can see an example of applying a key point detector to the previous images. The detected key points are shown in purple:

<img src="Algorithms%20for%20Image%20Comparison.assets/points.webp" alt="points" style="zoom:50%;" />

We observe that the key points are located in the region of the eyes, the ears, the mouth and the legs of the dog.

**Our next step is to compute a local descriptor for each detected key point. A local descriptor is defined by a 1-dimensional vector that describes the visual appearance of the point.** As a result, points from the same parts of the object will have similar vectors. The aforementioned [SIFT](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) and [SURF](https://en.wikipedia.org/wiki/Speeded_up_robust_features) methods are able to compute the local descriptors after detecting the key points.

**The final step is to match the descriptors of the two images.** To do this, we iteratively compare the descriptors of the images to discover pairs of descriptors that are similar. If the amount of similar descriptors is above a certain threshold, then it means that the two images depict the same object and are considered similar.

Below, we have matched the points located in the left ear and the front right leg of the dog in the two images:

<img src="Algorithms%20for%20Image%20Comparison.assets/matching.webp" alt="matching" style="zoom:50%;" />

Image matching using keypoint detectors and local descriptors is a successful image comparison method. **One possible downside is the running time of the final step of the algorithm that is  where is the number of the detected key points.** However, there are other algorithms that perform the matching step between the key points faster using [quadtrees](https://en.wikipedia.org/wiki/Quadtree) or [binary space partitioning](https://en.wikipedia.org/wiki/Binary_space_partitioning).

## 5. Siamese Networks

**Despite its intuitiveness, image matching cannot generalize well in real-world images. Its performance depends on the quality of the key point detector and the local feature descriptor.** Now, we’ll move on to the best image comparison algorithm nowadays that uses Siamese Networks.

**A [Siamese Network](https://en.wikipedia.org/wiki/Siamese_neural_network) is a neural network that consists of two identical subnetworks meaning that they contain exactly the same parameters and weights.** Each subnetwork can be any neural network designed for images like a [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network). The network’s input is a pair of images that are either similar (positive example) or not similar (negative example).

During training, we pass the images through the subnetworks, and we get as output two feature vectors, one for each image. **If the input pairs are similar, we want these two vectors to be as close as possible and vice versa.** To achieve this, we use the **contrastive loss function** that takes a pair of vectors $(x_i,x_j)$ and minimizes their euclidean distance when they come from similar images while maximizing the distance otherwise:
$$
L = (1-y)*\Vert x_i-x_j \Vert^2 + y*\max(0,m-\Vert x_i-x_j \Vert^2 )
$$
where $y=0$ if the images are similar and $y=1$ otherwise. Also, $m$ is a hyperparameter, defining the lower bound distance between images that are not similar.

In the below images, we can see the siamese architecture is the case of positive and negative examples:

<img src="Algorithms%20for%20Image%20Comparison.assets/siamese1-1024x361.webp" alt="siamese1-1024x361" style="zoom:50%;" />

**After training, the network has successfully learned to compare any pair of images using the euclidean distance of their output vectors (small distance corresponds to high similarity).**

Using Siamese networks, we are able to compare images with high precision even in the most extreme conditions (low-quality images, blurring, occlusions, etc.). **The only downside is that this is a learning-based method requiring a labeled image dataset for training.**

## 6. Conclusion

In this tutorial, we discussed three algorithms for image comparison. First, we made a brief introduction to the problem. Then, we presented the algorithms along with illustrative examples.

**References**

> https://www.baeldung.com/cs/image-comparison-algorithm