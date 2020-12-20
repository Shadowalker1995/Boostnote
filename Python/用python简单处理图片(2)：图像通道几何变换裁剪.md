# 用python简单处理图片(2)：图像通道\几何变换\裁剪

##一、图像通道

###1、彩色图像转灰度图

```python
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('d:/ex.jpg')
gray=img.convert('L')
plt.figure("beauty")
plt.imshow(gray,cmap='gray')
plt.axis('off')
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160103134331620-1785696059.png)

使用函数convert()来进行转换，它是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式，mode 的取值可以是如下几种：

- 1 (1-bit pixels, black and white, stored with one pixel per byte)
- L (8-bit pixels, black and white)
- P (8-bit pixels, mapped to any other mode using a colour palette)
- RGB (3x8-bit pixels, true colour)
- RGBA (4x8-bit pixels, true colour with transparency mask)
- CMYK (4x8-bit pixels, colour separation)
- YCbCr (3x8-bit pixels, colour video format)
- I (32-bit signed integer pixels)
- F (32-bit floating point pixels)

###2、通道分离与合并

```python
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('d:/ex.jpg')  # open image
gray=img.convert('L')   # convert to gray mode
r,g,b=img.split()   # split three channels
pic=Image.merge('RGB',(r,g,b)) # merge three channels
plt.figure("beauty")
plt.subplot(2,3,1), plt.title('origin')
plt.imshow(img),plt.axis('off')
plt.subplot(2,3,2), plt.title('gray')
plt.imshow(gray,cmap='gray'),plt.axis('off')
plt.subplot(2,3,3), plt.title('merge')
plt.imshow(pic),plt.axis('off')
plt.subplot(2,3,4), plt.title('r')
plt.imshow(r,cmap='gray'),plt.axis('off')
plt.subplot(2,3,5), plt.title('g')
plt.imshow(g,cmap='gray'),plt.axis('off')
plt.subplot(2,3,6), plt.title('b')
plt.imshow(b,cmap='gray'),plt.axis('off')
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160103140351917-83215038.png)

# 二、裁剪图片

从原图片中裁剪感兴趣区域 (roi）,裁剪区域由4-tuple决定，该tuple中信息为(left, upper, right, lower)。Pillow左边系统的原点(0，0)为图片的左上角。坐标中的数字单位为像素点。

```python
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('d:/ex.jpg')  # open image
plt.figure("beauty")
plt.subplot(1,2,1), plt.title('origin')
plt.imshow(img),plt.axis('off')

box=(80,100,260,300)
roi=img.crop(box)
plt.subplot(1,2,2), plt.title('roi')
plt.imshow(roi),plt.axis('off')
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160103141335370-2117901788.png)

用plot绘制显示出图片后，将鼠标移动到图片上，会在右下角出现当前点的坐标，以及像素值。

# 三、几何变换

Image类有resize()、rotate()和transpose()方法进行几何变换。

###1、图像的缩放和旋转

```python
dst = img.resize((128, 128))
dst = img.rotate(45) # 顺时针角度表示
```

###2、转换图像

```python
dst = im.transpose(Image.FLIP_LEFT_RIGHT) # 左右互换
dst = im.transpose(Image.FLIP_TOP_BOTTOM) # 上下互换
dst = im.transpose(Image.ROTATE_90)  # 顺时针旋转
dst = im.transpose(Image.ROTATE_180)
dst = im.transpose(Image.ROTATE_270)
```

transpose()和rotate()没有性能差别。