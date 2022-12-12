# Deep Learning meets Physics: Restricted Boltzmann Machines Part II

> Build your own Restricted Boltzmann Machine

> This article is the sequel of the first part which introduced the theory behind Restricted Boltzmann Machines. This second part consists in a step by step guide through a practical implementation of a Restricted Boltzmann Machine which serves as a Recommender System and can predict whether a user would like a movie or not based on the users taste.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1_9HZMP0Nkc0OkiW7ryfS3gw.png" style="zoom: 50%;" />

[toc]

## 0. Prerequisites

- Python 3.6
- TensorFlow 1.5 or higher
- NumPy 1.11 or higher

## 1. Dataset

We are using the [MovieLens 1M Dataset](https://grouplens.org/datasets/movielens/). This set contains 1 million ratings of approximately 4000 movies made by approximately 6000 users. The model will be trained on this dataset and will learn to make predictions whether a user would like a random movie or not. The dataset requires some reprocessing steps. Because an usual Restricted Boltzmann Machine accepts only binary values it is necessary to give ratings 1–2 a value of 0 — hence the user does not like the movie. Accordingly the ratings 3–5 receive a value of 1. The movies that are not rated yet receive a value of -1.

In the next step the transformed original data is divided into two separate training and test datasets. It is necessary two have exactly the same users in both datasets but different movie ratings. Fig. 1 shows a simple example for the partitioning of the original dataset into the training and test data. In this example the first 5 ratings are put into the training set, while the rest is masked with -1 as not rated yet. Accordingly the test set receives the remaining 5 ratings.

During the training time the Restricted Boltzmann Machine learns on the first 5 movie ratings of each user, while during the inference time the model tries to predict the ratings for the last 5 movies. These predicted ratings are then compared with the actual ratings which were put into the test set.

Both datasets are saved in a binary **TFRecords** format that enables a very efficient data input pipeline.

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1_7HtJjWXu8WJ4OApcC5ROIw.png" style="zoom:50%;" />

<center style="color:#C0C0C0;">Fig. 1. Partitioning of the data into training and test datasets.</center>

## 2. Model Architecture

The model is implemented in an object oriented manner. The Restricted Boltzmann Machine is a class with all necessary operations like training, loss, accuracy, inference etc. inside of it. Some helper functions are outsourced into a separate script.

The constructor sets the kernel initializers for the weights and biases. In the next step all weights and biases in the network get initialized. The weights are normal distributed with a mean of 0.0 and a variance of 0.02, while the biases are all set to 0.0 in the beginning. It can be noticed that the network consists only out of one hidden layer. As a result only one weight matrix is needed.

`boltzmann_model_def.py`:

```python
class RBM:
    ''' Implementation of the Restricted Boltzmann Machine for collaborative filtering. The model is based on the paper of 
        Ruslan Salakhutdinov, Andriy Mnih and Geoffrey Hinton: https://www.cs.toronto.edu/~rsalakhu/papers/rbmcf.pdf
    '''
    def __init__(self, FLAGS):
        '''Initialization of the model  '''
        self.FLAGS=FLAGS
        self.weight_initializer=model_helper._get_weight_init()
        self.bias_initializer=model_helper._get_bias_init()
        self.init_parameter()


    def init_parameter(self):
        ''' Initializes the weights and the bias parameters of the neural network.'''
        with tf.variable_scope('Network_parameter'):
            self.W=tf.get_variable('Weights', shape=(self.FLAGS.num_v, self.FLAGS.num_h),initializer=self.weight_initializer)
            self.bh=tf.get_variable('hidden_bias', shape=(self.FLAGS.num_h), initializer=self.bias_initializer)
            self.bv=tf.get_variable('visible_bias', shape=(self.FLAGS.num_v), initializer=self.bias_initializer)
```

## 3. Sampling of the Hidden States

$$
p(h_j=1 | \mathbf{v}) = \frac{1}{a + e^{(-(b_j + W_j v_j))}} = \sigma(b_j + \sum_i v_i w_{ij})
$$

<center style="color:#C0C0C0;">Eq. 1. Probability that a hidden neuron is activated.</center>

Giving the binary input $\mathbf{v}$ the following function `_sample_h(self) `obtains the probabilities that a hidden neuron is activated (Eq.1). This is achieved by multiplying the input $\mathbf{v}$ by the weight matrix, adding a bias and applying a sigmoid activation . The obtained probabilities are used to sample from Bernoulli distribution. The sampled values which are either 1.0 or 0.0 are the states of the hidden neurons.

`boltzmann_sample_h.py`:

```python
def _sample_h(self, v):
        ''' Uses the visible nodes for calculation of  the probabilities that a hidden neuron is activated. 
        After that Bernouille distribution is used to sample the hidden nodes.
        
        @param v: visible nodes
        @return probability that a hidden neuron is activated
        @return sampled hidden neurons (value 1 or 0 accroding to Bernouille distribution)
        '''
        with tf.name_scope('sampling_hidden_units'):
            a=tf.nn.bias_add(tf.matmul(v,self.W), self.bh)
            p_h_v=tf.nn.sigmoid(a)
            h_=self._bernouille_sampling(p_h_v, shape=[self.FLAGS.batch_size, int(p_h_v.shape[-1])])

            return p_h_v, h_


def _bernouille_sampling(self,p, shape):
        '''Samples from the Bernoulli distribution
        
        @param p: probability 
        @return samples from Bernoulli distribution
        '''
        return tf.where(tf.less(p, tf.random_uniform(shape,minval=0.0,maxval=1.0)),
                        x=tf.zeros_like(p),
                        y=tf.ones_like(p))
```

## 4. Sampling of the Visible States

$$
p(v_i=1 | \mathbf{h}) = \frac{1}{1 + e^{(-(a_i + W_i h_j))}} = \sigma(a_i + \sum_j h_j w_{ij})
$$

<center style="color:#C0C0C0;">Eq. 2. Probability that a visible neuron is activated.</center>

Given the hidden states $\mathbf{h}$ we can use these to obtain the probabilities that a visible neuron is active (Eq.2) as well as the corresponding state values. This is implemented in `_sample_v(self)` .

`boltzmann_sample_v.py`:

```python
def _sample_v(self, h):
        ''' Uses the hidden nodes for calculation of  the probabilities that a visible neuron is activated. 
        After that Bernouille distribution is used to sample the visible nodes.
        
        @param h: hidden nodes
        @return probability that a visible neuron is activated
        @return sampled visible neurons (value 1 or 0 accroding to Bernouille distribution)
        '''
        with tf.name_scope('sampling_visible_units'):
            a=tf.nn.bias_add(tf.matmul(h,tf.transpose(self.W, [1,0])), self.bv)
            p_v_h=tf.nn.sigmoid(a)
            v_=self._bernouille_sampling(p_v_h, shape=[self.FLAGS.batch_size, int(p_v_h.shape[-1])])

            return p_v_h, v_
```

## 5. Gibbs Sampling

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/1_UMbNSJVSmAgqkVnQKA62yg.png" style="zoom:50%;" />

<center style="color:#C0C0C0;">Fig.2. Gibbs Sampling.</center>

The first part of the training consists in an operation that is called **Gibbs Sampling**. Briefly speaking we take an input vector $\mathbf{v}_0$ and use it to predict the values of the hidden state $\mathbf{h}_0$. The hidden state are used on the other hand to predict new input state $\mathbf{v}$. This procedure is repeated $k$ times. This procedure is illustrated in Fig. 2.

Gibbs Sampling is implemented in the code snipped below. The iteration is happening in the while loop body. An important step in the body is `vk=tf.where(tf.less(V,0),V,Vk)`. **This operations makes sure that the ratings in $\mathbf{v}$ which are -1 (meaning movies that have not been seen yet) remain -1 for every $\mathbf{v}_k$ in every iteration.** After $k$ iteration we obtain $\mathbf{v}_k$ and corresponding probabilities $p(\mathbf{h}_k|\mathbf{v}_k)$. Together with $\mathbf{v}_0$ and $\mathbf{h}_0$ these values can be used to compute the gradient matrix in the next training step.

`boltzmann_gibbs.py`:

```python
def _gibbs_sampling(self, v):
        ''' Performing the Gibbs Sampling.
        
        @param v: visible neurons
        @return visible neurons before gibbs sampling
        @return visible neurons after gibbs sampling
        @return probability that hidden neurons are activated before gibbs sampling.
        @return probability that hidden neurons are activated after gibbs sampling.
        '''
        #end condition for the while loop
        def condition(i, vk, hk, v):
            r= tf.less(i,k)
            return r[0]

        #loop body
        def body(i, vk, hk, v):
            _,hk=self._sample_h(vk)
            _,vk=self._sample_v(hk)

            vk=tf.where(tf.less(v,0),v,vk)

            return [i+1, vk, hk,v]

        ph0, _=self._sample_h(v)

        vk=v
        hk=tf.zeros_like(ph0)

        i = 0 # start counter for the while loop
        k=tf.constant([self.FLAGS.k]) # number for the end condition of the while loop

        [i, vk, hk, v]=tf.while_loop(condition, body,[i, vk,hk,v])

        phk, _=self._sample_h(vk)

        return v, vk, ph0, phk, i
```

## 6. Computing the Gradients

The values obtained in the previous step can be used to compute the gradient matrix and the gradient vectors. The computation of gradients according to Eq. 3 are straight forward. Please notice that the symbols $a$ and $b$ in this equations stand for hidden respectively visible biases in contrasts to different symbols I used in my code.

The only tricky part is that TensorFlow 1.5 does not support outer products. But this issue can be solved by temporary reshaping and applying usual point wise multiplication.
$$
\Delta W = \mathbf{v}_0 \otimes p(\mathbf{h}_0 | \mathbf{v}_0) - \mathbf{v}_k \otimes p(\mathbf{h}_k | \mathbf{v}_k) \\
\Delta b = p(\mathbf{h}_0 | \mathbf{v}_0) - p(\mathbf{h}_k | \mathbf{v}_k) \\
\Delta a = \mathbf{v}_0 - \mathbf{v}_k
$$

<center style="color:#C0C0C0;">Eq. 3. Computation of gradients for the weights and biases.</center>

Notice that the computation of the gradients is happening in while loop. This is only due to the fact that the training is happening in mini-batches. Meaning the loop computes for each data sample in the mini-batch the gradients and adds them to the previously defined gradient placeholders. In the end the sum of gradients is divided by the size of the mini-batch.

`boltzmann_gradients.py`:

```python
def _compute_gradients(self, v0, vk, ph0, phk):
        ''' Computing the gradients of the weights and bias terms with Contrastive Divergence.
        
        @param v0: visible neurons before gibbs sampling
        @param vk: visible neurons after gibbs sampling
        @param ph0: probability that hidden neurons are activated before gibbs sampling.
        @param phk: probability that hidden neurons are activated after gibbs sampling.
        
        @return gradients of the network parameters
        '''

        #end condition for the while loop
        def condition(i, v0, vk, ph0, phk, dW, db_h, db_v):
            r=tf.less(i,k)
            return r[0]

        #loop body
        def body(i, v0, vk, ph0, phk, dW, dbh, dbv):
            v0_=v0[i]
            ph0_=ph0[i]

            vk_=vk[i]
            phk_=phk[i]       

            #reshaping for making the outer product possible
            ph0_=tf.reshape(ph0_, [1,self.FLAGS.num_h])
            v0_=tf.reshape(v0_, [self.FLAGS.num_v,1])
            phk_=tf.reshape(phk_, [1,self.FLAGS.num_h])
            vk_=tf.reshape(vk_, [self.FLAGS.num_v,1])

            #calculating the gradients for weights 
            dw_=tf.subtract(tf.multiply(ph0_, v0_),tf.multiply(phk_, vk_))
            #calculating the gradients for hidden bias
            dbh_=tf.subtract(ph0_,phk_)
            #calculating the gradients for visible bias
            dbv_=tf.subtract(v0_,vk_)

            dbh_=tf.reshape(dbh_,[self.FLAGS.num_h])
            dbv_=tf.reshape(dbv_,[self.FLAGS.num_v])

            # add the computed gradients to previosly computed gradients
            return [i+1, v0, vk, ph0, phk, tf.add(dW,dw_), tf.add(dbh,dbh_), tf.add(dbv,dbv_)]

        i = 0 # start counter for the while loop
        k=tf.constant([self.FLAGS.batch_size]) # number for the end condition of the while loop

        #init empty placeholders wherer the gradients will be stored              
        dW=tf.zeros((self.FLAGS.num_v, self.FLAGS.num_h))
        dbh=tf.zeros((self.FLAGS.num_h))
        dbv=tf.zeros((self.FLAGS.num_v))

        #iterate over the batch and compute for each sample a gradient
        [i, v0, vk, ph0, phk, dW,db_h,db_v]=tf.while_loop(condition, body,[i, v0, vk, ph0, phk, dW,dbh,dbv])

        #devide the summed gradients by the batch size
        dW=tf.div(dW, self.FLAGS.batch_size)
        dbh=tf.div(dbh, self.FLAGS.batch_size)
        dbv=tf.div(dbv, self.FLAGS.batch_size)

        return dW,dbh,dbv
```

## 7. Update Step

After the gradients are computed all weights and biases can be updated through gradient ascent according to eq. 4. For this procedure we must create an assign operation in `_update_parameter(self).`
$$
W_{new} = W_{old} + \Delta W \\
a_{new} = a_{old} + \Delta a
b_{new} = b_{old} + \Delta b
$$

<center style="color:#C0C0C0;">Eq. 4. Update step of the parameters through gradient ascent.</center>

The whole training operation is computed in `optimize(self)` method under the name scope "operation". Below that the more complicated accuracy operation of the training is implemented. Basically this operation subtracts the original input values $\mathbf{v}_0$ from $\mathbf{v}_k$ that are obtained during Gibbs Sampling. The subtraction is only happening for $\mathbf{v}_0$ ≥ 0. After that the summed subtractions are divided by the number of all ratings ≥ 0. The accuracy gives the ratio of correctly predicted binary movie ratings during training.

`boltzmann_update.py`:

```python
def optimize(self, v):
        ''' Optimization step. Gibbs sampling, calculating of gradients and doing an update operation.
        
        @param v: visible nodes
        @return update operation
        @return accuracy
        '''

        with tf.name_scope('optimization'):
            v0, vk,ph0, phk, _=self._gibbs_sampling(v)
            dW,db_h,db_v=self._compute_gradients(v0, vk, ph0, phk)
            update_op =self._update_parameter(dW,db_h,db_v)

        with tf.name_scope('accuracy'):
            mask=tf.where(tf.less(v0,0.0),x=tf.zeros_like(v0),y=tf.ones_like(v0))
            bool_mask=tf.cast(tf.where(tf.less(v0,0.0),x=tf.zeros_like(v0),y=tf.ones_like(v0)), dtype=tf.bool)
            acc=tf.where(bool_mask,x=tf.abs(tf.subtract(v0,vk)),y=tf.zeros_like(v0))
            n_values=tf.reduce_sum(mask)
            acc=tf.subtract(1.0,tf.div(tf.reduce_sum(acc), n_values))

        return update_op, acc

def _update_parameter(self,dW,db_h,db_v):
        ''' Creating TF assign operations. Updated weight and bias values are replacing old parameter values.
        
        @return assign operations
        '''

        alpha=self.FLAGS.learning_rate

        update_op=[tf.assign(self.W, alpha*tf.add(self.W,dW)),
                   tf.assign(self.bh, alpha*tf.add(self.bh,db_h)),
                   tf.assign(self.bv, alpha*tf.add(self.bv,db_v))]

        return update_op
```

## 8. Inference

During inference time the method `inference(self, v)` receives the input $\mathbf{v}$. That input is one **training** sample of a specific user that is used to activate the hidden neurons (the underlying features of users movie taste). The hidden neurons are used again to predict a new input $\mathbf{v}$. In the best scenario this new input consists of the recreation of already present ratings as well as ratings of movies that were not rated yet.

The made prediction are compared outside the TensorFlow Session with the according test data for validation purposes.

`boltzmann_inference.py`:

```python
def inference(self, v):
        '''Inference step. Training samples are used to activate the hidden neurons which are used for calculation of input neuron values.
        This new input values are the prediction, for already rated movies as well as not yet rated movies
        @param v: visible nodes
        @return sampled visible neurons (value 1 or 0 accroding to Bernouille distribution)
        '''
        p_h_v=tf.nn.sigmoid(tf.nn.bias_add(tf.matmul(v,self.W), self.bh))
        h_=self._bernouille_sampling(p_h_v, shape=[1,int(p_h_v.shape[-1])])

        p_v_h=tf.nn.sigmoid(tf.nn.bias_add(tf.matmul(h_,tf.transpose(self.W, [1,0])), self.bv))
        v_=self._bernouille_sampling(p_v_h, shape=[1,int(p_v_h.shape[-1])])

        return v_
```

## 9. The Network Graph

To outline the previous steps here is the definition of the main network graph and the start of the session where the training and inference steps are executed.

`boltzmann_networkgraph.py`:

```python
def main(_):
    '''Building the graph, opening of a session and starting the training od the neural network.'''

    num_batches=int(FLAGS.num_samples/FLAGS.batch_size)

    with tf.Graph().as_default():
        # get the training data for training and inference time
        train_data, train_data_infer=_get_training_data(FLAGS)
        # get the test data for inference
        test_data=_get_test_data(FLAGS)

        # make iterators
        iter_train = train_data.make_initializable_iterator()
        iter_train_infer = train_data_infer.make_initializable_iterator()
        iter_test = test_data.make_initializable_iterator()

        x_train= iter_train.get_next()
        x_train_infer=iter_train_infer.get_next()
        x_test=iter_test.get_next()

        # buid the model operations
        model=RBM(FLAGS)
        update_op, accuracy=model.optimize(x_train)
        v_infer=model.inference(x_train_infer)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            for epoch in range(FLAGS.num_epoch):
                acc_train=0
                acc_infer=0

                sess.run(iter_train.initializer)

                # training 
                for batch_nr in range(num_batches):

                    # run the update and accuracy operation
                    _, acc=sess.run((update_op, accuracy))
                    acc_train+=acc

                    # validation
                    if batch_nr>0 and batch_nr%FLAGS.eval_after==0:

                        sess.run(iter_train_infer.initializer)
                        sess.run(iter_test.initializer)

                        num_valid_batches=0

                        for i in range(FLAGS.num_samples):

                            v_target=sess.run(x_test)[0]

                            if len(v_target[v_target>=0])>0:

                                # make an prediction
                                v_=sess.run(v_infer)[0]
                                # predict this prediction with the target fro the test ste.
                                acc=1.0-np.mean(np.abs(v_[v_target>=0]-v_target[v_target>=0]))
                                acc_infer+=acc
                                num_valid_batches+=1

                        print('epoch_nr: %i, batch: %i/%i, acc_train: %.3f, acc_test: %.3f'%
                              (epoch, batch_nr, num_batches, (acc_train/FLAGS.eval_after), (acc_infer/num_valid_batches)))

                        acc_train=0
                        acc_infer=0
```

## 10. Performance of the Model

During the training process we can examine the progress of the accuracy on training and test sets. The accuracy gives the ratio of correctly predicted binary movie ratings. It can be seen that after 6 epochs the model predicts 78% of the time correctly if a user would like a random movie or not.

```
epoch_nr: 0, batch: 50/188, acc_train: 0.721, acc_test: 0.709
epoch_nr: 1, batch: 50/188, acc_train: 0.767, acc_test: 0.764
epoch_nr: 2, batch: 50/188, acc_train: 0.772, acc_test: 0.773
epoch_nr: 3, batch: 50/188, acc_train: 0.767, acc_test: 0.725
epoch_nr: 4, batch: 50/188, acc_train: 0.768, acc_test: 0.717
epoch_nr: 5, batch: 50/188, acc_train: 0.772, acc_test: 0.769
epoch_nr: 6, batch: 50/188, acc_train: 0.774, acc_test: 0.771
epoch_nr: 7, batch: 50/188, acc_train: 0.779, acc_test: 0.780
```

## References

>  https://github.com/artem-oppermann/Restricted-Boltzmann-Machine/blob/master/README.md

