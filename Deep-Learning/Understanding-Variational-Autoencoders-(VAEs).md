# Understanding Variational Autoencoders (VAEs)

> Building, step by step, the reasoning that leads to VAEs.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1*mbCY2_LZX2bpGX7CH80FAg.jpeg" alt="img" style="zoom: 67%;" />

## Introduction

In the last few years, deep learning based generative models have gained more and more interest due to (and implying) some amazing improvements in the field. Relying on huge amount data, well-designed networks architectures and smart training techniques, deep generative models have shown an incredible ability to produce highly realistic pieces of content of various kind, such as images, texts and sounds. Among these deep generative models, two major families stand out and deserve a special attention: **Generative Adversarial Networks (GANs)** and **Variational Autoencoders (VAEs)**.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1*BaZPg3SRgZGVigguQCmirA.png" alt="img" style="zoom:50%;" />

<center style="color:#C0C0C0;">Face images generated with a Variational Autoencoder (source: Wojciech Mormul on Github).</center>

In Generative Adversarial Networks (GANs), adversarial training can oppose two networks, a generator and a discriminator, to push both of them to improve iteration after iteration. In this post, we introduce the other major kind of deep generative models: Variational Autoencoders (VAEs). In a nutshell, a VAE is an autoencoder whose encodings distribution is regularized during the training in order to ensure that its latent space has good properties allowing us to generate some new data. Moreover, the term "variational" comes from the close relation there is between the regularization and the variational inference method in statistics.

If the last two sentences summarize pretty well the notion of VAEs, they can also raise a lot of questions. What is an autoencoder? What is the latent space and why regularizing it? How to generate new data from VAEs? What is the link between VAEs and variational inference? In order to describe VAEs as well as possible, we will try to answer all this questions and to provide the reader with as much as insights as we can (ranging from basic intuitions to more advanced mathematical details). Thus, the purpose of this post is not only to discuss the fundamental notions VAEs rely on but also to build step by step and starting from the very beginning the reasoning that leads to these notions.

### Outline

In the first section, we will review some important notions about dimensionality reduction and autoencoder that will be useful for the understanding of VAEs. Then, in the second section, we will show why autoencoders cannot be used to generate new data and will introduce Variational Autoencoders that are regularized versions of autoencoders making the generative process possible. Finally in the last section we will give a more mathematical presentation of VAEs, based on variational inference.

> **Note:** In the last section we have tried to make the mathematical derivation as complete and clear as possible to bridge the gap between intuition and equations. However, the readers that doesn't want to dive into the mathematical details of VAEs can skip this section without hurting the understanding of the main concepts. Notice also that this post we will make the following abuse of notation: for a random variable $z$, we will denote $p(z)$ the distribution (or the density, depending on the context) of this random variable.

## Dimensionality reduction, PCA and autoencoders

In this first section we will start by discussing some notions related to dimensionality reduction. In particular, we will review briefly principal component analysis (PCA) and autoencoders, showing how both ideas are related to each other.

### What is dimensionality reduction?

In machine learning, **[dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction) is the process of reducing the number of features that describe some data.** This reduction is done either by **selection** (only some existing features are conserved) or by **extraction** (a reduced number of new features are created based on the old features) and can be useful in many situations that require low dimensional data (data visualization, data storage, heavy computation...). Although there exists many different methods of dimensionality reduction, we can set a global framework that is matched by most (if not any!) of these methods.

First, let's call **encoder** the process that produce the "new features" representation from the "old features" representation ( by selection or by extraction) and **decoder** the reverse process. Dimensionality reduction can then be interpreted as data compression where the encoder compress the data ( from the initial space to the **encoded space**, also called **latent space**) whereas the decoder decompress them. Of course, depending on the initial data distribution, the latent space dimension and the encoder definition, this compression can be lossy, meaning that a part of the information is lost during the encoding process and cannot be recovered when decoding.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1*UdOybs9wOe3zW8vDAfj9VA@2x.png" alt="img" style="zoom:50%;" />

<center style="color:#C0C0C0;">Illustration of the dimensionality reduction principle with encoder and decoder.</center>

The main purpose of a dimensionality reduction method is to find the best encoder/decoder pair among a given family. In other words, for a given set of possible encoders and decodes, we are looking for the pair that **keep the maximum of information when encoding and, so, has the minimum of reconstruction error when decoding**. If we denote respectively $E$ and $D$ the families of encoders and decoders we are considering, then the dimensionality reduction problem can be written:
$$
(e^\star, d^\star) = \arg \min_{(e,d) \in E \times D} \epsilon(x, d(e(x)))
$$
where $\epsilon(x, d(e(x)))$ defines the reconstruction error measured between the input data $x$ and the encoded-decoded data $d(e(x))$. Notice finally that in the following we will denote $N$ the number of data, $n_d$ the dimension of the initial (decoded) space and $n_e$ the dimension of the reduced (encoded) space.

### Principal Components Analysis (PCA)

One of the first methods that come in mind when speaking about dimensionality reduction is **[principal component analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis)**. In order to show how it fits the framework we just describe and make link towards autoencoders, let's give a very high overview of how PCA works, letting most of the detailed aside.

The idea of PCA is to build $n_e$ new **independent** features that are **linear combination** of the $n_d$ old features and so that the projections of the data on the subspace defined by these new features are as close as possible to the initial data (in term of euclidean distance). In other words, PCA is looking for the best linear subspace of the initial space (describe by an orthogonal basis of new features) such that the error approximating the data by their projections on this subspace is as small as possible.

Translated in our global framework, we are looking for an encoder in the family $E$ of the $n_e \times n_d$ matrices (linear transformation) whose rows are orthonormal (features independence) and for the associated decoder among the family $D$ of $n_d \times n_e$ matrices. It can be shown that the unitary eigenvectors corresponding to the $n_e$ greatest eigenvalues (in norm) of the covariance features matrix are orthogonal ( or can be chosen to be so) and define the best subspace of dimension $n_e$ eigenvectors can be chosen as our new features and, so, the problem of dimension reduction can then be expressed as an eigenvalue/eigenvector problem. Moreover, it can also be shown that, in such case, the decoder matrix is the transposed of the encoder matrix.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1*LRPyMAwDlio7f1_YKYI2hw@2x.png" alt="img" style="zoom:50%;" />

<center style="color:#C0C0C0;">PCA matches the encoder-decoder framework we described.</center>

### Autoencoders

Let's now discuss autoencoders and see how we can use neural networks for dimensionality reduction. The general idea of autoencoders is pretty simple and consist in setting an encoder and a decoder as neural networks and to learn the best encoding-decoding scheme using an iterative optimization process. So, at each iteration we feed the autoencoder architecture (the encoder followed by the decoder) with some data, we compare the encoded-decoded output with the initial data and backpropagate the error through the architecture to update the weights of the networks.

Thus, intuitively, the overall autoencoder architecture (encoder+decoder) creates a bottleneck for data that ensures only the main structured part of the information can go through and be reconstructed. Looking at our general framework, the family $E$ of considered encoder is defined by the encoder network architecture, the family $D$ of considered decoders is defined by the decoder network architecture and the search of encoder and decoder that minimize the reconstruction error is done by gradient descent over the parameters of these networks.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1*bY_ShNK6lBCQ3D9LYIfwJg@2x.png" alt="img" style="zoom:50%;" />

<center style="color:#C0C0C0;">Illustration of an autoencoder with its loss function.</center>

Let's first suppose that both our encoder and decoder architectures have only one layer without non-linearity (linear autoencoder). Such encoder and decoder are then simple linear transformation that can be expressed as matrices. In such situation, we can see a clear link with PCA in  the sense that, just like PCA does, we are looking for the best linear subspace to project data on with as few information loss as possible when doing so. Encoding and decoding matrices obtained with PCA define naturally one of the solutions we would be satisfied to reach by gradient descent, but we should outline that this is not the only one. Indeed, several basis can be chosen to describe the same optimal subspace, and so, several encoder/decoder pairs can give the optimal reconstruction error. Moreover, for linear autoencoders and contrarily to PCA, the new features we end up do not have to be independent (no orthogonality constraints in the neural networks).

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1*ek9ZFmimq9Sr1sG5Z0jXfQ@2x.png" alt="img" style="zoom:50%;" />

<center style="color:#C0C0C0;">Link between linear autoencoder and PCA.</center>











> https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73