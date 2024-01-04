# What is the Difference Between Artificial Intelligence, Machine Learning, Statistics, and Data Mining?

## 1. Introduction

In this tutorial, we’ll talk about the differences between artificial intelligence, [machine learning](https://www.baeldung.com/cs/ml-fundamentals), statistics, and data mining.

There’s a significant overlap between those fields and no clear way to separate them. Over the years, researchers and engineers have articulated different and often conflicting opinions about this question, so **there is no consensus**.

## 2. Artificial Intelligence

Let’s start with artificial intelligence (AI). In general, **the goal of AI is to build agents that can solve the problems we put before them on their own, as if they have innate intelligence like humans**. What makes this field so rich is the abundance of ways to define and construct the agents.

For example, handwriting recognition software is an AI agent since it can read handwritten texts and convert them to a digital format without human help. It learns that ability from machine-readable images of handwritten digits and letters.

Another example is a chess-playing program. It plays chess by searching for the best possible sequence of moves considering what its opponent may play. The intelligence of such an AI agent doesn’t come from the data. Instead, it stems from [how the agent searches for the best move](https://www.baeldung.com/cs/minimax-algorithm).

There are other examples, such as sudoku solvers and airport flight schedules. The notion of an intelligent agent is at the center of them all. More precisely, we say that **AI builds rational agents**. Here, **rationality means consistently choosing the best available option given what we know about all the alternatives**: determining the word that best fits the handwriting, the move that will lead to winning a chess game the fastest, the flight schedule with the minimal waiting time, etc.

## 3. Machine Learning

Machine learning (ML) is a subfield of AI. Stepping back from the general AI terminology for a moment, we’d say that **ML applies learning algorithms to datasets to get automated rules for predicting new data**.

For instance, we may be interested in predicting the sale price of an apartment based. We have the data on various flats’ features (such as the size in square feet) and their final sale prices. Inducing a quality prediction rule from the dataset is a job for ML. Those rules may take different forms, such as [trees](https://www.baeldung.com/cs/decision-tree-vs-naive-bayes), math equations in [linear regression](https://www.baeldung.com/cs/linear-vs-logistic-regression), or [neural networks](https://www.baeldung.com/cs/svm-vs-neural-network). So instead of working out the rules by hand, we use ML to extract them automatically.

But, given what we know about AI, we see that finding the ML rules falls under constructing AI agents. For example, we may restrict the price prediction rules to the equations of the form:

$$
\begin{equation*}
\theta_0 + \theta_1 \cdot size + \theta_2\cdot(number \ of \ rooms) + \theta_3 \cdot floor \tag 1 \label{1}
\end{equation*}
$$

Our goal is to discover the most accurate one. That’s the same as building an AI agent that, of all the prices it can predict using equation $\eqref{1}$, outputs the one that is the most likely to be true. So, **ML is a part of AI which builds the agents from data using the algorithms specialized for that**.

## 4. Statistics

Unlike its relationship with AI, ML’s relationship with statistics is highly controversial. Many researchers, statisticians especially, would argue that ML is just a rebranded statistic. That argument is not without its merits. But, there are many researchers with a contesting view. To see why let’s first (try to) define statistics.

### 4.1. What Is Statistics?

**Most people would describe statistics as the branch of mathematics for making inferences about a population using only a sample**.

For example, we may want to discover the average height of teenagers in the USA. It would be impractical to measure all American teenagers. Instead, we could randomly select a few schools across the country and measure ten teenagers per school. That way, we’d get a sample of heights, the average of which informs us about the whole teenage population’s mean.

Similarly, we may be interested to see how temperature affects an industrial process or how the number of rooms in a flat influences its sale price.

Statistics develops the methods for answering such questions. In doing so, it is highly formal. All its tools, such as hypothesis testing and descriptive statistics, come with mathematical proofs of performance. For instance, we know that the $95\%$ confidence intervals we construct around the sample means are guaranteed to capture the actual population mean $95\%$ of the time. Such proofs, however, rely on assumptions that may not hold in reality. For example, common assumptions are statistical independence of the sample elements and normality of data.

### 4.2. Why Machine Learning Is Statistics?

The researchers in favor of this view argue that inducing a prediction rule (of any form) from data is nothing else than making an inference about the process producing those data. For instance, the equation ML gives us to predict flat prices is also an inference about the general rule that the whole “population” of apartments follows on sale. Likewise, inferring a general rule about a data generating process in statistics allows predicting new data.

In support of this argument, people also say that some core ML models like [linear regression](https://www.baeldung.com/cs/linear-vs-logistic-regression) were initially developed and researched in statistics. They go a step further and assert that all ML models are statistical tools. The only difference is that the former are less interpretable and computationally more demanding. Even more so, some researchers voice the concern that ML is statistics done wrong. The reason is that automated modeling lacks proper rigor possible only through human involvement.

### 4.3. Why Machine Learning Is Not Statistics?

But, many ML researchers would strongly oppose those claims. They would argue that **the focus on prediction makes ML different from statistics**. Most of the time, especially in industry, performance metrics are all that counts. So, a deep neural network with hundreds of inner layers is a perfectly acceptable ML product if its predictions are accurate even though, by itself, it isn’t interpretable and doesn’t allow for any inference. On the other hand, a statistician would be very uncomfortable using a black-box model like that.

Further, since ML focuses on predictive performance, it validates its models on held-out test data to check their generalization capabilities. Statistics, however, don’t split samples into [training and test sets](https://www.baeldung.com/cs/train-test-datasets-ratio).

Additionally, it seems that **ML pays attention to the engineering and computational aspects of training its models and handling large datasets much more than statistics**. The reason is that statisticians developed their tools to work on small samples precisely to avoid dealing with large amounts of data. In contrast, ML tools originated from the computer science and AI fields, so the scientists considered the algorithmic and their implementation aspects from the start. As a result, the ML methodology replaced the statistical one as it solved the tasks that traditional statistics couldn’t tackle.

An interesting argument is that **the research cultures of ML scientists and statisticians differ**. Extensive theoretical results accompany all statistical methods. For instance, it’s impossible to publish a paper about a new statistical test without theorems and proofs. The empirical evaluation alone wouldn’t cut it. In contrast, ML researchers and practitioners would show interest in a method with good results on real-world data even though there may be gaps in its theory.

### 4.4. Example

Finally, **although we can use ML and statistics for both prediction and inference, their methodologies differ**. ML isn’t just reworded statistics done wrong. It employs a different modeling approach.

For example, let’s say that a dataset contains the sizes (in square feet) and sale prices of ten apartments:

<img src="What%20is%20the%20Difference%20Between%20Artificial%20Intelligence,%20Machine%20Learning,%20Statistics,%20and%20Data%20Mining.assets/data.webp" alt="data" style="zoom: 50%;" />

To fit a linear model $\theta_0 + \theta_1 \cdot size$, an ML scientist would divide the set into training (blue) and test (red) data and minimize the [loss](https://www.baeldung.com/cs/cost-vs-loss-vs-objective-function) over the former:

<img src="What%20is%20the%20Difference%20Between%20Artificial%20Intelligence,%20Machine%20Learning,%20Statistics,%20and%20Data%20Mining.assets/machine_learning.jpg" alt="machine_learning" style="zoom: 50%;" />

Then, the s(he) would evaluate the model on the three test data. If the errors are negligible and not that different from those on the training data, the scientist would consider it a good model for predicting the price based on the apartment size.

In contrast, a statistician would fit $\theta_0 + \theta_1 \cdot size$ to the whole dataset (probably obtaining different coefficients):

<img src="What%20is%20the%20Difference%20Between%20Artificial%20Intelligence,%20Machine%20Learning,%20Statistics,%20and%20Data%20Mining.assets/statistics.jpg" alt="statistics" style="zoom:50%;" />

But, s(he) wouldn’t use it for prediction. Instead, s(he) would test the hypothesis that the size affects the sale price by checking the significance of the coefficient $\theta_1$.

This example may present an overly simplistic view of the two disciplines in practice but illustrates the difference between the approaches.

## 5. Data Mining

[Data mining](https://www.baeldung.com/cs/weka-data-mining) grew out of database management in commercial applications. **Its goal is to discover valuable patterns in [big data](https://www.baeldung.com/cs/big-data-vs-data-mining) and provide business stakeholders with actionable information**. Let’s illustrate that with an example.

**References**

> https://www.baeldung.com/cs/ai-ml-statistics-data-mining