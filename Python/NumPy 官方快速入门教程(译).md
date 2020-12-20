# NumPy 官方快速入门教程(译)

> 写在前面：本来是学习下 $NumPy$，看到官网的[入门教程](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)想跟着实验一下，怕不常用，而我这人健忘，所以记录下来。索性就照着翻译一下，同样可以提升自己的阅读和写作能力，需要的可以存一下。当然，本人水平有限，有错误的地方欢迎大家指正。这里是基于 [$NumPy v1.13 Manual$](https://docs.scipy.org/doc/numpy-1.13.0/user/quickstart.html) 翻译的。截止时间 $2018/02/04$

## 快速入门教程

### 1 准备工作

在你浏览这个指导之前，你应该懂一点 $Python$ 。如果你想回顾一下可以看[Python tutorial](https://docs.python.org/3/tutorial/)。如果你想把教程的代码跑起来，必须安装一些软件，请参考<http://scipy.org/install.html>

### 2 基础知识

$NumPy$ 的主要操作对象是同类型的多维数组。它是一个由正整数元组索引，元素类型相同的表（通常元素是数字）。在 $NumPy$ 维度被称为 `axes`, `axes` 的数量称为 `rank`。

例如，在 $3D$ 空间的一个点 $[1,2,1]$ 是一个 `rank = 1` 的数组，因为它只有一个 `axes`。这个 `axes` 的长度是 33。在下面这个例子中，数组 `rank = 2` （它是 22维的）。第一维（`axes`）长度是 22，第二位长度是 33

```python
[[ 1., 0., 0. ],
 [ 0., 1., 2. ]]
```

$NumPy$ 的数组类是 `ndarray`。也可以叫做 `array`。说到这里，`numpy.array` 和标准 ( Python \) 库中的 `array.array` 是不一样的，它只能处理一维的数组和提供更少的功能。`ndarray` 对象的一些重要属性如下：

##### ndarray.ndim

> 数组的 `axes` （维度) 的数量。在 $Python$ 中维数的大小又被称作 `rank`

##### ndarray.shape

> 数组的维数，这是由每个维度的大小组成的一个元组。对于一个 $n$ 行 $m$ 列的矩阵。`shape` 是 `(n, m)`。由 `shape` 元组的长度得出 `rank` 或者维数 `ndim`。

##### ndarray.size

> 数组元素的个数总和，这等于 `shape` 元组数字的乘积。

##### ndarray.dtype

> 在数组中描述元素类型的一个对象。它是一种可以用标准的 $Python$ 类型创建和指定的类型。另外，$NumPy$ 也提供了它自己的类型：`numpy.int32`，`numpy.int16`，`numpy.float64`…

##### ndarray.itemsize

> 数组中每个元素所占字节数。例如，一个 `float64` 的 `itemsize` 是 $8(=64/8bit)$，`complex32` 的 `itemsize`是 $4(=32/8bit)$。它和 `ndarray.dtype.itemsize` 是相等的。

##### ndarray.data

> 数组实际元素的缓存区。通常来说，我们不需要使用这个属性，因为我们会使用索引的方式访问数据。

### 2.1 例子

```python
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<type 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<type 'numpy.ndarray'>
```

### 2.2 创建数组

这里有几种方法创建数组。

例如，你可以使用 `array` 函数从一个常规的 $Python$ 列表或元组创建一个数组。创建的数组类型是从原始序列中的元素推断出来的。

```python
>>> import numpy as np
>>> a = np.array([2,3,4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> b = np.array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')
```

一个常见错误是在调用 `array` 函数时，传递的参数是多个数值而不是一个单独的数字列表。

```python
>>> a = np.array(1,2,3,4)    # WRONG
>>> a = np.array([1,2,3,4])  # RIGHT
```

`array` 将序列转化成高维数组

```python
>>> b = np.array([(1.5,2,3), (4,5,6)])
>>> b
array([[ 1.5,  2. ,  3. ],
       [ 4. ,  5. ,  6. ]])
```

数组的类型也能够在创建时具体指定：

```python
>>> c = np.array( [ [1,2], [3,4] ], dtype=complex )
>>> c
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])
```

通常，我们都是知道数组的大小而不知道其中的原始数据。因此 $NumPy$ 提供了几个用占位符的函数去创建数组。这样可以最小化增加数组的成本，增加数组是一项很耗费资源的操作。

`zeros` 函数创建一个全是 $0$ 的数组，`ones` 函数创建全是 $1$ 的数组，`empty` 创建一个随机的数组。默认创建数组的类型是 `float64`。

```python
>>> np.zeros( (3,4) )
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
>>> np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified
array([[[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]],
       [[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]]], dtype=int16)
>>> np.empty( (2,3) )                                 # uninitialized, output may vary
array([[  3.73603959e-262,   6.02658058e-154,   6.55490914e-260],
       [  5.30498948e-313,   3.14673309e-307,   1.00000000e+000]])
```

为了创建数字序列，$NumPy$ 提供了一个和 `range` 相似的函数，可以返回一个数组而不是列表。

```python
>>> np.arange( 10, 30, 5 )
array([10, 15, 20, 25])
>>> np.arange( 0, 2, 0.3 )                 # it accepts float arguments
array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
```

当 `arange` 的参数是浮点型的，由于有限的浮点精度，通常不太可能去预测获得元素的数量。出于这个原因，通常选择更好的函数 `linspace`，他接收我们想要的**元素数量**而不是步长作为参数。

```python
>>> from numpy import pi
>>> np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
>>> x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
>>> f = np.sin(x)
```

##### 参考

---

[array](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.array.html#numpy.array), [zeros](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.zeros.html#numpy.zeros), [zeros_like](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.zeros_like.html#numpy.zeros_like), [ones](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ones.html#numpy.ones), [ones_like](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ones_like.html#numpy.ones_like), [empty](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.empty.html#numpy.empty), [empty_like](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.empty_like.html#numpy.empty_like), [arange](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.arange.html#numpy.arange), [linspace](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.linspace.html#numpy.linspace), [numpy.random.rand](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.random.rand.html#numpy.random.rand), [numpy.random.randn](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.random.randn.html#numpy.random.randn), [fromfunction](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.fromfunction.html#numpy.fromfunction), [fromfile](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.fromfile.html#numpy.fromfile)

### 2.3 打印数组

当你打印数组时，$NumPy$ 显示出来和嵌套的列表相似，但是具有以下布局：

- 最后一个 `axis` 从左到右打印，
- 第二到最后一个从上到下打印，
- 剩余的也是从上到下打印，每一片通过一个空行隔开。

```python
>>> a = np.arange(6)                         # 1d array
>>> print(a)
[0 1 2 3 4 5]
>>>
>>> b = np.arange(12).reshape(4,3)           # 2d array
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>>
>>> c = np.arange(24).reshape(2,3,4)         # 3d array
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]
 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
```

参考[下文](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#quickstart-shape-manipulation)来获取更多 `reshape` 的细节。

如果一个数组太大而不能被打印，那么 $NumPy$ 会自动忽略中间的只打印角上的数据。

```python
>>> print(np.arange(10000))
[   0    1    2 ..., 9997 9998 9999]
>>>
>>> print(np.arange(10000).reshape(100,100))
[[   0    1    2 ...,   97   98   99]
 [ 100  101  102 ...,  197  198  199]
 [ 200  201  202 ...,  297  298  299]
 ...,
 [9700 9701 9702 ..., 9797 9798 9799]
 [9800 9801 9802 ..., 9897 9898 9899]
 [9900 9901 9902 ..., 9997 9998 9999]]
```

为了取消这种行为，强制 $NumPy$ 去打印整个数组，你可以通过 `set_printoptions` 改变打印选项。

```python
>>> np.set_printoptions(threshold='nan')
```

### 2.4 基本操作

在数组上的算数运算应用于每个元素。并创建一个用结果填充的新的数组。

```python
>>> a = np.array( [20,30,40,50] )
>>> b = np.arange( 4 )
>>> b
array([0, 1, 2, 3])
>>> c = a-b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10*np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a<35
array([ True, True, False, False], dtype=bool)
```

在 $NumPy$ 数组的 `*` 操作不像其他的矩阵语言。矩阵乘法通过 `dot` 函数进行模拟。

```python
>>> A = np.array( [[1,1],
...             [0,1]] )
>>> B = np.array( [[2,0],
...             [3,4]] )
>>> A*B                         # elementwise product
array([[2, 0],
       [0, 4]])
>>> A.dot(B)                    # matrix product
array([[5, 4],
       [3, 4]])
>>> np.dot(A, B)                # another matrix product
array([[5, 4],
       [3, 4]])
```

想 `+=` 和 `*=` 操作之类的，直接在**原数组**上做修改，不会创建新数组。

```python
>>> a = np.ones((2,3), dtype=int)
>>> b = np.random.random((2,3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[ 3.417022  ,  3.72032449,  3.00011437],
       [ 3.30233257,  3.14675589,  3.09233859]])
>>> a += b                  # b is not automatically converted to integer type
Traceback (most recent call last):
  ...
TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

在不同数组类型之间的操作，结果数组的类型趋于更普通或者更精确的一种（称为向上转型）

```python
>>> a = np.ones(3, dtype=np.int32)
>>> b = np.linspace(0,pi,3)
>>> b.dtype.name
'float64'
>>> c = a+b
>>> c
array([ 1.        ,  2.57079633,  4.14159265])
>>> c.dtype.name
'float64'
>>> d = np.exp(c*1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
```

许多类似于求数组所有元素的和的一元操作都是作为 `ndarray` 类的方法实现的。

```python
>>> a = np.random.random((2,3))
>>> a
array([[ 0.18626021,  0.34556073,  0.39676747],
       [ 0.53881673,  0.41919451,  0.6852195 ]])
>>> a.sum()
2.5718191614547998
>>> a.min()
0.1862602113776709
>>> a.max()
0.6852195003967595
```

默认情况下，尽管这些操作是应用于一个数字列表，可以无视它的形状。当时，通过指定 `axis` 参数可以将操作应用于数组的某一具体 `axis` 。

```python
>>> b = np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)                            # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)                            # min of each row
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)                         # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```

### 2.5 通用功能

$NumPy$ 提供了很多数学上的函数，例如 `sin`、`cos`、`exp`。这些被叫做 “universal functions” (`ufunc`)。在 $NumPy$ 中这些函数是操作数组数字，产生一个数组作为输出。

```python
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([ 1.        ,  2.71828183,  7.3890561 ])
>>> np.sqrt(B)
array([ 0.        ,  1.        ,  1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([ 2.,  0.,  6.])
```

##### 参考

[all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#universal-functions)

### 2.6 索引，切片和迭代

一维数组可以被索引，切片和迭代，就像[列表](https://docs.python.org/tutorial/introduction.html#lists)和其他Python序列一样。

```python
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
>>> a
array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
>>> a[ : :-1]                                 # reversed a
array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
>>> for i in a:
...     print(i**(1/3.))
...
nan
1.0
nan
3.0
nan
5.0
6.0
7.0
8.0
9.0
```

多维数组对于每个 `axis` 都有一个索引，这些索引用逗号分隔。

```python
>>> def f(x,y):
...     return 10*x+y
...
>>> b = np.fromfunction(f,(5,4),dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2,3]
23
>>> b[0:5, 1]                       # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[ : ,1]                        # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, : ]                      # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

当提供的索引少于 `axis` 的数量时，缺失的索引按完全切片考虑。

```python
>>> b[-1]                                  # the last row. Equivalent to b[-1,:]
array([40, 41, 42, 43])
```

`b[i]` 这种表达中括号中的 `i` 后面可以跟很多用 `:` 表示其它 `axis` 的实例。NumPyNumPy 也允许使用三个点代替 `b[i, ...]`

这三个点(`...`)表示很多完整索引元组中的冒号。例如，`x` 的 `rank = 5` 有：

- `x[1, 2, ...]` = `x[1, 2, :, :, :]`
- `x[..., 3]` = `x[:, :, :, :, 3]`
- `x[4, ..., 5, :]` = `x[4, :, :, 5, :]`

```python
>>> c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
...                 [ 10, 12, 13]],
...                [[100,101,102],
...                 [110,112,113]]])
>>> c.shape
(2, 2, 3)
>>> c[1,...]                                   # same as c[1,:,:] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[...,2]                                   # same as c[:,:,2]
array([[  2,  13],
       [102, 113]])
```

迭代多维数组是对第一 `axis` 进行的。

```python
>>> for row in b:
...     print(row)
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

然而，如果你想模拟对数组中每一个元素的操作，你可以使用 `flat`属性，它是一个 [iterator](https://docs.python.org/2/tutorial/classes.html#iterators)，能够遍历数组中每一个元素。

```python
>>> for element in b.flat:
...     print(element)
...
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```

##### 参考

[Indexing](https://docs.scipy.org/doc/numpy-dev/user/basics.indexing.html#basics-indexing), [Indexing](https://docs.scipy.org/doc/numpy-dev/reference/arrays.indexing.html#arrays-indexing) (reference), [newaxis](https://docs.scipy.org/doc/numpy-dev/reference/arrays.indexing.html#numpy.newaxis), [ndenumerate](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate), [indices](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.indices.html#numpy.indices)

## 3 操控形状

### 3.1 改变数组的形状

每一个数组的形状通过每一个 `axis` 中的元素数量。（其实就是每一个维度的元素多少确定）

```python
>>> a = np.floor(10*np.random.random((3,4)))
>>> a
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
>>> a.shape
(3, 4)
```

数组的形状可以通过很多命令来改变，提到这里，接下来的三个例子放回一个被修改的数组，原数组不会改变。

```python
>>> a.ravel()  # returns the array, flattened
array([ 2.,  8.,  0.,  6.,  4.,  5.,  1.,  1.,  8.,  9.,  3.,  6.])
>>> a.reshape(6,2)  # returns the array with a modified shape
array([[ 2.,  8.],
       [ 0.,  6.],
       [ 4.,  5.],
       [ 1.,  1.],
       [ 8.,  9.],
       [ 3.,  6.]])
>>> a.T  # returns the array, transposed
array([[ 2.,  4.,  8.],
       [ 8.,  5.,  9.],
       [ 0.,  1.,  3.],
       [ 6.,  1.,  6.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```

`ravel()` 函数中每个元素的位置通常是一种 “C-style” 的，也就是说，最右边的索引改变起来最快。所以元素 `a[0, 0]` 后面的元素是 `a[0, 1]`。如果这个数组被塑造成其它形状，这个数组也是作为 “C-style” 对待。$NumPy$ 通常也是按照这个创建的数组，所以使用 `ravel()` 函数时不需要复制，但是如果这个数组是通过从另一个数组切片或者其它不同寻常的方式而来的话，它就需要进行复制了。函数 `ravel()` 和 `reshape()` 也可以通过可选参数被指定去用 `FORTRAN-style` 的数组，这这种风格中，最左的索引改变最快。

[reshape](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.reshape.html#numpy.reshape) 函数返回修改的形状，而 [ndarray.resize](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize) 方法直接修改数组本身。

```python
>>> a
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
>>> a.resize((2,6))
>>> a
array([[ 2.,  8.,  0.,  6.,  4.,  5.],
       [ 1.,  1.,  8.,  9.,  3.,  6.]])
```

如果一个维度给一个 $−1$ 作为参数，那么其他它维度将自动计算。

```
>>> a.reshape(3,-1)
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
```

##### 参考

[ndarray.shape](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape), [reshape](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.reshape.html#numpy.reshape), [resize](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.resize.html#numpy.resize), [ravel](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ravel.html#numpy.ravel)

### 3.2 不同数组的组合

数组可以通过不同的 `axes` 组合起来。

```python
>>> a = np.floor(10*np.random.random((2,2)))
>>> a
array([[ 8.,  8.],
       [ 0.,  0.]])
>>> b = np.floor(10*np.random.random((2,2)))
>>> b
array([[ 1.,  8.],
       [ 0.,  4.]])
>>> np.vstack((a,b))
array([[ 8.,  8.],
       [ 0.,  0.],
       [ 1.,  8.],
       [ 0.,  4.]])
>>> np.hstack((a,b))
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])
```

[column_stack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.column_stack.html#numpy.column_stack) 函数可以将 $1D$ 数组作为 $2D$ 数组的列。当且仅当数组是 $1D$ 的时候它等于 [vstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.vstack.html#numpy.vstack)

```python
>>> from numpy import newaxis
>>> np.column_stack((a,b))   # With 2D arrays
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])
>>> a = np.array([4.,2.])
>>> b = np.array([2.,8.])
>>> a[:,newaxis]  # This allows to have a 2D columns vector
array([[ 4.],
       [ 2.]])
>>> np.column_stack((a[:,newaxis],b[:,newaxis]))
array([[ 4.,  2.],
       [ 2.,  8.]])
>>> np.vstack((a[:,newaxis],b[:,newaxis])) # The behavior of vstack is different
array([[ 4.],
       [ 2.],
       [ 2.],
       [ 8.]])
```

对于超过两个维度的数组，[hstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.hstack.html#numpy.hstack) 会沿着第二个 `axis` 堆积，[vstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.vstack.html#numpy.vstack)沿着第一个 `axes` 堆积，[concatenate](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.concatenate.html#numpy.concatenate) 允许一个可选参数选择哪一个 `axis` 发生连接操作。

##### 提示

在复杂情况下，[r_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.r_.html#numpy.r_) 和 [c_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.c_.html#numpy.c_) 对于通过沿一个 `axis` 堆积数字来创建数组很有用。它们允许使用范围表示符号（“:”）

```python
>>> np.r_[1:4,0,4]
array([1, 2, 3, 0, 4])
```

当使用数组作为参数时，[r_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.r_.html#numpy.r_) 与 [c_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.c_.html#numpy.c_) 在默认行为是和 [vstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.vstack.html#numpy.vstack) 与 [hstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.hstack.html#numpy.hstack) 相似的，但是它们允许可选参数给出 `axis` 来连接。

##### 参考

[hstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.hstack.html#numpy.hstack)，[vstack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.vstack.html#numpy.vstack)，[column_stack](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.column_stack.html#numpy.column_stack)，[concatenate](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.concatenate.html#numpy.concatenate)，[c_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.c_.html#numpy.c_)，[r_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.r_.html#numpy.r_)

### 3.3 将数组分割成几个小数组

使用 [hsplit](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.hsplit.html#numpy.hsplit)，你能沿着它的水平 `axis` 分割，可以通过指定数组形状来返回，也可以指定哪个列应该拆分：

```python
>>> a = np.floor(10*np.random.random((2,12)))
>>> a
array([[ 9.,  5.,  6.,  3.,  6.,  8.,  0.,  7.,  9.,  7.,  2.,  7.],
       [ 1.,  4.,  9.,  2.,  2.,  1.,  0.,  6.,  2.,  2.,  4.,  0.]])
>>> np.hsplit(a,3)   # Split a into 3
[array([[ 9.,  5.,  6.,  3.],
       [ 1.,  4.,  9.,  2.]]), array([[ 6.,  8.,  0.,  7.],
       [ 2.,  1.,  0.,  6.]]), array([[ 9.,  7.,  2.,  7.],
       [ 2.,  2.,  4.,  0.]])]
>>> np.hsplit(a,(3,4))   # Split a after the third and the fourth column
[array([[ 9.,  5.,  6.],
       [ 1.,  4.,  9.]]), array([[ 3.],
       [ 2.]]), array([[ 6.,  8.,  0.,  7.,  9.,  7.,  2.,  7.],
       [ 2.,  1.,  0.,  6.,  2.,  2.,  4.,  0.]])]
```

[vplit](http://fitzeng.org/2018/02/04/NumPyOfficialQuickstartTutorial/) 沿着竖直的 `axis` 分割，[array_split](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.array_split.html#numpy.array_split) 允许通过指定哪个 `axis` 去分割。

## 4 拷贝和 Views

在操作数组的时候，它们的数据有时候拷贝进一个新的数组，有时候又不是。这经常是初学者感到困惑。下面有三种情况：

### 4.1 不拷贝

简单的赋值不会拷贝任何数组对象和它们的数据。

```python
>>> a = np.arange(12)
>>> b = a            # no new object is created
>>> b is a           # a and b are two names for the same ndarray object
True
>>> b.shape = 3,4    # changes the shape of a
>>> a.shape
(3, 4)
```

$Python$ 将可变对象作为引用传递，所以函数调用不会产生拷贝。

```python
>>> def f(x):
...     print(id(x))
...
>>> id(a)                           # id is a unique identifier of an object
148293216
>>> f(a)
148293216
```

### 4.2 View 或者浅拷贝

不同的数组对象可以分享相同的数据。`view` 方法创建了一个相同数据的新数组对象。

PS：这里 View（视图？） 不知道如何理解好，所以保留。

```python
>>> c = a.view()
>>> c is a
False
>>> c.base is a                        # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c.shape = 2,6                      # a's shape doesn't change
>>> a.shape
(3, 4)
>>> c[0,4] = 1234                      # a's data changes
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
```

切片数组返回一个 `view`：

```python
>>> s = a[ : , 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
>>> s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

### 4.3 深拷贝

`copy` 方法完全拷贝数组。

```python
>>> d = a.copy()                          # a new array object with new data is created
>>> d is a
False
>>> d.base is a                           # d doesn't share anything with a
False
>>> d[0,0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

### 4.4 函数和方法综述

这里通过类别排序列举一些有用的 $NumPy$ 函数和方法。拆看完整列表点击[Routines](https://docs.scipy.org/doc/numpy-dev/reference/routines.html#routines)

##### 数组收集

> [arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 转化

> [ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 操作

> [array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 疑问

> [all, any, nonzero, where](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 排序

> [argmax, argmin, argsort, max, min, ptp, searchsorted, sort](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 运算

> [choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 基本统计

> [cov, mean, std, var](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

##### 基本线性代数

> [cross, dot, outer, linalg.svd, vdot](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview)

## 5 Less Basic

### 5.1 广播规则

广播允许通用功能用一种有意义的方式去处理不完全相同的形状输入。
第一条广播规则是如果所有输入的数组都没有相同的维度数字，那么将会重复地用 11 去加在较小的数组形状上直到所有的数组有相同的维度数字。
第二条广播规则是确保沿着特定维度大小为 11 的数组就像沿着这个维度最大维数大小一样的，假设数组元素的值在广播数组的维度是相同的。
应用广播规则后，所有数组大小不必须匹配。更多细节可以在[Broadcasting](https://docs.scipy.org/doc/numpy-dev/user/basics.broadcasting.html)。

- [Numpy中的广播(Broadcasting)](http://blog.csdn.net/yangnanhai93/article/details/50127747)

## 6 花式索引和索引技巧

$NumPy$ 提供了比 $Python$ 序列更多的索引功能。除了我们之前看到的通过整数和切片索引之外，数组可以通过整数数组和布尔数组索引。

### 6.1 用索引数组索引

```python
>>> a = np.arange(12)**2                       # the first 12 square numbers
>>> i = np.array( [ 1,1,3,8,5 ] )              # an array of indices
>>> a[i]                                       # the elements of a at the positions i
array([ 1,  1,  9, 64, 25])
>>>
>>> j = np.array( [ [ 3, 4], [ 9, 7 ] ] )      # a bidimensional array of indices
>>> a[j]                                       # the same shape as j
array([[ 9, 16],
       [81, 49]])
```

当数组 `a` 是多维的，单个数组指向数组 `a` 的第一维。以下示例通过使用调色板将标签图像转换为彩色图像来显示此行为。

```python
>>> palette = np.array( [ [0,0,0],                # black
...                       [255,0,0],              # red
...                       [0,255,0],              # green
...                       [0,0,255],              # blue
...                       [255,255,255] ] )       # white
>>> image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
...                     [ 0, 3, 4, 0 ]  ] )
>>> palette[image]                            # the (2,4,3) color image
array([[[  0,   0,   0],
        [255,   0,   0],
        [  0, 255,   0],
        [  0,   0,   0]],
       [[  0,   0,   0],
        [  0,   0, 255],
        [255, 255, 255],
        [  0,   0,   0]]])
```

我们可以给超过一维的索引。数组每个维度的索引形状必须一样。

```python
>>> a = np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> i = np.array( [ [0,1],                        # indices for the first dim of a
...                 [1,2] ] )
>>> j = np.array( [ [2,1],                        # indices for the second dim
...                 [3,3] ] )
>>>
>>> a[i,j]                                     # i and j must have equal shape
array([[ 2,  5],
       [ 7, 11]])
>>>
>>> a[i,2]
array([[ 2,  6],
       [ 6, 10]])
>>>
>>> a[:,j]                                     # i.e., a[ : , j]
array([[[ 2,  1],
        [ 3,  3]],
       [[ 6,  5],
        [ 7,  7]],
       [[10,  9],
        [11, 11]]])
```

当然，我们可以把 `i`, `j` 放进一个序列然后对这个列表进行索引。

```python
>>> l = [i,j]
>>> a[l]                                       # equivalent to a[i,j]
array([[ 2,  5],
       [ 7, 11]])
```

然而，我们可以直接把 `i`，`j` 放进数组中，因为这个数组将会被解释成 `a` 第一维的索引。

```python
>>> s = np.array( [i,j] )
>>> a[s]                                       # not what we want
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
IndexError: index (3) out of range (0<=index<=2) in dimension 0
>>>
>>> a[tuple(s)]                                # same as a[i,j]
array([[ 2,  5],
       [ 7, 11]])
```

另一个常用数组索引是查询时间相关系列的最大值。

```python
>>> time = np.linspace(20, 145, 5)                 # time scale
>>> data = np.sin(np.arange(20)).reshape(5,4)      # 4 time-dependent series
>>> time
array([  20.  ,   51.25,   82.5 ,  113.75,  145.  ])
>>> data
array([[ 0.        ,  0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ,  0.6569866 ],
       [ 0.98935825,  0.41211849, -0.54402111, -0.99999021],
       [-0.53657292,  0.42016704,  0.99060736,  0.65028784],
       [-0.28790332, -0.96139749, -0.75098725,  0.14987721]])
>>>
>>> ind = data.argmax(axis=0)                   # index of the maxima for each series
>>> ind
array([2, 0, 3, 1])
>>>
>>> time_max = time[ ind]                       # times corresponding to the maxima
>>>
>>> data_max = data[ind, xrange(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
>>>
>>> time_max
array([  82.5 ,   20.  ,  113.75,   51.25])
>>> data_max
array([ 0.98935825,  0.84147098,  0.99060736,  0.6569866 ])
>>>
>>> np.all(data_max == data.max(axis=0))
True
```

你也可以使用数组索引对数组进行赋值：

```python
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> a[[1,3,4]] = 0
>>> a
array([0, 0, 2, 0, 0])
```

然而，当你的列表索引包含重复，这个赋值会发生几次，保留最后一个数值。

```python
>>> a = np.arange(5)
>>> a[[0,0,2]]=[1,2,3]
>>> a
array([2, 1, 3, 3, 4])
```

这足够合理，但是如果你想使用 $Python$ 的 `+=` 结构时要小心，它可能不像你期待的一样：

```python
>>> a = np.arange(5)
>>> a[[0,0,2]]+=1
>>> a
array([1, 1, 3, 3, 4])
```

即使 $0$ 在列表中出现了两次，这第 $0$ 个元素也只增加一次。这是因为$Python$ 把 “a+=1” 等价于 “a=a+1”。

### 6.2 用布尔数组索引

当我们用整数数组去索引数组时，我们提供了索引列表去挑选。用布尔索引的方法是不用的；我们明确的在数组中选择哪个我们想要哪个我们不想要。
最自然能想到的方法是用和原数组一样形状的布尔数组进行布尔索引。

```python
>>> a = np.arange(12).reshape(3,4)
>>> b = a > 4
>>> b                                          # b is a boolean with a's shape
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]], dtype=bool)
>>> a[b]                                       # 1d array with the selected elements
array([ 5,  6,  7,  8,  9, 10, 11])
```

这个属性在复制时非常有用。

```python
>>> a[b] = 0                                   # All elements of 'a' higher than 4 become 0
>>> a
array([[0, 1, 2, 3],
       [4, 0, 0, 0],
       [0, 0, 0, 0]])
```

你可以看接下来的例子去了解如何使用布尔索引去生成 [Mandelbrot set](http://en.wikipedia.org/wiki/Mandelbrot_set)图像。

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def mandelbrot( h,w, maxit=20 ):
...     """Returns an image of the Mandelbrot fractal of size (h,w)."""
...     y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
...     c = x+y*1j
...     z = c
...     divtime = maxit + np.zeros(z.shape, dtype=int)
...
...     for i in range(maxit):
...         z = z**2 + c
...         diverge = z*np.conj(z) > 2**2            # who is diverging
...         div_now = diverge & (divtime==maxit)  # who is diverging now
...         divtime[div_now] = i                  # note when
...         z[diverge] = 2                        # avoid diverging too much
...
...     return divtime
>>> plt.imshow(mandelbrot(400,400))
>>> plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
    c = x + y * 1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoid diverging too much
    return divtime

plt.imshow(mandelbrot(400, 400))
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/NumPy 官方快速入门教程(译).assets/6_2_01.png)

第二种用布尔索引方法更像是整数索引，对于每个数组的维度，我们给一个 $1D$ 的布尔数组去选择我们想要的切片。

```python
>>> a = np.arange(12).reshape(3,4)
>>> b1 = np.array([False,True,True])             # first dim selection
>>> b2 = np.array([True,False,True,False])       # second dim selection
>>>
>>> a[b1,:]                                   # selecting rows
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> a[b1]                                     # same thing
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> a[:,b2]                                   # selecting columns
array([[ 0,  2],
       [ 4,  6],
       [ 8, 10]])
>>>
>>> a[b1,b2]                                  # a weird thing to do
array([ 4, 10])
```

请注意，$1D$ 布尔数组的长度必须与你要切片的维度（或`axis`）的长度一致。在之前的例子中，`b1` 是一个长度为 33（`a` 的行数） 的 `1-rank` 数组，`b2` （长度为 44）是一个适合去索引 `a` 的第二 `rank`(列)。

### 6.3 ix_() 函数

[ix_](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.ix_.html#numpy.ix_) 可以组合不同向量去获得对于每一个 `n-uplet` 的结果。例如，如果你想从每个 $a,b,c$ 向量中取得三元组去计算所有的 $a+b∗c$：

```python
>>> a = np.array([2,3,4,5])
>>> b = np.array([8,5,4])
>>> c = np.array([5,4,6,8,3])
>>> ax,bx,cx = np.ix_(a,b,c)
>>> ax
array([[[2]],
       [[3]],
       [[4]],
       [[5]]])
>>> bx
array([[[8],
        [5],
        [4]]])
>>> cx
array([[[5, 4, 6, 8, 3]]])
>>> ax.shape, bx.shape, cx.shape
((4, 1, 1), (1, 3, 1), (1, 1, 5))
>>> result = ax+bx*cx
>>> result
array([[[42, 34, 50, 66, 26],
        [27, 22, 32, 42, 17],
        [22, 18, 26, 34, 14]],
       [[43, 35, 51, 67, 27],
        [28, 23, 33, 43, 18],
        [23, 19, 27, 35, 15]],
       [[44, 36, 52, 68, 28],
        [29, 24, 34, 44, 19],
        [24, 20, 28, 36, 16]],
       [[45, 37, 53, 69, 29],
        [30, 25, 35, 45, 20],
        [25, 21, 29, 37, 17]]])
>>> result[3,2,4]
17
>>> a[3]+b[2]*c[4]
17
```

你也可以按以下方式实现：

```python
>>> def ufunc_reduce(ufct, *vectors):
...    vs = np.ix_(*vectors)
...    r = ufct.identity
...    for v in vs:
...        r = ufct(r,v)
...    return r
```

然后这样使用：

```python
>>> ufunc_reduce(np.add,a,b,c)
array([[[15, 14, 16, 18, 13],
        [12, 11, 13, 15, 10],
        [11, 10, 12, 14,  9]],
       [[16, 15, 17, 19, 14],
        [13, 12, 14, 16, 11],
        [12, 11, 13, 15, 10]],
       [[17, 16, 18, 20, 15],
        [14, 13, 15, 17, 12],
        [13, 12, 14, 16, 11]],
       [[18, 17, 19, 21, 16],
        [15, 14, 16, 18, 13],
        [14, 13, 15, 17, 12]]])
```

这个版本的比通常的 `ufunc.reduce` 好在它使用了[Broadcasting Rules](https://docs.scipy.org/doc/numpy-dev/user/Tentative_NumPy_Tutorial.html#head-c43f3f81719d84f09ae2b33a22eaf50b26333db8) 规则去避免创建一个大小是输出乘以矢量数量数组。

### 6.4 使用字符串索引

参考[Structured arrays](https://docs.scipy.org/doc/numpy-dev/user/basics.rec.html#structured-arrays)

## 7 线性代数

工作进行中，基本的线性代数包含在其中。

### 7.1 简单的数组操作

看 $NumPy$ 文件夹下的 $linalg.pylinalg.py$ 文件了解更多。

```python
>>> import numpy as np
>>> a = np.array([[1.0, 2.0], [3.0, 4.0]])
>>> print(a)
[[ 1.  2.]
 [ 3.  4.]]

>>> a.transpose()
array([[ 1.,  3.],
       [ 2.,  4.]])

>>> np.linalg.inv(a)
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

>>> u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
>>> u
array([[ 1.,  0.],
       [ 0.,  1.]])
>>> j = np.array([[0.0, -1.0], [1.0, 0.0]])

>>> np.dot (j, j) # matrix product
array([[-1.,  0.],
       [ 0., -1.]])

>>> np.trace(u)  # trace
2.0

>>> y = np.array([[5.], [7.]])
>>> np.linalg.solve(a, y)
array([[-3.],
       [ 4.]])

>>> np.linalg.eig(j)
(array([ 0.+1.j,  0.-1.j]), array([[ 0.70710678+0.j        ,  0.70710678-0.j        ],
       [ 0.00000000-0.70710678j,  0.00000000+0.70710678j]]))
```

```python
Parameters:
    square matrix
Returns
    The eigenvalues, each repeated according to its multiplicity.
    The normalized (unit "length") eigenvectors, such that the
    column ``v[:,i]`` is the eigenvector corresponding to the
    eigenvalue ``w[i]`` .
```

## 8 技巧和提示

这里我们给出一些有用的小技巧。

### 8.1 “自动塑形”

为了改变数组的维度，你可以省略一个可以自动被推算出来的大小的参数。

```python
>>> a = np.arange(30)
>>> a.shape = 2,-1,3  # -1 means "whatever is needed"
>>> a.shape
(2, 5, 3)
>>> a
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]],
       [[15, 16, 17],
        [18, 19, 20],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29]]])
```

### 8.2 矢量叠加

我们怎么从一个相同大小的行向量构造出一个 $2D$ 数组？在 $MATLAB$ 中是相当简单的：如果 `x` 和 `y` 是两个相同长度的向量，你只需要把 `m=[x;y]`。在 $NumPy$ 中，通过函数 `column_stack`，`dstack`，`hstack` 和 `vstack` 实现，这取决于所要叠加的维度。例如：

```python
x = np.arange(0,10,2)                     # x=([0,2,4,6,8])
y = np.arange(5)                          # y=([0,1,2,3,4])
m = np.vstack([x,y])                      # m=([[0,2,4,6,8],
                                          #     [0,1,2,3,4]])
xy = np.hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])
```

在超过两个维度时这些函数背后的逻辑是奇怪的。

##### 参考

[NumPy for Matlab users](https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html)

### 8.3 柱状图

$NumPy$ 的 `histogram` 函数应用于数组，返回一对矢量：数组的柱状图和 `bins` 矢量。当心：`matplotlib` 也有一个函数去构建柱状图（叫做 `hist`，同样在 $Matlab$ 中），这个和 $NumPy$ 还是不一样的。主要的区别是 `pylab.hist` 自动绘制柱状图而 `matplotlib`只是生成数据。

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
>>> mu, sigma = 2, 0.5
>>> v = np.random.normal(mu,sigma,10000)
>>> # Plot a normalized histogram with 50 bins
>>> plt.hist(v, bins=50, normed=1)       # matplotlib version (plot)
>>> plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, normed=1)  # matplotlib version (plot)
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/NumPy 官方快速入门教程(译).assets/8_3_01.png)

```python
>>> # Compute the histogram with numpy and then plot it
>>> (n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
>>> plt.plot(.5*(bins[1:]+bins[:-1]), n)
>>> plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()
```

![img](http://fitzeng.org/2018/02/04/NumPyOfficialQuickstartTutorial/8_3_02.png)

## 9 更多阅读

- The [Python tutorial](http://docs.python.org/tutorial/)
- [NumPy Reference](https://docs.scipy.org/doc/numpy-dev/reference/index.html#reference)
- [SciPy Tutorial](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html)
- [SciPy Lecture Notes](http://www.scipy-lectures.org/)
- A [matlab, R, IDL, NumPy/SciPy dictionary](http://mathesaurus.sf.net/)