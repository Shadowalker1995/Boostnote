## 用python简单处理图片(4)：图像中的像素访问

前面的一些例子中，我们都是利用Image.open()来打开一幅图像，然后直接对这个PIL对象进行操作。如果只是简单的操作还可以，但是如果操作稍微复杂一些，就比较吃力了。因此，通常我们加载完图片后，都是把图片转换成矩阵来进行更加复杂的操作。

python中利用numpy库和scipy库来进行各种数据操作和科学计算。我们可以通过pip来直接安装这两个库

```shell
pip install numpy
pip install scipy
```

以后，只要是在python中进行数字图像处理，我们都需要导入这些包：

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
```

打开图像并转化为矩阵，并显示：

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('d:/lena.jpg'))  # 打开图像并转化为数字矩阵
plt.figure("dog")
plt.imshow(img)
plt.axis('off')
plt.show()
```

调用numpy中的array()函数就可以将PIL对象转换为数组对象。

查看图片信息，可用如下的方法：

```python
print img.shape  
print img.dtype 
print img.size 
print type(img)
```

如果是RGB图片，那么转换为array之后，就变成了一个rows\*cols\*channels的三维矩阵,因此，我们可以使用

img[i, j, k]

来访问像素值。

例1：打开图片，并随机添加一些椒盐噪声

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('d:/ex.jpg'))

# 随机生成5000个椒盐
rows, cols, dims=img.shape
for i in range(5000):
    x=np.random.randint(0, rows)
    y=np.random.randint(0, cols)
    img[x,y,:]=255
    
plt.figure("beauty")
plt.imshow(img)
plt.axis('off')
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160103151154214-782489875.png)

例2：将lena图像二值化，像素值大于128的变为1，否则变为0

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('d:/pic/lena.jpg').convert('L'))

rows, cols=img.shape
for i in range(rows):
    for j in range(cols):
        if (img[i,j] <= 128):
            img[i,j] = 0
        else:
            img[i,j] = 1
            
plt.figure("lena")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160103152515620-1498965355.png)

如果要对多个像素点进行操作，可以使用数组切片方式访问。切片方式返回的是以指定间隔下标访问 该数组的像素值。下面是有关灰度图像的一些例子：

```python
img[i,:] = im[j,:] # 将第 j 行的数值赋值给第 i 行
img[:,i] = 100 # 将第 i 列的所有数值设为 100
img[:100,:50].sum() # 计算前 100 行、前 50 列所有数值的和
img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
img[i].mean() # 第 i 行所有数值的平均值
img[:,-1] # 最后一列
img[-2,:] (or im[-2]) # 倒数第二行
```