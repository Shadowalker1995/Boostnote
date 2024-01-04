# Q-Learning vs. Deep Q-Learning vs. Deep Q-Network

## 1. Introduction

<a href="./Reinforcement Learning with Neural Network.md" alt="Reinforcement Learning (RL)">Reinforcement Learning (RL)🔗</a>has recently received considerable attention due to its successful application in several fields, including game theory, operations research, <a href="../Machine-Learning/Combinatorial Optimization.md" alt="combinatorial optimization">combinatorial optimization🔗</a>, <a href="../Machine-Learning/Information Theory.md" alt="information theory">information theory🔗</a>, simulation-based optimization, control theory, and [statistics](https://www.baeldung.com/cs/ai-ml-statistics-data-mining).

In this tutorial, we’ll explore the concept of reinforcement learning, [Q-learning](https://www.baeldung.com/cs/q-learning-vs-sarsa), [deep Q-learning](https://www.baeldung.com/cs/reinforcement-learning-neural-network) vs. deep Q-network, and how they relate to each other.

## 2. Reinforcement Learning

Reinforcement learning (RL) is a subset of [machine learning](https://www.baeldung.com/cs/ml-fundamentals) in which an agent learns to obtain the best strategy for achieving its goals by interacting with the environment. Unlike supervised machine learning algorithms, which rely on ingesting and processing data, RL does not require data to learn. Instead, the agent learns from its interactions with the environment and the rewards it receives to make better decisions. In RL, the goal is to maximize the cumulative reward over time, and the agent learns through trial and error to select actions that lead to the highest rewards.

The below figure illustrates how the agent interacts with the environment in reinforcement learning:

<img src="Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/rl.webp" alt="rl" style="zoom:67%;" />

To illustrate, consider the Mario video game. If the game character takes a random action, such as moving left, it may receive a reward based on that action. After taking action, the game character (Mario) will be in a new state, and the process will repeat until Mario reaches the end of the stage or loses the game. This episode will repeat several times until Mario learns to navigate the environment by maximizing the rewards. Through this trial and error process, Mario will learn which actions lead to higher rewards and will adjust its strategy accordingly to achieve the goal of completing the level.

In brief, RL is the science of using experiences to make optimal decisions. The process involves the following simple steps:

- Observing the environment
- Making decisions on how to act using some strategy
- Executing the action
- Receiving a reward or penalty based on the action
- Learning from experiences and refining the strategy
- Repeating this iterative process until an optimal strategy is found

RL algorithms can be broadly categorized into two types: [**model-based and model-free**](https://www.baeldung.com/cs/ai-model-free-vs-model-based).

**A model-based algorithm estimates the optimal policy using the transition and reward functions**. In other words, it learns a model of the environment’s dynamics and uses it to predict future states and rewards.

**On the other hand, a model-free algorithm does not use or estimate the environment’s dynamics**. Instead, it directly estimates the optimal policy through trial and error, using the rewards received from the environment to guide its decisions. This makes model-free algorithms more suitable for environments with complex dynamics where it is difficult to model the environment accurately.

## 3. Q-Learning

### 3.1. What is Q-Learning

**Q-learning is a model-free, value-based, [off-policy](https://www.baeldung.com/cs/off-policy-vs-on-policy) algorithm that is used to find the [optimal policy](https://www.baeldung.com/cs/ml-value-iteration-vs-policy-iteration) for an agent in a given environment**. The algorithm determines the best series of actions to take based on the agent’s current state. The “Q” in Q-learning stands for quality, representing how valuable action maximizes future rewards.

**As a model-based algorithm, Q-learning does not require knowledge of the transition and reward functions**. It directly estimates the optimal policy through trial and error, using the rewards received from the environment to guide its decisions. The algorithm updates the Q-values based on the reward received for a particular (state, action) pair and the estimated value of the next state. By repeatedly updating the Q-values based on the observed rewards, Q-learning can converge to an optimal policy that maximizes the cumulative reward over time.

**As a value-based algorithm, Q-learning trains the value function to learn which actions are more valuable in each state and select the optimal action accordingly**. The value function is updated iteratively based on the rewards received from the environment, and through this process, the algorithm can converge to an optimal policy that maximizes the cumulative reward over time.

**As an off-policy algorithm, Q-learning evaluates and updates a policy that differs from the policy used to take action**. Specifically, Q-learning uses an epsilon-greedy policy, where the agent selects the action with the highest Q-value with probability 1-epsilon and selects a random action with probability epsilon. This exploration strategy ensures that the agent explores the environment and discovers new (state, action) pairs that may lead to higher rewards.

The Q-values are updated based on the rewards received for the action taken, even if it is not the optimal action according to the current policy. By updating the Q-values based on the highest Q-value action in each state, Q-learning can converge to the optimal policy even if it is different from the policy used to take actions during training.

### 3.2. How Q-Learning Works

As the agent exposes itself to the environment and receives different rewards by executing different actions, the values are updated per the following equation:
$$
Q_{new}(s,a)=Q(s,a)+\alpha(R(s,a)+\gamma\max_a Q^\prime (s^\prime,a^\prime)-Q(s,a))
$$
where $Q(s,a)$ is the current Q-value, $Q_{new}(s,a)$ is the update value, $\alpha$ is the learning rate, $R(s,a)$ is the reward, $\gamma$ is a number between $[0,1]$ and is used to discount the reward as the time passes, given the assumption that action in the beginning, is more important than at the end (an assumption that is confirmed by many real-life use cases).

In its simplest form, Q-values is a table (or matrix) with states as rows and actions as columns. The Q-table is initialized randomly, and the agent starts to interact with the environment and measures the reward for each action. It then computes the observed Q-values and updates the Q-table. The following pseudocode summarizes how Q-learning works:

<img src="Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/quicklatex.com-38616f4956479e09d6fb84afc49e6a42_l3.svg" alt="quicklatex.com-38616f4956479e09d6fb84afc49e6a42_l3"  />

### 3.3. Example

Let’s see a simple example below to see how Q-learning works. Our agent is a rat that has to cross a maze and reach the end (its house) point. There are mines in the maze, and the rat can only move one tile (from one square to one another) at a time. If the rat steps onto a mine, it will be dead. The rat wants to reach its home in the shortest time possible:

<img src="Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/rat-maze.webp" alt="rat-maze" style="zoom:50%;" />

The reward system is as below:

- The rat loses 1 point at each step. This is done so that the rat should take the shortest path and reach its home as fast as possible
- If the rat steps on a mine, it loses 100 points, and the game is over
- If the rat gets power (the yellow lightning icon), it gains 1 point
- If the rat reaches its home, it is rewarded 100 points

The rat has four possible actions at each non-edge tile: $(\uparrow,\downarrow,\leftarrow,\rightarrow)$ (move up, down, right, or left). The state is the position of the rat in the maze.

Having all this information, we can initialize the Q-table as a matrix of size $5\times4$, where the rows represent the rat’s possible states (positions), and the columns represent the possible actions (moving in 4 directions). Initially, our rat knows nothing about the environment (maze), so it will choose a random action, say our robot knows nothing about the environment. So the robot chooses a random action, say right:

<img src="Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/rat-maze_step1.webp" alt="rat-maze_step1" style="zoom:50%;" />

Using the Bellman equation, we can now update the Q-values for being at the start and moving right. We will repeat this again and again until the learning is stopped. In this way, the Q-table will be updated. For instance, the next Q-table corresponding to the current position of the rat looks like this:

<img src="Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/rat-maze_step2.webp" alt="rat-maze_step2" style="zoom:50%;" />

## 4. Deep Q-Learning and Deep Q-Network

**One of the main drawbacks of Q-learning is that it becomes infeasible when dealing with large state spaces, as the size of the Q-table grows exponentially with the number of states and actions**. In such cases, the algorithm becomes computationally expensive and requires a lot of memory to store the Q-values. Imagine a game with 1000 states and 1000 actions per state. We would need a table of one million cells. And that is a very small state space compared to chess or Go. Also, Q-learning can’t be used in unknown states because it can’t infer the Q-value of new states from the previous ones. This presents two problems:

First, the amount of memory required to save and update that table would increase as the number of states increases.

Second, the amount of time required to explore each state to create the required Q-table would be unrealistic.

To tackle this challenge, one alternative approach is to combine Q-learning with [deep neural networks](https://www.baeldung.com/cs/deep-cnn-design). This approach is coined as [Deep Q-Learning (DQL)](https://www.baeldung.com/cs/q-learning-vs-dynamic-programming). The neural networks in DQL act as the Q-value approximator for each (state, action) pair.

**The neural network receives the state as an input and outputs the Q-values for all possible actions**. The following figure illustrates the difference between Q-learning and deep Q-learning in evaluating the Q-value:

<img src="Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/dql-vs-ql-1.webp" alt="dql-vs-ql-1" style="zoom:67%;" />

**Essentially, deep Q-Learning replaces the regular Q-table with the neural network**. Rather than mapping a (state, action) pair to a Q-value, the neural network maps input states to (action, Q-value) pairs.

In 2013, [DeepMind introduced Deep Q-Network (DQN) algorithm](https://arxiv.org/abs/1312.5602). DQN is designed to learn to play Atari games from raw pixels. This was a breakthrough in the field of reinforcement learning and helped pave the way for future developments in the field. **The term Deep Q-network refers to the neural network in their DQL architecture**.

### 4.1. How Deep Q-Learning Works

Here are the steps of how DQN works:

- **Environment**: DQN interacts with an environment with a state, an action space, and a reward function. The goal of the DQN is to learn the optimal policy that maximizes cumulative rewards over time
- **Replay Memory**: DQN uses a replay memory buffer to store past experiences. Each experience is a tuple (state, action, reward, next state) representing a single transition from one state to another. The replay memory stores these experiences to sample from later randomly
- **Deep Neural Network**: DQN uses a deep neural network to estimate the Q-values for each (state, action) pair. The neural network takes the state as input and outputs the Q-value for each action. The network is trained to minimize the difference between the predicted and target Q-values
- **Epsilon-Greedy Exploration**: DQN uses an [epsilon-greedy exploration strategy](https://www.baeldung.com/cs/epsilon-greedy-q-learning) to balance exploration and exploitation. During training, the agent selects a random action with probability epsilon and selects the action with the highest Q-value with probability (1 – epsilon)
- **Target Network**: DQN uses a separate target network to estimate the target Q-values. The target network is a copy of the main neural network with fixed parameters. The target network is updated periodically to prevent the overestimation of Q-values
- **Training**: DQN trains the neural network using the Bellman equation to estimate the optimal Q-values. The loss function is the mean squared error between the predicted and target values. The target Q-value is calculated using the target network and the Bellman equation. The neural network weights are updated using backpropagation and stochastic gradient descent
- **Testing**: DQN uses the learned policy to make environmental decisions after training. The agent selects the action with the highest Q-value for a given state

In summary, DQN learns the optimal policy by using a deep neural network to estimate the Q-values, a replay memory buffer to store past experiences, and a target network to prevent overestimating Q-values. The agent uses an epsilon-greedy exploration strategy during training and selects the action with the highest Q-value during testing.

## 5. Summarized Differences Between Q-Learning, Deep Q-Learning, and Deep Q-Network

The below table outlines the differences between Q-learning, Deep Q-learning, and Deep Q-network:

![quicklatex.com-d27e1a72e0ad4607225e9fd22602f7ae_l3](Q-Learning%20vs.%20Deep%20Q-Learning%20vs.%20Deep%20Q-Network.assets/quicklatex.com-d27e1a72e0ad4607225e9fd22602f7ae_l3.svg)

## 6. Conclusion

In this brief article, we explored an overview of reinforcement learning, including its definition and purpose. Additionally, we delved into the details of some significant reinforcement learning algorithms, namely Q-learning, Deep Q-learning, and Deep Q-network, outlining their fundamental concepts and roles in the decision-making process.

**References**

> https://www.baeldung.com/cs/q-learning-vs-deep-q-learning-vs-deep-q-network