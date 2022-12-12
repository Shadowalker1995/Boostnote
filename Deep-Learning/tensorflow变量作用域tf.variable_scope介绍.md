# tensorflow变量作用域tf.variable_scope介绍

[toc]

## 0.Introduction

TensorFlow中的变量一般就是模型的参数, 当模型复杂的时候共享变量会无比复杂.

官网给了一个case, 当创建两层卷积的过滤器时, 每输入一次图片就会创建一次过滤器对应的变量, 但是我们希望所有图片都共享同一过滤器变量, 一共有4个变量: `conv1_weights`, `conv1_biases`, `conv2_weights`, and `conv2_biases`.

通常的做法是将这些变量设置为全局变量. 但是存在的问题是打破封装性, 这些变量必须文档化被其他代码文件引用, 一旦代码变化, 调用方也可能需要变化.

还有一种保证封装性的方式是将模型封装成类. 不过TensorFlow提供了 **Variable Scope** 这种独特的机制来共享变量. 这个机制涉及两个主要函数:

- `tf.get_variable(<name>, <shape>, <initializer>)`: 创建或返回给定名称的变量
- `tf.variable_scope(<scope_name>)`: 管理传给get_variable()的变量名称的作用域

在下面的代码中, 通过 `tf.get_variable()` 创建了名称分别为weights和biases的两个变量. 

```python
def conv_relu(input, kernel_shape, bias_shape):
    # Create variable named "weights".
    weights = tf.get_variable("weights", kernel_shape,
        initializer=tf.random_normal_initializer())
    # Create variable named "biases".
    biases = tf.get_variable("biases", bias_shape,
        initializer=tf.constant_initializer(0.0))
    conv = tf.nn.conv2d(input, weights,
        strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv + biases)
```

但是我们需要两个卷积层, 这时可以通过 `tf.variable_scope()` 指定作用域进行区分, 如 `with tf.variable_scope("conv1")` 这行代码指定了第一个卷积层作用域为conv1, 在这个作用域下有两个变量weights和biases.

```python
def my_image_filter(input_images):
    with tf.variable_scope("conv1"):
        # Variables created here will be named "conv1/weights", "conv1/biases".
        relu1 = conv_relu(input_images, [5, 5, 32, 32], [32])
    with tf.variable_scope("conv2"):
        # Variables created here will be named "conv2/weights", "conv2/biases".
        return conv_relu(relu1, [5, 5, 32, 32], [32])
```

最后在image_filters这个作用域重复使用第一张图片输入时创建的变量, 调用函数 `reuse_variables()`, 代码如下：

```python
with tf.variable_scope("image_filters") as scope:
    result1 = my_image_filter(image1)
    scope.reuse_variables()
    result2 = my_image_filter(image2)
```

## 1. `tf.get_variable()`工作机制

tf.get_variable()工作机制是这样的:

当 `tf.get_variable_scope().reuse == False`, 调用该函数会创建新的变量

```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
assert v.name == "foo/v:0"
```

当 `tf.get_variable_scope().reuse == True`, 调用该函数会重用已经创建的变量

```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v", [1])
assert v1 is v
```

变量都是通过作用域/变量名来标识, 后面会看到作用域可以像文件路径一样嵌套

## 2. `tf.variable_scope`理解

tf.variable_scope()用来指定变量的作用域, 作为变量名的前缀, 支持嵌套, 如下：

```python
with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1])
assert v.name == "foo/bar/v:0"
```

当前环境的作用域可以通过函数 `tf.get_variable_scope()` 获取, 并且reuse标志可以通过调用 `reuse_variables()` 设置为True, 这个非常有用, 如下:

```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
    tf.get_variable_scope().reuse_variables()
    v1 = tf.get_variable("v", [1])
assert v1 is v
```

作用域中的resuse默认是False, 调用函数 `reuse_variables()` 可设置为True, 一旦设置为True, 就不能返回到False, 并且该作用域的子空间reuse都是True. 如果不想重用变量, 那么可以退回到上层作用域, 相当于exit当前作用域, 如:

```python
with tf.variable_scope("root"):
    # At start, the scope is not reusing.
    assert tf.get_variable_scope().reuse == False
    with tf.variable_scope("foo"):
        # Opened a sub-scope, still not reusing.
        assert tf.get_variable_scope().reuse == False
    with tf.variable_scope("foo", reuse=True):
        # Explicitly opened a reusing scope.
        assert tf.get_variable_scope().reuse == True
        with tf.variable_scope("bar"):
            # Now sub-scope inherits the reuse flag.
            assert tf.get_variable_scope().reuse == True
    # Exited the reusing scope, back to a non-reusing one.
    assert tf.get_variable_scope().reuse == False
```

一个作用域可以作为另一个新的作用域的参数, 如:

```python
with tf.variable_scope("foo") as foo_scope:
    v = tf.get_variable("v", [1])
with tf.variable_scope(foo_scope):
    w = tf.get_variable("w", [1])
with tf.variable_scope(foo_scope, reuse=True):
    v1 = tf.get_variable("v", [1])
    w1 = tf.get_variable("w", [1])
assert v1 is v
assert w1 is w
```

不管作用域如何嵌套, 当使用 `with tf.variable_scope()` 打开一个已经存在的作用域时, 就会跳转到这个作用域:

```python
with tf.variable_scope("foo") as foo_scope:
    assert foo_scope.name == "foo"
with tf.variable_scope("bar"):
    with tf.variable_scope("baz") as other_scope:
        assert other_scope.name == "bar/baz"
        with tf.variable_scope(foo_scope) as foo_scope2:
            assert foo_scope2.name == "foo"  # Not changed.
```

variable scope的Initializers可以创递给子空间和tf.get_variable()函数, 除非中间有函数改变, 否则不变

```python
with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4)):
    v = tf.get_variable("v", [1])
    assert v.eval() == 0.4  # Default initializer as set above.
    w = tf.get_variable("w", [1], initializer=tf.constant_initializer(0.3)):
    assert w.eval() == 0.3  # Specific initializer overrides the default.
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1])
        assert v.eval() == 0.4  # Inherited default initializer.
    with tf.variable_scope("baz", initializer=tf.constant_initializer(0.2)):
        v = tf.get_variable("v", [1])
        assert v.eval() == 0.2  # Changed default initializer.
```

算子(ops)会受变量作用域(variable scope)影响, 相当于隐式地打开了同名的名称作用域(name scope), 如 `+` 这个算子的名称为 foo/add

```python
with tf.variable_scope("foo"):
    x = 1.0 + tf.get_variable("v", [1])
assert x.op.name == "foo/add"
```

除了变量作用域(variable scope), 还可以显式打开名称作用域(name scope), 名称作用域仅仅影响算子的名称, 不影响变量的名称. 另外如果 `tf.variable_scope()` 传入字符参数, 创建变量作用域的同时会隐式创建同名的名称作用域. 如下面的例子, 变量 `v` 的作用域是foo, 而算子 `x` 的算子变为foo/bar, 因为有隐式创建名称作用域foo

```python
with tf.variable_scope("foo"):
    with tf.name_scope("bar"):
        v = tf.get_variable("v", [1])
        x = 1.0 + v
assert v.name == "foo/v:0"
assert x.op.name == "foo/bar/add"
```

注意: 如果 `tf.variable_scope()` 传入的不是字符串而是scope对象, 则不会隐式创建同名的名称作用域, 而是将传入的scope对象的名字后面加上 `_N` (其中N是scope对象被传入的次数).

## Reference

> https://blog.csdn.net/weixin_41793877/article/details/86628060