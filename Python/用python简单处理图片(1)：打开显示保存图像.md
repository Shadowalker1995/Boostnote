# 用python简单处理图片(1)：打开/显示/保存图像

一提到数字图像处理，可能大多数人就会想到matlab，但matlab也有自身的缺点：

1、不开源，价格贵

2、软件容量大。一般3G以上，高版本甚至达5G以上。

3、只能做研究，不易转化成软件。

因此，我们这里使用python这个脚本语言来进行数字图像处理。

要使用python，必须先安装python，一般是2.7版本以上，不管是在windows系统，还是linux系统，安装都是非常简单的。

要使用python进行各种开发，就必须安装对应的库。这和matlab非常相似，只是matlab里面叫工具箱（toolbox)，而python里面叫库或包。安装这些库，一般都是使用pip来安装。

使用python进行数字图片处理，还得安装Pillow包。虽然python里面自带一个PIL（python images library), 但这个库现在已经停止更新了，所以使用Pillow, 它是由PIL发展而来的。

```shell
pip install Pillow
```

##一、图片的打开与显示

```python
from PIL import Image
img=Image.open('d:/dog.png')
img.show()
```

虽然使用的是Pillow，但它是由PIL fork而来，因此还是要从PIL中进行import. 使用open()函数来打开图片，使用show()函数来显示图片。

这种图片显示方式是调用操作系统自带的图片浏览器来打开图片，有些时候这种方式不太方便，因此我们也可以使用另上一种方式，让程序来绘制图片。

```python
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('d:/dog.png')
plt.figure("dog")
plt.imshow(img)
plt.show()
```

这种方法虽然复杂了些，但推荐使用这种方法，它使用一个matplotlib的库来绘制图片进行显示。matplotlib是一个专业绘图的库，相当于matlab中的plot,可以设置多个figure,设置figure的标题，甚至可以使用subplot在一个figure中显示多张图片。matplotlib 可以直接安装

```shell
pip install matplotlib
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160103115154339-792142004.png)

figure默认是带axis的，如果没有需要，我们可以关掉

```python
plt.axis('off')
```

打开图片后，可以使用一些属性来查看图片信息，如

```python
print img.size  #图片的尺寸
print img.mode  #图片的模式
print img.format  #图片的格式
```

显示结果为：

```python
(558, 450)
RGBA
PNG
```

##二、图片的保存

```python
img.save('d:/dog.jpg')
```

就一行代码，非常简单。这行代码不仅能保存图片，还是转换格式，如本例中，就由原来的png图片保存为了jpg图片。