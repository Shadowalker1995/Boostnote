# Typora软件学习总结

[TOC]

### 安装

```shell
# optional, but recommended
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io linux/'
sudo apt-get update
# install typora
sudo apt-get install typora
```

### 数学表达式

要启用这个功能，首先到`Preference`->`Editor`中启用。然后使用`$`符号包裹Tex命令，例如：`$lim_{x \to \infty} \ exp(-x)=0$`将产生如下的数学表达式：$lim_{x \to \infty} \ exp(-x)=0$

Typora支持Latex的公式编辑，公式编辑几乎和代码编辑的使用方法相同，同样分行内公式和行间公式，行内公式用两个`$`包裹起来，行间公式可以使用`$$ + enter`插入：
$$
lim_{x \to \infty} \ exp(-x)=0
$$

### 下标

下标使用`~`包裹，例如：`H~2~O`将产生水的分子式。

H~2~O

### 上标

上标使用`^`包裹，例如`X^2^`将产生：

X^2^

### 插入表情

使用`:happy:`输入高兴的表情，使用`:cry:`输入哭的表情等。以此类推！

:happy:

:cry:

### 下划线

用HTML的语法`<u>underline</u>`将产生下划线Underline.

<u>underline</u>

### 删除线

GFM添加了删除文本的语法，这是标准的Markdown语法木有的。使用`~~`包裹的文本将会具有删除的样式，例如：

~~删除文本~~

### 代码

输入`~~~`或者“```”然后回车，可以出入代码块，并且可以选择代码的语言，例如：

~~~java
public Class HelloWorld{

  System.out.println("Hello World!");

}
~~~

### 强调

```
**使用两个*号强调内容**
__使用两个下划线强调内容__
```

**使用两个*号强调内容**
__使用两个下划线强调内容__

### 斜体

在标准的Markdown语法中，*和_包裹的内容会是斜体显示，但是GFM下划线一般用来分隔人名和代码变量名，因此我们推荐是用星号来包裹斜体内容。如果要显示星号，则使用转义：

```
\*
```

###插入图片

直接把图片拖进来就可以了！（Ps：如果你单击图片还能显示 Markdown 格式以及图片的本地路径）。

但是这个功能默认是关闭的需要在设置中手动开启，设置的路径为`Preferences -> Editor`，在`Image Drag & Drop`后打上勾就可以了，如图所示：

![img](http://upload-images.jianshu.io/upload_images/1182605-1cbd9bb6f1ed0be4.gif?imageMogr2/auto-orient/strip)

### 插入URL链接

使用尖括号包裹的url将产生一个连接，例如：`<www.baidu.com>`将产生链接：<www.baidu.com>

如果是标准的url，则会自动产生连接，例如：www.google.com

### 目录列表Table of Contents（TOC）

输入[toc]然后回车，将会产生一个目录，这个目录抽取了文章的所有标题，自动更新内容。

### 水平分割线

使用`***`或者`---`，然后回车，来产生水平分割线。

### 标注

我们可以对某一个词语进行标注。例如

```
某些人用过了才知道[^注释]
[^注释]:Somebody that I used to know.
```

某些人用过了才知道[^注释]

### 表格

```
|姓名|性别|毕业学校|工资|
|:---|:---:|:---:|---:|
|杨洋|男|重庆交通大学|3200|
|峰哥|男|贵州大学|5000|
|坑货|女|北京大学|2000|
```

其中代码的第二行指定对齐的方式，第一个是左对齐，第二个和第三个是居中，最后一个是右对齐。

| 姓名 | 性别 |   毕业学校   | 工资 |
| :--- | :--: | :----------: | ---: |
| 杨洋 |  男  | 重庆交通大学 | 3200 |
| 峰哥 |  男  |   贵州大学   | 5000 |
| 坑货 |  女  |   北京大学   | 2000 |

使用快捷键`ctrl+T`可以快速插入表格，最上面可以选择行列数、没一列的对齐方式，并且支持在表格中使用`tab`键跳到下一单元格。

### 数学表达式块

输入两个美元符号，然后回车，就可以输入数学表达式块了。例如：

```latex
$$\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\\end{vmatrix}$$
```

$$\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\\end{vmatrix}$$

### 任务列表

```
- [ ] 吃饭
- [ ] 逛街
- [ ] 看电影
```

- [ ] 吃饭
- [ ] 逛街
- [ ] 看电影

### 列表

输入+, -, *,创建无序的列表，使用任意数字加`.`开头，创建有序列表，例如：

```
**无序的列表**
* tfboys
* 杨洋
* 我爱你
```

* tfboys
* 杨洋
* 我爱你
  1. tfboys
  2. 杨洋
  3. 我爱你

### 块引用

使用`>`来插入块引用。例如：

> 这是一个块引用！

### 标题

使用#表示一级标题，##表示二级标题，以此类推，有6个标题。

------

[^注释]: Somebody that I used to know.

