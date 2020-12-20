# Matplotlib 基本操作

> 写在前面：这篇主要为了自己的学习，先理一下基础概念，然后记录下来，下次使用起来就方便了。学这个的主要目的是为了可视化机器学习的学习过程。网络上的资料太多了，每次写的时候去查算起来也是挺花费时间的。所以还是花点时间直接整理记录好了。这里推荐[morvan：markdown + 视频](https://morvanzhou.github.io/tutorials/data-manipulation/plt/) 和 [官方文档](https://matplotlib.org/tutorials/index.html)。当然，此文还参考了好多网上的其它文章，再此一并感谢，并且参考资料中给出链接。所有代码整理到[GitHub](https://github.com/mk43/python-practice/tree/master/matplotlib)。

## 1. Matplotlib 快速入门

主要内容是把图画出来，然后认识图中的基本元素。

### 1.1 显示图像

直接上代码吧。整个过程就是`导库-准备数据-绘制-显示`

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x + 1

plt.plot(x, y)
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_1_01.png)

那么显示多条线怎么办？

```python
x = np.linspace(0, 10, 20)
y1 = x + 1
y2 = -x + 1

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_1_02.png)

看到这里，我们就很清楚了，$plot$ 函数就是把数据绘制在画框里。

### 1.2 认识 figure

$figure$ 可以理解为一个画框，往里面 $plot$ 图形。所以以下代码会显示出两个窗体。一个窗体比例是 $9:6$。更多参数可以参考源码注释，讲的很清楚。

```python
x = np.linspace(0, 10, 20)
y1 = x + 1
y2 = -x - 10
plt.figure()
plt.plot(x, y1)
plt.figure(figsize=(9, 6))
plt.plot(x, y2)
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_2_01.png)

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_2_02.png)

### 1.3 plot 参数设置

先看下一些效果吧。![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_3_01.png)

```python
x = np.linspace(0, 10, 20)
y1 = x + 1
y2 = x + 2
y3 = x + 3
y4 = x + 4
y5 = x + 5
y6 = x + 6
y7 = x + 7

plt.figure()
plt.plot(x, y1, 'bo')
plt.plot(x, y2, 'r-')
plt.plot(x, y3, 'g--')
plt.plot(x, y4, 'y.-')
plt.plot(x, y5, 'm^', x, y6, 'm-')
plt.plot(x, y7, 'c-', linewidth=6)

plt.show()
```

这里可供实验的东西实在太多，只要知道这个函数大概可以给我提供什么效果就可以了，其它的交给[API: matplotlib.pyplot.plot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)

### 1.4 坐标轴设置

设置范围和标签

```python
x = np.linspace(-10, 10, 40)
y1 = 10 * x + 50
y2 = x**2

plt.figure()
plt.plot(x, y1, 'b-')
plt.plot(x, y2, 'b--')
plt.xlim((-20, 20))
plt.ylim((-60, 160))
plt.xlabel('I am x')
plt.ylabel('I am y')

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_4_01.png)

设置刻度

```python
plt.xticks(np.linspace(-20, 20, 5))
plt.yticks([0, 50, 100], [r'$bad$', r'$normal$', r'$good$'])
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_4_02.png)

设置边框

```python
boderparameter = plt.gca()
boderparameter.spines['right'].set_color('none')
boderparameter.spines['top'].set_color('none')
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_4_03.png)

设置刻度

```python
boderparameter.xaxis.set_ticks_position('top')
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_4_04.png)

通过边框参数设置属性

```python
boderparameter.spines['left'].set_position(('data',0))
boderparameter.spines['bottom'].set_position(('data',0))
boderparameter.xaxis.set_ticks_position('bottom')
boderparameter.set_xlabel('')
boderparameter.set_ylabel('')
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_4_05.png)

### 1.5 图例设置

这里很简单，设置 $label$ 和 位置就可以了。其它可以参考文档。需要注意的一点是 $l1$ $l2$后面要加一个 `,`。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 40)
y1 = 10 * x + 50
y2 = x**2

plt.figure()
l1, = plt.plot(x, y1, 'b-')
l2, = plt.plot(x, y2, 'b--')

plt.legend(handles=[l1, l2], labels=[r'$line\ 1$', r'$line\ 2$'],  loc='best')

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_5_01.png)

### 1.6 添加注释

直接看代码，就不一一介绍了。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 40)
y = x + 5

plt.figure()
plt.plot(x, y, 'b-')

plt.xticks(np.linspace(-10, 10, 6))
plt.yticks(np.linspace(-6, 14, 6))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position('zero')

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position('zero')

x0 = 4
y0 = x0 + 5
plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)
plt.scatter([x0], [y0], color='k')

plt.annotate(r'$(%s,\ %s)$' % (x0, y0), xy=(x0, y0),
             xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.1"))

plt.text(2, 14, r'$y\ =\ x\ +\ 5$', fontdict={'size': 16, 'color': 'r'})

plt.show()
```

主要是观察倒数第二三行代码进行设置。

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_6_01.png)

### 1.7 散点图

散点图在上面标点的时候就已经用过了，这里回顾一下。

```python
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=50, c=T, alpha=.5)

plt.xlim(-2.5, 2.5)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_7_01.png)

### 1.8 柱状图

```python
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = np.random.uniform(0.1, 1.0, n)
Y2 = np.random.uniform(0.1, 1.0, n)

plt.bar(X, +Y1)
plt.bar(X, -Y2)

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

for x, y in zip(X, Y1):
    plt.text(x, y + 0.02, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x, -y - 0.02, '%.2f' % y, ha='center', va='top')

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_8_01.png)

### 1.9 饼状图

```python
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
colors = ['y', 'g', 'c', 'm']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_9_01.png)

### 1.10 等高线

```python
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, f(X, Y), 12, alpha=.9, cmap=plt.cm.coolwarm)

C = plt.contour(X, Y, f(X, Y), 12, colors='black')

plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_10_01.png)

### 1.11 图像

```python
import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(2, 1, 16).reshape(4, 4)

plt.imshow(a, interpolation='nearest', cmap='coolwarm', origin='lower')

plt.colorbar(shrink=.98)

plt.xticks(())
plt.yticks(())
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_11_01.png)

### 1.12 3D

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

ax.contourf(X, Y, Z, zdir='x', offset=-5, cmap=plt.get_cmap('rainbow'))

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_12_01.png)

### 1.13 子图

```python
import matplotlib.pyplot as plt

# example 1:
###############################
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(222)
plt.plot([0, 1], [0, 2])

plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])

plt.tight_layout()

# example 2:
###############################
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(2, 1, 1)
# figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.plot([0, 1], [0, 1])

plt.subplot(234)
# figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.plot([0, 1], [0, 2])

plt.subplot(235)
# figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.plot([0, 1], [0, 3])

plt.subplot(236)
# figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.plot([0, 1], [0, 4])


plt.tight_layout()
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_13_01.png)

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_13_02.png)

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1: subplot2grid
##########################
plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))

# method 2: gridspec
#########################
plt.figure()
gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

# method 3: easy to define structure
####################################
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])

plt.tight_layout()
plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_13_03.png)

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_13_04.png)

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_13_05.png)

### 1.14 图中图

```python
import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# below are all percentage
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')


# different method to add axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_14_01.png)

### 1.15 第二 Y 坐标

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 *y1

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()    # mirror the ax1
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_15_01.png)

### 1.16 动画

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x))
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

ani.save('myanimation.gif', writer='imagemagick')

plt.show()
```

![img](/home/zzhenry/Boostnote/Python/Matplotlib 基本操作.assets/1_16_01.gif)

## 2. 总结

花时间把小细节搞懂就是节省时间。

## 3. 参考资料

- [morvan：markdown + 视频](https://morvanzhou.github.io/tutorials/data-manipulation/plt/)
- [官方文档](https://matplotlib.org/tutorials/index.html)