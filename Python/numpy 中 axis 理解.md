# numpy 中 axis 理解

numpy库中有些函数有个参数 axis，像 `ndarray.max()` 等，ndarray 其实就是一个多维数组，比python 内建的list多了一些对多维数组的操纵方法。如果一个多维数组是 2\*3\*2，他就是3维的，参数axis=0指的就是第一维，即2那一个数轴，axis=1,即3的那个数轴，axis=2,即最后2的那个数轴。

程序段

```python
import numpy as np
np.random.seed(123)
x=np.random.randint(0,5,[2,3,2])
print x
print x.max(axis=0) 
```

输出

```python
[[[2 4]
  [2 1]
  [3 2]]

 [[3 1]
  [1 0]
  [1 1]]]
[[3 4]
 [2 1]
 [3 2]] 
```

分析：

指定 axis=0，即在第一维的数轴求取最大值，2\*3\*2，去掉第一个维度，结果应该是3\*2。将上面x的上面和下面块比较就可以啦。

如果指定 axis=1,则输出为

```python
[[[2 4]
  [2 1]
  [3 2]]

 [[3 1]
  [1 0]
  [1 1]]]
[[3 4]
 [3 1]]
```