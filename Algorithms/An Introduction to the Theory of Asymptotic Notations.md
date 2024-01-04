# An Introduction to the Theory of Asymptotic Notations

## 1. Overview

In this tutorial, we’ll give an introduction to asymptotic notations, as well as show examples for each of them. **We’ll be discussing Big $\mathbf \Theta$ (Theta), Big $\mathbf \Omega$ (Omega), and Big O notations.**

## 2. Evaluating an Algorithm

In computer science and programming, developers often face code efficiency problems. **Asymptotic notations and especially the Big O notation help predict and reason about the efficiency of an algorithm.** This knowledge can also affect designing an algorithm based on its goal and desirable performance.

Imagine that we have some code that works on a small subset of data. In the nearest future, we’re expecting an increase in the data, and we need to analyze if our algorithm would be performant enough. Let’s imagine what the algorithm could look like in pseudocode:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/quicklatex.com-dbafc89b7e2d0239ba50a87c04f47026_l3.svg" alt="quicklatex.com-dbafc89b7e2d0239ba50a87c04f47026_l3"  />

The piece of code is quite simple. It just checks if an element is in the list. Let’s try to evaluate its performance. To do that, we need to find out how this algorithm will change if we change the size of our input.

**How can we approach measuring the efficiency and performance of this algorithm?** **We can use time, which can provide us with some understanding of the performance.** However, time will depend on the amount of data, the machine we’re running it on, and implementation details. Thus, it would not be helpful for us.

**We can count the number of steps require for this code to complete and try to base our judgment on this.** This approach will better show us the complexity of an algorithm. However, counting all the steps will depend heavily on the implementation. If we add a step, it will change the measurement of the complexity of an algorithm.

**The best approach is to consider that all the elements have the same time to be processed.** Let’s assume that we process an element in this list in one basic unit. Thus if we have an element that we’re looking for in the middle of the list, we’ll spend $n/2$ units of time.

In the best-case scenario, the element we’re looking for will be the first one, and we’ll check only the first one. In the worst case – this element won’t be there, and we’ll have to check all the elements in the list. **If the elements are distributed randomly, on average, we’ll need to go through half of the list to find the required element.**

## 3. Big O Notation

In the example above, the time we’ll spend on the search will depend on the location of the element we’re looking for. However, we can tell exactly how many elements we need to check for the worst-case scenario. **The Big O notation represents this worst-case scenario.**

### 3.1. Formal Definition

In essence, Big O notation defines a function that will always be greater than the result of its bounding function. As we’re interested only in the complexity of an algorithm, we can scale $g(x)$ by any constant.

**Definition:** $f(x) = O(g(x))$ means that there exist two positive constants, $x_1$ and $c$, such that $0 \le f(x) \le cg(x)$ for all $x \ge  x_1$.

### **3.2. Example**

Let’s assume that we have a piece of code that sorts some list, prints it, and then writes it to a file.

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/quicklatex.com-28c261ff27a3dc7c803a545d2e3093f0_l3.svg" alt="quicklatex.com-28c261ff27a3dc7c803a545d2e3093f0_l3"  />

**We can define the complexity of this algorithm. It will be a sum of several parts of the code in our case.** Bubble sort has $n^{2}$ complexity. Printing all the elements will have $n$. Writing to a file, we can assume as a constant time operation. We can assume that it will be 3. Therefore, the overall complexity of this piece of code will be:

$y = n^{2} + n + 3$

Visually, it’s represented by the graph below:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/qauratic-full-small-1.webp" alt="qauratic-full-small-1" style="zoom: 67%;" />

First of all, we should simplify the function. **We should drop all the lower order components as they won’t significantly change when n approaches big values.** For example, if we assume n as $10^{10}$, the equation will look like this:

$y = 10^{20} + 10^{10} + 3$

**The second and the third components will comprise a dramatically small part of the overall result.** Thus we can drop them. Sometimes, it’s hard to define the higher-order component in more complex functions. Reference [this](https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations) table in case of any doubts.

After simplification, we can reduce the function to $y = n^{2}$. Thus, the previous graph will change a bit, and the final version will be:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/quadratic-small-1.webp" alt="quadratic-small-1" style="zoom: 67%;" />

### **3.3. Big O Graphical Representation**

As we already defined, the Big O notation represents the worst-case scenario. It will be a function higher than our function from a specific $x$ to infinity.

Let’s make a faulty assumption and decide to use a linear function for Big O notation:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/small-comparison-with-linear-1.webp" alt="small-comparison-with-linear-1" style="zoom: 67%;" />

We compared our quadratic function with several linear: $x$, $2x$, $3x$, and $4x$. **However, because a quadratic function’s growth rate is greater than linear, it’s impossible to cap it with linear. Also, we used a constant multiplier for a function because we’re interested in the rate of growth which depends on the input.** A constant, in this case, won’t make any difference.

Before checking the right solution, we can try another one that won’t work. We can try to cap our current quadratic function with a cubic one:

$y = x^{3}$

We can see overlapping graphs below:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/small-quadratic-to-cubic-1.webp" alt="small-quadratic-to-cubic-1" style="zoom: 67%;" />

As we can observe, cubic function caps quadratic function from 1 to infinity. **We don’t care if the quadratic function, in this case, always has a higher value when $x < 1$.** Therefore, the cubic function completely fits the definition. **However, we also should consider the tightness of the function, and in this case, the cubic function overshoots a lot.** The comparison function should be as close to the given function as possible. Despite meeting all the requirements, we cannot use it to define complexity.

Let’s try to cap this function with a quadratic one:

$y = x^{2} * 1.2$

The red graph represents our initial function, and the blue one represents the comparison function:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/small-quadratic-big-o-1.webp" alt="small-quadratic-big-o-1" style="zoom:67%;" />

As we can see from the graph, the blue line representing our comparison function is always above our initial function. That’s why we can use this function for Big O notation. **We should drop the constant multiplier as we’re only interested in the growth rate, not a specific value.**

**Thus, the Big O of our initial code block will be $\mathbf O(n^{2})$.** In most cases, the Big O of an equation will be the highest order component with all the constant multipliers dropped.

**It is worth repeating that the comparison function should be as tight as possible to the function we want to estimate.**

## 4. Big $\mathbf \Omega$ (Omega)

After learning about Big O notation, Big $\Omega$ should be easier to grasp. **This asymptotic notation represents a lower bound of a given function.** It means the best-case scenario for a function or an algorithm. **However, considering that the function should be as tight as possible, we cannot go too optimistic.**

Let’s consider an example from the beginning:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/quicklatex.com-1e714ffe7e49c084a58e2802d5fbb9db_l3.svg" alt="quicklatex.com-1e714ffe7e49c084a58e2802d5fbb9db_l3"  />

The complexity of this function is quadratic and, after simplification, will look the same as in the first example:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/quadratic-small-1-168156685643827.webp" alt="quadratic-small-1" style="zoom:67%;" />

The best-case scenario is when all the elements are sorted already, and bubble sort will only go through the list once. Thus, we can assume that, theoretically, the best-case scenario will have linear complexity:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/quadratic-omega.webp" alt="quadratic-omega" style="zoom:67%;" />

However, as mentioned before, even though this comparison function meets all the criteria, it’s not tight enough. **We cannot assume that all the elements in a given list will be sorted in all the cases in real life.** That’s why we need to find a function that will be as tight as possible to the current one:

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/approaching-omega.webp" alt="approaching-omega" style="zoom:67%;" />

The correct Big $\mathbf \Omega$ for the given code will be of quadratic complexity, $\Omega(n)$.

## 5. Big $\mathbf \Theta$ (Theta)

**Big $\mathbf \Theta$ notation is the combination of both above.** For the Big $\mathbf \Theta$, we need to use the function that perfectly fits the given function. **To simplify, Big $\mathbf \Theta$ can be described as some function that, with the use of constant multipliers, can represent Big O and Big $\mathbf \Omega$ at the same time:**

<img src="An%20Introduction%20to%20the%20Theory%20of%20Asymptotic%20Notations.assets/big-theta-2.webp" alt="big-theta-2" style="zoom:67%;" />

Two quadratic functions with different constant multipliers (0.8 and 1.2, respectively) contain inside the given function. Thus, the Big $\mathbf \Theta$ will also be of quadratic complexity.

## **6. Conclusion**

**This article taught us about asymptotic notations and why they are essential and valuable in computer science. Even a basic understanding of their use can help create better software.**

These notations also help to think about algorithms in terms of efficiency and complexity. Even though modern machines’ hardware and computing power increased dramatically, so did the datasets these machines operate on. In most cases, it’s enough to concentrate on Big O notation for the accessing algorithms.

We can find [a more practical look at this topic implemented in Java](https://www.baeldung.com/java-algorithm-complexity) as well.

**References**

> https://www.baeldung.com/cs/big-o-notation