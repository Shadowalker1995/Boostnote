# Categorical cross-entropy and SoftMax regression

> Ever wondered how to implement a simple baseline model for multi-class problems? Here is one example (code included)

<img src="Categorical%20cross-entropy%20and%20SoftMax%20regression.assets/1*-3yza9S1OCTAANFXGkgYQg.jpeg" alt="img" style="zoom:33%;" />

Although it finds its roots in statistics, logistic regression is a fairly standard approach to solve binary classification problems in machine learning and is by far the most commonly used algorithm for such classification tasks in real-life applications. By design, it can, however, handle only **binary classification problems**, i.e. problems wherein the object to be classified belongs to one of two classes (e.g. malfunctioning or not, pass or fail, sick or healthy, etc). But what if you have more than two classes? Here comes the **SoftMax** regression!

SoftMax regression is a relatively straightforward extension of the binary logistic regression (see this [post](https://towardsdatascience.com/binary-cross-entropy-and-logistic-regression-bf7098e75559) for a quick recap if needed) for multi-class problems. While the latter relies on the minimization of the so-called **binary cross-entropy**:
$$
\mathcal{J} (\mathbf{w}) = - \frac{1}{m} \sum_{i=1}^m \big[ y_i \log \sigma(\mathbf{w}^T \mathbf{x}_i) + (1-y_i) \log (1 - \sigma(\mathbf{w}^T \mathbf{x}_i)) \big]
$$
the former relies on the minimization of its generalization: the **categorical cross-entropy**:
$$
\mathcal{J} (\mathbf{w}) = - \frac{1}{m} \sum_{i=1}^m \sum_{k=1}^K 1\{ y_i = k \} \log \frac{\exp(\mathbf{w}_k^T \mathbf{x}_i)}{\sum_{j=1}^K \exp(\mathbf{w}_j^T \mathbf{x}_i)}
$$
where $1\{ y=k \}$ is an indicator function (i.e. $1\{ y=k \} = 1$ if the example belongs to class $k$ and 0 otherwise). But what is this mathematical mumbo jumbo? How do I go from two classes to an arbitrary number of classes? And more importantly, how can I train my model more efficiently than with plain old gradient descent? We'll address these questions below and provide a simple implementation in Python (we'll actually implement it, not rely on scikit-learn as numerous other posts do…). But first, let us briefly introduce the SoftMax function!

### A (brief) introduction to the SoftMax function

The SoftMax function is a generalization of the ubiquitous logistic function. It is defined as:
$$
\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^k e^{z_j}}
$$
where the exponential function is applied element-wise to each entry of the input vector $\mathbf{z}$. The normalization ensures that the sum of the components of the output vector $\sigma(\mathbf{z})$ is equal to one. As for the classical logistic function, all of its outputs are bounded between 0 and 1 which makes it a natural candidate to model the probability distribution in a multi-class problem. It inherits most of the properties of the logistic function, the most important one for our purposes being:
$$
\frac{\partial \sigma_i(\mathbf{z})}{\partial z_k} = \sigma_i(\mathbf{z}) (\delta_{ik} - \sigma_k(\mathbf{Z})
$$
where the Kronecker symbol $\delta$ is equal to one if $i = k$ and 0 otherwise.

### Properties of the categorical cross-entropy for SoftMax regression

Given an example $\mathbf{x}$, the softmax function can be used to model the probability it belongs to class $y = k$ as follows:
$$
\mathcal{P}(y=k | \mathbf{x}, \mathbf{W}) = \frac{\exp(\mathbf{w}_k^T \mathbf{x})}{sum_{j=1}^K \exp(\mathbf{w}_j^T \mathbf{x})}
$$
where $\mathbf{W}$ are the parameters of our model. Our goal will thus be to find the parameters $\mathbf{W}$ such that the modeled probability function is as close as possible to the true one. As for the binary logistic regression, this will involve the maximization of the likelihood function (or equivalently the minimization of the negative log-likelihood) with an exponentiation trick. Since going from the definition of our probability distribution to the categorical cross-entropy closely follows what we have done for the binary logistic regression and I thus refer you to the corresponding post if you need a quick refresh.

**A convex function**

Our goal is to find the weight matrix $\mathbf{W}$ minimizing the categorical cross-entropy. In the most general case, a function may however admit multiple minima, and finding the global one is considered a hard problem. It can be shown nonetheless that minimizing the categorical cross-entropy for the SoftMax regression is a convex problem and, as such, any minimum is a global one!

Let us derive the gradient of our objective function. To facilitate our derivation and subsequent implementation, consider the vectorized version of the categorical cross-entropy:
$$
\mathcal{J}(\mathbf{W}) = \frac{1}{m} \mathbf{Y} \odot \log (\sigma(\mathbf{XW}))
$$
where each row of $\mathbf{X}$ is one of our training examples, $\mathbf{Y}$ is the one-hot encoded label vector and the log is applied element-wise. Finally, $\odot$ denotes the **Hadamard Product**, i.e. the element-wise multiplication of two matrices. Using some elements of matrix calculus, the gradient of our loss function with respect to $\mathbf{W}$ is given by:
$$
\nabla \mathcal{J} = \mathbf{X}^T (\sigma(\mathbf{XW}) - \mathbf{Y})
$$
Continuing this derivation once more would yield the **Hessian** of our problem. Once again, it follows rather closely the derivation for the logistic regression. From there, it is straightforward to show that its smallest eigenvalue is larger or equal to zero. Hence, it is symmetric positive semi-definite and our optimization problem is convex!

**Over-parameterization**

Before moving on with how to find the optimal solution and the code itself, let us emphasize a particular property of SoftMax regression: it is **over-parameterized**! Some of the model's parameters are redundant. Starting from the definition of $\mathcal{P}(y=i|x)$, it can be shown that subtracting an arbitrary vector $\mathbf{v}$ from every weight vector $\mathbf{w}$ does not change the output of the model. The matrix of weights $\mathbf{W}$ thus contains one extra weight vector not required to solve the problem. If one does not account for this redundancy, our minimization problem will admit an infinite number of equally likely optimal solutions. Without loss of generality, we can thus assume for instance that the weight vector $\mathbf{w}$ associated with the last class is equal to zero. Doing so enables us to get rid of this over-parameterization issue.

### How to minimize it?

Unlike linear regression, no closed-form solution exists for SoftMax regression. However, the categorical cross-entropy being a convex function in the present case, any technique from convex optimization is nonetheless guaranteed to find the global optimum. In the rest of this post, we'll illustrate the implementation of SoftMax regression using a slightly improved version of gradient descent, namely **gradient descent with (adaptive) optimal learning rate**.

**Gradient descent with optimal learning rate**

In machine learning, variations of gradient descent are the workhorses of model training. In this framework, the weight matrix $\mathbf{W}$ is iteratively updated following the simple rule:
$$
\mathbf{W}_{i+1} = \mathbf{W}_i - \alpha \nabla \mathcal{J}(\mathbf{W}_i)
$$
until convergence is reached. Here $\alpha$ is known as the **learning rate** or step size. It is quite common to use a constant learning rate but how to choose it? Simple math shows that the [Lipschitz constant](https://en.wikipedia.org/wiki/Lipschitz_continuity) (using the Frobenius norm) of the categorical cross-entropy function is:
$$
L = \frac{k-1}{km} \| X \|_F
$$
where $k$ is the number of different classes in the problem investigated so that the "optimal" learning rate is approximately:
$$
\alpha = \frac{km}{k-1} \frac{1}{\| X \|_F}
$$
A larger learning rate would cause the computation to diverge. A much smaller one would yield convergence but at the price of a very large number of iterations. Alternatively, one can use an [(inexact) line search](https://en.wikipedia.org/wiki/Wolfe_conditions) at each iteration to have an adaptive/optimal learning rate. Below is a simple Python/SciPy implementation ([SoftMax_regression.py](https://gist.github.com/loiseaujc/bcf289881fc0ddccc1d7eba1451b5bb9#file-softmax_regression-py)) of the corresponding algorithm using [Brent's method](https://en.wikipedia.org/wiki/Brent's_method) to find the quasi-optimal learning rate. Assuming you are already familiar with Python, the code should be quite self-explanatory.

```python
# --> Import standard Python libraries.
import numpy as np
from scipy.special import softmax
from scipy.linalg import norm
from scipy.optimize import line_search, minimize_scalar

# --> Import sklearn utility functions.
from sklearn.base import BaseEstimator, ClassifierMixin

def SoftMax(x):
    """
    Protected SoftMax function to avoid overflow due to
    exponentiating large numbers.
    """

    # --> Add a feature associated to the neglected class.
    x = np.insert(x, x.shape[1], 0, axis=1)

    # --> Max-normalization to avoid overflow.
    x -= np.max(x)

    return softmax(x, axis=1)

def cross_entropy(W, X, y, epsilon=1e-10):
    """
    Implementation of the categorical cross-entropy.
    """

    # --> Evaluate model.
    ypred  = SoftMax(X @ W)

    # --> Compute the cross-entropy.
    return -np.mean(y * np.log(ypred + epsilon))

def cross_entropy_gradient(W, X, y):
    """
    Evalute the gradient of the cross-entropy function.
    """

    # --> Number of training examples
    m = X.shape[0]

    # --> Evaluate model.
    ypred = SoftMax(X @ W)

    # --> Compute the gradient.
    gradient = X.T @ (ypred[:, :-1] - y[:, :-1]) / m

    return gradient

class SoftMax_regression(BaseEstimator, ClassifierMixin):
    """
    Implementation of the SoftMax regression. Minimization is performed
    using gradient descent with adaptive learning rate obtained from an
    inexact line search. Note that we assume a unit-term has been prepended
    to X for the sake of simplicity.
    """

    def __init__(self, maxiter=100000, tol=1e-6):
        # --> Maximum number of iterations.
        self.maxiter = maxiter

        # --> Tolerance for the optimizer.
        self.tol = tol

    def fit(self, X, y):
        """
        Implementation of the gradient descent with inexact line search
        for the learning rate performed by Brent's method.
        INPUT
        -----
        X : numpy 2D array. Each row corresponds to one training example.
        y : numpy 2D array. One-hot encoded vector of labels.
        OUTPUT
        ------
        self : The trained SoftMax regression model.
        """

        # --> Add the bias.
        X = np.insert(X, 0, 1, axis=1)

        # --> Number of examples and features.
        m, n = X.shape

        # --> Number of classes - 1.
        k = y.shape[1] -1

        # --> Initialize the weights matrix.
        W = np.zeros((n, k))

        # --> Maximum value for the learning rate derived from the Lipschitz constant
        #     of the categorical cross-entropy function.
        amax = (k+1)*m / (k*norm(X))

        # --> Training using gradient descent and optimal stepsize.
        for _ in range(self.maxiter):
            # --> Compte the gradient.
            p = cross_entropy_gradient(W, X, y)

            # --> Check for convergence.
            if norm(p)**2 < self.tol:
                break

            # --> Compute a quasi-optimal stepsize using 1D minimization.
            res = minimize_scalar(
                lambda alpha : cross_entropy(W - alpha*p, X, y),
                bracket=(0, amax),
                method="brent",
                tol=0.1*self.tol*amax
            )

            # --> Worst-case scenario : Brent's method failed (or returned negative values).
            #     Switch back to the inverse Lipschitz constant.
            if res["success"] and (res["x"] > 0):
                alpha = res["x"]
            else:
                alpha = 0.5*amax

            # --> Update the weights.
            W -= alpha*p

        # --> Final weights and biases.
        self.bias, self.W = W[0, :], W[1:, :]

        return self

    def predict_proba(self, X):
        return SoftMax(X @ self.W + self.bias)

    def predict(self, X):
        return self.predict_proba(X).argmax(axis=1)
```

Although it ensures that the objective function will decrease at each step, this implementation is by no means optimized. Some performance gains could be obtained by refactoring the code a bit albeit at the expense of readability (which I believe is more important in such an introductory post). Moreover, more efficient optimization techniques could have been used, e.g. **gradient descent with momentum**, **Newton-Raphson's method**, **stochastic gradient descent**, **ADAM**, etc. This variant of gradient descent is however sufficiently simple to code and reasonably efficient. I would thus suggest sticking to it as a starting point and move on to more advanced optimizers once you get comfortable.

### Going beyond vanilla SoftMax regression

Like its binary counterpart (i.e. logistic regression), SoftMax regression is a fairly flexible framework for classification tasks. As such, numerous variants have been proposed over the years to overcome some of its limitations.

**Handling nonlinearly separable classes**

By construction, SoftMax regression is a linear classifier. Just like linear regression can be extended to model nonlinear relationships, logistic and SoftMax regressions can also be extended to classify points otherwise nonlinearly separable. Doing so may however require expert knowledge, a good understanding of the properties of the data, and feature engineering (which is more of a craft than exact science).

**Imbalanced class distribution**

Implicit when using cross-entropy is the fact that the prevalence of each class in our training dataset is roughly the same. There are however numerous real-life situations where this is not the case. The same tricks that are used for imbalance classification in binary classification can be adapted to multi-class problems, in particular, the cost-sensitive training (see [this post](https://towardsdatascience.com/binary-cross-entropy-and-logistic-regression-bf7098e75559) for more details).

**Regularization**

It is fairly common in machine learning to handle data characterized by a large number of features. Not all of these features may however be informative for prediction purposes. For the example of digit classification on the MNIST dataset, these features are the 784 different pixels of the images.

<img src="Categorical%20cross-entropy%20and%20SoftMax%20regression.assets/1*EXFVjRzGYx0k1qrnc470Qw.png" alt="img" style="zoom:10%;" />

<center style="color:#C0C0C0;">A random subset of handwritten digits from the MNIST dataset.</center>

However, these images being standardized, the outermost pixels provide little to no information for the task considered. In such a situation, it is possible to *regularize* the optimization problem such that the coefficients associated with uninformative features are set to zero. The simplest such sparsity-promoting regularized version of the problem is the following one:
$$
\mathcal{J}(\mathbf{W}) = CCE(\mathbf{W}) + \lambda \| \mathbf{W} \|_1
$$
where $CCE(\mathbf{W})$ is a shorthand notation for categorical cross-entropy and the $\ell_1$-norm of $\mathbf{W}$ is the sum of the absolute value of its entries. The parameter $\lambda$ **controls the trade-off between the minimization of the cross-entropy function and the desired sparsity of the weight matrix**. Only small modifications to the code provided are needed to solve this new optimization problem.

### Conclusion

Over the past decade, deep neural networks have gained a lot of traction and appear to be used absolutely everywhere and for literally everything. Although this may be true in certain domains (e.g. computer vision), a lot of more classical domains still rely on simpler but well-established techniques (e.g. in manufacturing). Because of its simplicity and flexibility, both from a mathematical and computational point of view, SoftMax regression is by far the most commonly used technique for multi-class classification in real-life applications. In machine learning, despite the superiority of deep nets, it nonetheless makes for an excellent baseline model to evaluate what has been actually gained by moving to a more complex neural network model (i.e. was it really worth it ?).

I hope that you now have a better understanding of what SoftMax regression is, how it works and how it can be implemented. As usual, there is a lot we did not cover (e.g. the statistical interpretation of the model, how to go beyond the simple accuracy metric, etc) but the Internet is full of excellent resources! Just go check it out! Also, do not hesitate to derive all of the mathematical results presented herein yourself and to play with the codes provided!

### References

https://towardsdatascience.com/categorical-cross-entropy-and-softmax-regression-780e8a2c5e8c