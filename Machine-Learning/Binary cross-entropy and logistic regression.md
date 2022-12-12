# Binary cross-entropy and logistic regression

> Ever wondered why we use it, where it comes from and how to optimize it efficiently? Here is one explanation (code included).

<img src="Binary%20cross-entropy%20and%20logistic%20regression.assets/1*-3yza9S1OCTAANFXGkgYQg.jpeg" alt="img" style="zoom: 33%;" />

Although it finds its roots in statistics, logistic regression is a fairly standard approach to solve binary classification problems in machine learning. It is actually so standard that it is implemented in all major data analysis software (e.g. Excel, [SPSS](https://www.ibm.com/analytics/spss-statistics-software), or its open-source alternative [PSPP](https://www.gnu.org/software/pspp/)) and libraries (e.g. [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html), etc). Even if you are only mildly familiar with logistic regression, you may know that it relies on the minimization of the so-called **binary cross-entropy**
$$
\mathcal{J} (\mathbf{w}) = - \frac{1}{m} \sum_{i=1}^m \big[ y_i \log \sigma(\mathbf{w}^T \mathbf{x}_i) + (1-y_i) \log (1 - \sigma(\mathbf{w}^T \mathbf{x}_i)) \big]
$$
where $m$ is the number of samples, $\mathbf{x}_i$ is the $i$-th training example, $y_i$ is the corresponding class (i.e., either 0 or 1), $\sigma(z)$ is the logistic function and $\mathbf{w}$ is the vector of parameters of the model. You may also know that, for logistic regression, it is a convex function. As such, any minimum is a global minimum. But have you ever wondered why we use it, where it actually comes from or how you could find this minimum more efficiently than with plain gradient descent? We'll address these questions below and provide simple implementations in Python. But first, let us do a quick recap about the logistic function!

### (Very) Quick recap’ about the logistic function

<img src="Binary%20cross-entropy%20and%20logistic%20regression.assets/1*Dp-LdM15MqyNX4JYUAXkPg.jpeg" alt="img" style="zoom: 10%;" />

<center style="color:#C0C0C0;">Graph of the logistic function.</center>

The logistic function $\sigma(z)$ is an S-shaped curve defined as:
$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$
It is also sometimes known as the $expit$ function or the $sigmoid$. It is monotonic and is bounded between 0 and 1, hence its widespread usage as a model for probability. We moreover have:
$$
1 - \sigma(z) = \sigma(-z)
$$
Finally, you can easily show that its derivative with respect to $z$ is given by:
$$
\frac{\mathrm{d} \sigma(z)}{\mathrm{d} z} = \sigma(z) (1 - \sigma(z))
$$
This is pretty much all you need to know about this function (at least for this post). So, without further ado, let us get started!

### Deriving the binary cross-entropy for logistic regression

Let us consider a predictor $\mathbf{x}$ and a binary (or Bernoulli) variable $y$. Assuming there exist some relationship between $\mathbf{x}$ and $y$, an ideal model would predict
$$
\mathcal{P} (y | \mathbf{x}) =
	\begin{cases}
		1 & \text{if } \ y=1 \\
		0 & \text{if } \ y=0
	\end{cases}
$$
By using logistic regression, this unknown probability function is modeled as:
$$
\hat{\mathcal{P}} (y=1 | \mathbf{x}, \mathbf{w}) = \frac{1}{1 + e^{-\mathbf{w}^T\mathbf{x}}}
$$
Our goal is thus to find the parameters $\mathbf{w}$ such that the modeled probability function is as close as possible to the true one.

**From the Bernoulli distribution to the binary cross-entropy**

One way to assess how good of a job our model is doing is to compute the so-called $likelihood$ function. Given $m$ examples, this likelihood function is defined as:
$$
\mathcal{L}(\mathbf{w}) = \prod_{i=1}^m \hat{\mathcal{P}} (y_i | \mathbf{x}_i, \mathbf{w})
$$
Ideally, we thus want to find the parameters $\mathbf{w}$ that maximizes $\mathcal{L}(\mathbf{w})$. In practice, however, one usually does not work directly with this function but with its negative log for the sake of simplicity:
$$
- \log \mathcal{L}(\mathbf{w}) = - \sum_{i=1}^m \log \hat{\mathcal{P}} (y_i | \mathbf{x}_i, \mathbf{w})
$$
Because logarithm is a strictly monotonic function, minimizing the negative log-likelihood will result in the same parameters $\mathbf{w}$ as when maximizing directly the likelihood function. But how to compute $\mathcal{P}(y | \mathbf{x}, \mathbf{w})$ when our logistic regression only models $\mathcal{P}(1 | \mathbf{x}, \mathbf{w})$? Given that:
$$
\hat{\mathcal{P}}(0 | \mathbf{x}, \mathbf{w}) = 1 - \hat{\mathcal{P}}(1 | \mathbf{x}, \mathbf{w})
$$
one can use a simple exponentiation trick to write:
$$
\hat{\mathcal{P}}(y | \mathbf{x}, \mathbf{w}) = \hat{\mathcal{P}}(1 | \mathbf{x}, \mathbf{w})^y \times \hat{\mathcal{P}}(0 | \mathbf{x}, \mathbf{w})^{1-y}
$$
Inserting this expression into the negative log-likelihood function (and normalizing by the number of examples), we finally obtain the desired normalized binary cross-entropy:
$$
\begin{equation} \begin{aligned}
	\mathcal{J}(\mathbf{w}) &=  - \frac{1}{m} \sum_{i=1}^m \big[ y_i \log \hat{\mathcal{P}}(1 | \mathbf{x}_i, \mathbf{w}) + (1-y_i) \log (1 - \hat{\mathcal{P}}(0 | \mathbf{x}_i, \mathbf{w})) \big] \\
	&= - \frac{1}{m} \sum_{i=1}^m \big[ y_i \log \sigma(\mathbf{w}^T \mathbf{x}_i) + (1-y_i) \log (1 - \sigma(\mathbf{w}^T \mathbf{x}_i)) \big]
\end{aligned} \end{equation}
$$
Finding the weight $\mathbf{w}$ minimizing the binary cross-entropy is thus equivalent to finding the weights that maximizing the likelihood function assessing how good of a job of our logistic regression model is doing at approximating the true probability distribution of our Bernoulli variable.

**Proving it is a convex function**

As stated, our goal is to find the weights $\mathbf{w}$ that minimizes the binary cross-entropy. In the most general case, a function may however admit multiple minima, and finding the global one is considered a hard problem. It can be shown nonetheless that minimizing the binary cross-entropy for the logistic regression is a convex problem and, as such, any minimum is a global one. Let us prove quickly it is indeed a convex problem!

Several approaches could be used to prove that a function is convex. A sufficient condition is however that its **Hessian Matrix** (i.e. its matrix of second-order derivatives) is positive semi-definite for all possible values of $\mathbf{w}$. To facilitate our derivation and subsequent implementation, let us consider the vectorized version of the binary cross-entropy, i.e.:
$$
\mathcal{J}(\mathbf{w}) = - \frac{1}{m} \big[ \mathbf{y}^T \log \sigma(\mathbf{Xw}) + (1-\mathbf{y})^T \log \sigma(-\mathbf{Xw}) \big]
$$
where each row of $\mathbf{X}$ is one of our training examples and we made use of some identities introduced along with the logistic function. Using some elements of matrix calculus (check [here](https://en.wikipedia.org/wiki/Matrix_calculus) if you're not familiar with it), one can show that the gradient of our loss function with respect to $\mathbf{w}$ is given by:
$$
\nabla_{\mathbf{w}} \mathcal{J}(\mathbf{w}) = \frac{1}{m} \mathbf{X}^T (\sigma(\mathbf{Xw} - \mathbf{y}))
$$
Similarly, the Hessian matrix reads
$$
\mathbf{H}(\mathbf{w}) = \mathbf{X}^T \mathbf{D} \mathbf{X}
$$
with
$$
\mathbf{D} = \frac{1}{m} \mathrm{diag}( \sigma(\mathbf{Xw}) (1 - \sigma(\mathbf{Xw})) )
$$
From this point, one can easily show that:
$$
\label{long3000}
\begin{equation} \begin{aligned} 
\mathbf{a}^T \mathbf{H}(\mathbf{w}) \mathbf{a} &= \mathbf{a}^T \mathbf{X}^T \mathbf{D} \mathbf{X} \mathbf{a} \\
&= \mathbf{a}^T \mathbf{X}^T \mathbf{D} \mathbf{X} \mathbf{a} \\
&= \\
&\ge 0
\end{aligned} \end{equation}
$$
Hence, the Hessian matrix is positive semi-definite for every possible $\mathbf{w}$ and the binary cross-entropy (for the logistic regression) is a convex function. Now that we know our optimization problem is well-behaved, let us turn our attention to how to solve it!

### How to find efficiently this minimum?

Unlike linear regression, no closed-form solution exists for logistic regression. The binary cross-entropy being a convex function in the present case, any technique from convex optimization is nonetheless guaranteed to find the global minimum. We'll illustrate this point below using two such techniques, namely **Gradient Descent with optimal learning rate** and **Newton-Raphson's method**.

**Gradient descent with optimal learning rate**

In machine learning, variations of gradient descent are the workhorses of model training. In this framework, the weights $\mathbf{w}$ are iteratively updated following the simple rule:
$$
\mathbf{w} = \mathbf{w} - \alpha \nabla_{\mathbf{w}} \mathcal{J}(\mathbf{w})
$$
until convergence is reached. Here, $\alpha$ is known as the *learning rate* or step size. It is quite common to use a constant learning rate but how to choose it? By computing the expression of the **Lipschitz Constant** of various loss functions, Yedida & Saha [^1] have recently shown that, for the logistic regression, the optimal learning rate is given by
$$
\alpha = \frac{2m}{\| \mathbf{X} \|_F}
$$
Below is a simple Python implementation ([logistic_regression_gd.py](https://gist.github.com/loiseaujc/0f9b1b29db4afc9d27cc36cf040089a6#file-logistic_regression_gd-py)) of the corresponding algorithm. Assuming you are already familiar with Python, the code should be quite self-explanatory.

```python
# --> Import standard Python libraries.
import numpy as np
from scipy.special import expit
from scipy.linalg import norm

# --> Import sklearn utility functions.
from sklearn.base import BaseEstimator, ClassifierMixin


class LogisticRegression_GD(BaseEstimator, ClassifierMixin):

    """
    Implementation of Logistic Regression. Minimization is performed
    by gradient descent. Note that we assume a unit-term has been prepended
    to X for the sake of simplicity.
    """

    def __init__(self, maxiter=1000, tol=1e-6):

        # --> Maximum number of iterations.
        self.maxiter = maxiter

        # --> Tolerance for the optimizer.
        self.tol = tol

    def predict(self, X):
        return np.rint(self.predict_proba(X)).astype(np.int)

    def predict_proba(self, X):
        return expit(X @ self.weights)

    def fit(self, X, y):
        """
        Implementation of the gradient descent method with optimal
        learning rate following [1].
        INPUT
        -----
        X : numpy 2D array. Each row corresponds to one training example.
            It is assumed that the first column is a column of ones (bias).
        y : numpy 1D array. Label (0 or 1) of each example.
        OUTPUT
        ------
        self : The trained logistic regression model.
        References
        ----------
        [1] R. Yedida & S. Saha. LipschitzLR: Using theoritically computed
        adaptive learning rates for fast convergence. arXiv eprint 1902.07399.
        """

        # --> Number of examples and features.
        m, n = X.shape

        # --> Initialize the weights.
        self.weights = np.zeros((n, ))

        # --> Compute optimal learning rate (see [1]).
        alpha = 2*m / norm(X)

        # --> Training using gradient descent and optimal stepsize.
        for _ in range(self.maxiter):

            # --> Compute the gradient.
            grad = X.T @ (self.predict_proba(X) - y) / m

            # --> Update the weights.
            self.weights -= alpha * grad

            # --> Check for convergence.
            if norm(grad)**2 < self.tol:
                break

        return self
```

**Newton-Raphson's method**

Gradient Descent-based techniques are also known as first-order methods since they only make use of the first derivatives encoding the local slope of the loss function. When proving the binary cross-entropy for logistic regression was a convex function, we however also computed the expression of the Hessian matrix so let's use it!

Having access to the Hessian matrix allows us to use second-order optimization methods. Such techniques use additional information about the local curvature of the loss function encoded by this Hessian matrix to adaptively estimate the optimal step size in each direction during the training procedure, thus enabling faster convergence (albeit at a larger computational cost). The most famous second-order technique is the [Newton-Raphson's method](https://en.wikipedia.org/wiki/Newton's_method), named after the illustrious [Sir Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton) and lesser-known English mathematician [Joseph Raphson](https://en.wikipedia.org/wiki/Joseph_Raphson). Using this method, the update rule for the weights $\mathbf{w}$ is now given by
$$
\mathbf{w} = \mathbf{w} - \mathbf{H}^{-1}(\mathbf{w}) \nabla_{\mathbf{w}} \mathcal{J}(\mathbf{w})
$$
where $\mathbf{H}(\mathbf{w})$ is the **Hessian Matrix** evaluated for the current $\mathbf{w}$. Note that the entries of the Hessian matrix depend explicitly on the current $\mathbf{w}$. As such, it needs to be updated at every iteration and its inverse recomputed. Although it converges faster than plain gradient descent, Newton's method is thus more computationally expansive and memory intensive. For small to moderate-size problems, it may nonetheless still converge faster (in wall-clock time) than gradient descent. For larger problems, one may look at methods known as **Quasi-Newton**, the most famous one being the **BFGS** method. As before, a simple Python implementation ([logistic_regression_newt.py](https://gist.github.com/loiseaujc/7c38045001eda2e3b21e8d5cff8b4562#file-logistic_regression_newt-py)) of the corresponding algorithm is provided below.

```python
# --> Import standard Python libraries.
import numpy as np
from scipy.special import expit
from scipy.linalg import norm

# --> Import sklearn utility functions.
from sklearn.base import BaseEstimator, ClassifierMixin


class LogisticRegression_Newton(BaseEstimator, ClassifierMixin):

    """
    Implementation of Logistic Regression. Minimization is performed
    by Newton method. Note that we assume a unit-term has been prepended
    to X for the sake of simplicity.
    """

    def __init__(self, maxiter=1000, tol=1e-8):

        # --> Maximum number of iterations.
        self.maxiter = maxiter

        # --> Tolerance for the optimizer.
        self.tol = tol

    def predict(self, X):
        return np.rint(self.predict_proba(X)).astype(np.int)

    def predict_proba(self, X):
        return expit(X @ self.weights)

    def fit(self, X, y):
        """
        Implementation of the Newton method.
        INPUT
        -----
        X : numpy 2D array. Each row corresponds to one training example.
            It is assumed that the first column is a column of ones (bias).
        y : numpy 1D array. Label (0 or 1) of each example.
        OUTPUT
        ------
        self : The trained logistic regression model.
        """

        # --> Number of examples and features.
        m, n = X.shape

        # --> Initialize the weights.
        self.weights = np.zeros((n, ))

        # --> Training using gradient descent and optimal stepsize.
        for _ in range(self.maxiter):

            # --> Compute the gradient.
            grad = X.T @ (self.predict_proba(X) - y) / m

            # --> Compute the Hessian matrix.
            hess = X.T @ np.diag(expit(X @ self.weights) * (1-expit(X @ self.weights))) @ X / m

            # --> Update the weights.
            # NOTE : For real applications, do not use explicit inverse !
            self.weights -= np.linalg.inv(hess) @ grad

            # --> Check for convergence.
            if norm(grad)**2 < self.tol:
                break

        return self
```

### Going beyond vanilla logistic regression

Logistic regression provides a fairly flexible framework for classification tasks. As such, numerous variants have been proposed over the years to overcome some of its limitations.

**Handling nonlinearly separable classes**

By construction, logistic regression is a **linear classifier**. Just like linear regression can be extended to model nonlinear relationships, logistic regression can also be extended to classify points otherwise nonlinearly separable. Doing so may however require expert knowledge, a good understanding of the properties of the data, and feature engineering (which is more of a craft than exact science).

**Imbalanced class distribution**

When using vanilla logistic regression, we implicitly assume that the prevalence of the two classes in our samples is roughly the same (e.g. predicting whether an individual is male or female). There are however numerous real-life situations where this is not the case. This is particularly true in medical sciences **wherein** one may like to predict whether, given his/her medical record, a patient will die or not after say surgery. Hopefully, most patients already treated have survived and our training dataset thus only contains relatively few examples of patients who did die. This is known as a **class imbalance**.

Different approaches have been proposed to handle this class imbalance problem such as **up-sampling the minority class** or **down-sampling the majority one**. Another approach is to use **cost-sensitive training**. To illustrate the latter, let us considered the following situation: we have 90 samples belonging to say class $y=0$ (e.g., patient survived) and only 10 belonging to class $y=1$ (e.g., patient died)*.* If our model were to predict $y=0$ all the time (i.e., patient will survive), it would have a remarkable accuracy of 90% but would be nowhere useful to predict if a given patient is likely to die or not. A simple trick to improve the model's usefulness and predictive capabilities are however to modify the binary cross-entropy loss as follows:
$$
\mathcal{J} (\mathbf{w}) = - \frac{1}{m} \sum_{i=1}^m \big[ \alpha_1 y_i \log \sigma(\mathbf{w}^T \mathbf{x}_i) + \alpha_0 (1-y_i) \log (1 - \sigma(\mathbf{w}^T \mathbf{x}_i)) \big]
$$
The weights $\alpha_0$ and $\alpha_1$ are usually chosen as the inverse frequency of each class in the training set. Back to our small example above, $\alpha_0$ would be chosen as:
$$
\alpha_0 = \frac{100}{90} \simeq 1.11
$$
while $\alpha_1$ would be set to:
$$
\alpha_1 = \frac{100}{10} = 10
$$
Doing so, the model is more severely penalized (approximately 10 times more) when it misclassifies a patient likely to die than to survive. It requires only minor modifications of the algorithms presented before. Although this approach may increase the number of false-positive (i.e., patients that would survive wrongly classified as being likely to die), it reduces the number of false-negative (i.e., patients that would die wrongly classified as being likely to survive). Doctors can then focus their attention on patients who actually need it even though a few of them would have survived anyway.

**Multinomial classification**

Albeit binary classification problems are ubiquitous in real-life applications, some problems may require a multiclass approach exemplified by handwritten digit recognition.

<img src="Binary%20cross-entropy%20and%20logistic%20regression.assets/1*UIjrJpJ0QPIhcw38oYY0wA.png" alt="img" style="zoom:10%;" />

<center style="color:#C0C0C0;">A random subset of handwritten digits from the MNIST dataset.</center>

In this problem, one tries to assign a label (from 0 to 9) characterizing which digit is presented in the image. Even though logistic regression is by design a binary classification model, it can solve this task using a One-vs-Rest approach. Ten different logistic regression models are trained independently:

- Model 1: Predict whether the digit is a zero or not a zero.
- Model 2: Predict whether the digit is a one or not a one.
- …
- Model 10: Predict whether the digit is a nine or not a nine.

In the deployment phase, the label assigned to a new image is based on which of these models is the most confident about its prediction. This **One-vs-Rest** approach is however not free from limitations, the major three being :

- **Uncertainty quantification**: getting an estimate of the confidence of this model in its overall prediction is not straightforward. Although quantifying the uncertainty in the prediction may not be important for Kaggle-like competitions, it can be of crucial importance in industrial applications.
- **Undecidability**: how to handle the case when two of these models are equally confident about their prediction?
- **Imbalance learning**: each model learns using an imbalanced dataset. Assuming we have roughly the same number of examples for each digit, a given model only has 10% of training examples of this-particular-digit and 90% of not-this-particular-digit.

Despite these limitations, a One-vs-Rest logistic regression model is nonetheless a good baseline to use when tackling a multiclass problem and I encourage you to do so as a starting point. A more suitable approach, known as **softmax regression**, will be considered in an upcoming post.

**Regularized logistic regression**

It is fairly common in machine learning to handle data characterized by a large number of features. Not all of these features may however be informative for prediction purposes and one may thus aim for a **sparse logistic regression** model. To do so, one can for instance use an $\ell_1$-norm regularization of the model's weights. The modified loss function is then given by:
$$
\mathcal{J}(\mathbf{w}) = CE(\mathbf{w}) + \lambda \| \mathbf{w} \|_1
$$
where $CE(\mathbf{w})$ is a shorthand notation for the binary cross-entropy. It is now well known that using such a regularization of the loss function encourages the vector of parameters $\mathbf{w}$ to be sparse. The hyper-parameter $\lambda$ then **controls the trade-off between how sparse the model should be and how important it is to minimize the cross-entropy**. Although hyper-parameter optimization is a dedicated area of machine learning in itself and well beyond the scope of this post, let us finally mention that scikit-learn provides a simple heuristic based on grid-search and cross-validation to find good values for $\lambda$.

### Conclusion

Its simplicity and flexibility, both from a mathematical and computational point of view, makes logistic regression by far the most commonly used technique for binary classification in real-life applications. If you are a newcomer to machine learning, I hope you now have a better understanding of the mathematics it relies on and how it can be used in practice. Note that there is a lot we did not cover such as:

- the statistical interpretation of the model in term of odds ratios (or log-odds),
- how to quantify how accurate the predictions are (other than the fact that we minimized the cross-entropy on our training set) using various metrics and ROC or precision-recall curves.

These should however come in a second step after you have mastered the basics. Furthermore, there are plenty of resources online that address these extra points. Do not hesitate to go through them to gain even better insights! Do not hesitate also to derive all of the mathematical results presented herein yourself and to play with the codes provided!

**Additional online resources**

- Excellent video by Aurélien Géron ([here](https://www.youtube.com/watch?v=ErfnhcEV1O8)) providing an information-theoretic point of view of why it makes sense to use the cross-entropy for classification purposes.

### References

[^1]:[1] R. Yedida & S. Saha. LipschitzLR: Using theoretically computed adaptive learning rates for fast convergence. arXiv eprint 1902.07399, 2020.

https://towardsdatascience.com/binary-cross-entropy-and-logistic-regression-bf7098e75559