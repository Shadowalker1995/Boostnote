# MarkDown 中的数学公式

## 0. 前言

> 这里尽量详细地纪录在MarkDown语法中插入数学公式的技巧和经验，方便以后查阅。

## 1. 基础认识

这里我们选取 MathJax 引擎。

引入脚本，把下面代码插入 MD 文件里面，如果你怕这份在线文件源别人访问不到的话，可以把这个下下来自己做一个源，这样比较稳定缺点是要自己手动更新源。

```
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
```

好了到这里就可以插入公式了，如果你懂 LaTeX 的话那看一两个例子就知道了，不懂也没关系，自己写一写代码就知道了，可以找一个可以预览 MD 的工具一直尝试。

### 1.1 插入方式

这里分两种，一种是行间插入，另一种是另取一行

#### 1.1.1 行间插入

```latex
$a + b$
```

这里是行间插入公式 a + b : $a + b$

#### 1.1.2 另取一行

```latex
$$a + b$$
```

这里是另取一行

$$a + b$$

特点就是通过`$$`包含公式。

笔者认为第二种方式更好，以下没看 JS 源码纯属猜测：行间的需要考虑到当前行的行高并对公式进行处理，而另取一行就更简单一些，可能解析起来更快。

### 1.2 基本类型的插入

#### 1.2.1 上、下标

先看结果再总结语法吧。

```latex
$$x_1$$

$$x_1^2$$

$$x^2_1$$

$$x_{22}^{(n)}$$

$${}^*x^*$$

$$x_{balabala}^{bala}$$
```

$$x_1$$

$$x_1^2$$

$$x^2_1$$

$$x_{22}^{(n)}$$

$${}^*x^*$$

$$x_{balabala}^{bala}$$

可以看到 `x` 元素的上标通过 `^` 符号后接的内容体现，下表通过 `_`符号后接的内容体现，多于一位是要加 `{}` 包裹的。

习惯上是先下标后上标的写法：`x_{balabala}^{bala}`

#### 1.2.2 分式

```latex
$$\frac{x+y}{2}$$

$$\frac{1}{1+\frac{1}{2}}$$
```

$$\frac{x+y}{2}$$

$$\frac{1}{1+\frac{1}{2}}$$

这里可以试试分数的行间解析 $\frac{1}{1+\frac{1}{2}}$。我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果我要看行间填充效果。

#### 1.2.3 根式

```latex
$$\sqrt{2}<\sqrt[3]{3}$$

$$\sqrt{1+\sqrt[p]{1+a^2}}$$

$$\sqrt{1+\sqrt[^p\!]{1+a^2}}$$
```

$$\sqrt{2}<\sqrt[3]{3}$$

$$\sqrt{1+\sqrt[p]{1+a^2}}$$

$$\sqrt{1+\sqrt[^p\!]{1+a^2}}$$

#### 1.2.4 求和、积分

```latex
$$\sum_{k=1}^{n}\frac{1}{k}$$

$$\int_a^b f(x)dx$$
```

$$\sum_{k=1}^{n}\frac{1}{k}$$

$$\int_a^b f(x)dx$$

这里很容易看出求和函数表达式 `sum_{起点}^{终点}表达式`，积分函数表达式 `int_下限^上限 被积函数d被积量`。还有一个有趣的是行间的公式都被压缩了。

#### 1.2.5 空格

```latex
紧贴 $a\!b$

没有空格 $ab$

小空格 $a\,b$

中等空格 $a\;b$

大空格 $a\ b$

quad空格 $a\quad b$

两个quad空格 $a\qquad b$

```

- 紧贴 $a\!b$
- 没有空格 $ab$
- 小空格 $a\,b$
- 中等空格 $a\;b$
- 大空格 $a\ b$
- quad空格 $a\quad b$
- 两个quad空格 $a\qquad b$

这个直接看上面的文字，介绍很清楚，主要指微调距离，使得公式更加漂亮。请比较下面的积分公式：

```latex
$$\int_a^b f(x)\mathrm{d}x$$

$$\int_a^b f(x)\,\mathrm{d}x$$
```

$$\int_a^b f(x)\mathrm{d}x$$

$$\int_a^b f(x)\,\mathrm{d}x$$

#### 1.2.6 公式界定符

主要符号有

$$($$

$$)$$

$$[$$

$$]$$

$$\{$$

$$\}$$

$$|$$

$$||$$

那么如何使用呢？

通过 `\left` 和 `\right` 后面跟界定符来对同时进行界定。

```latex
$$\left(\sum_{k=\frac{1}{2}}^{N^2}\frac{1}{k}\right)$$
```

 $$\left(\sum_{k=\frac{1}{2}}^{N^2}\frac{1}{k}\right)$$

#### 1.2.7 矩阵

```latex
$$\begin{matrix}1 & 2\\\\3 & 4\end{matrix}$$

$$\begin{pmatrix}1 & 2\\\\3 & 4\end{pmatrix}$$

$$\begin{bmatrix}1 & 2\\\\3 & 4\end{bmatrix}$$

$$\begin{Bmatrix}1 & 2\\\\3 & 4\end{Bmatrix}$$

$$\begin{vmatrix}1 & 2\\\\3 & 4\end{vmatrix}$$

$$\left|\begin{matrix}1 & 2\\\\3 & 4\end{matrix}\right|$$

$$\begin{Vmatrix}1 & 2\\\\3 & 4\end{Vmatrix}$$
```

$$\begin{matrix}1 & 2\\\\3 &4\end{matrix}$$

$$\begin{pmatrix}1 & 2\\\\3 &4\end{pmatrix}$$

$$\begin{bmatrix}1 & 2\\\\3 &4\end{bmatrix}$$

$$\begin{Bmatrix}1 & 2\\\\3 &4\end{Bmatrix}$$

$$\begin{vmatrix}1 & 2\\\\3 &4\end{vmatrix}$$

$$\left|\begin{matrix}1 & 2\\\\3 &4\end{matrix}\right|$$

$$\begin{Vmatrix}1 & 2\\\\3 &4\end{Vmatrix}$$

类似于 `left` `right`，这里是 `begin` 和 `end`。而且里面有具体的矩阵语法，`&` 区分行间元素，`\\` 代表换行。可以理解为 HTML 的标签之类的。

#### 1.2.8 排版数组

```latex
$$
\mathbf{X} =
\left( \begin{array}{ccc}
x_{11} & x_{12} & \ldots \\
x_{21} & x_{22} & \ldots \\
\vdots & \vdots & \ddots
\end{array} \right)
$$
```

$$
\mathbf{X} =
\left( \begin{array}{ccc}
x_{11} & x_{12} & \ldots \\
x_{21} & x_{22} & \ldots \\
\vdots & \vdots & \ddots
\end{array} \right)
$$

## 2. 常用公式举例

> 持续更新……

### 2.1 多行公式

> 主要是各种方程的表达

#### 2.1.1 长公式

```latex
$$
\begin{multline}
x = a+b+c+{} \\
d+e+f+g
\end{multline}
$$

$$
\begin{aligned}
x ={}& a+b+c+{} \\
&d+e+f+g
\end{aligned}
$$
```

不对齐

$$
\begin{multline}
x = a+b+c+{} \\
d+e+f+g
\end{multline}
$$
对齐

$$
\begin{aligned}
x ={}& a+b+c+{} \\
&d+e+f+g
\end{aligned}
$$

#### 2.1.2 公式组

```latex
$$
\begin{gathered}
a = b+c+d \\
x = y+z
\end{gathered}
$$

$$
\begin{aligned}
a &= b+c+d \\
x &= y+z
\end{aligned}
$$
```

$$
\begin{gathered}
a = b+c+d \\
x = y+z
\end{gathered}
$$

$$
\begin{aligned}
a &= b+c+d \\
x &= y+z
\end{aligned}
$$

#### 2.1.3 分段函数

```latex
$$
y=\begin{cases}
-x,\quad x\leq 0 \\\\
x,\quad x>0
\end{cases}
$$
```

$$
y=\begin{cases}
-x,\quad x\leq 0 \\\\
x,\quad x>0
\end{cases}
$$

里面用到了 `≤` 符号，下一章会介绍常用数学符号。

#### 2.1.4 块级公式的编号

- 使用 `\tag{...}` 标签就可以生成对应的编号。

这样的代码

```latex
$$x^n+y^n=z^n \tag{1.1}$$
```

可以生成如

$$x^n+y^n=z^n \tag{1.1}$$

的编号块级公式。

- 对于需要**自动编号**的公式，需要使用 `\begin{equation}...\end{equation}` 将代码快包围起来。

```latex
$$\begin{equation}
x^n+y^n=z^n
\end{equation}$$
```

$$
\begin{equation}
x^n+y^n=z^n
\end{equation}
$$

因为自动编号的代码较为复杂，而且不易扩展，所以不太建议使用自动编号，手动编号更易维护。

#### 2.1.5 公式换行

单个公式很长的时候需要换行，但仅允许生成一个编号时，可以用 `split` 标签包围公式代码，在需要转行的地方使用 `\\`，每行需要使用1个 `&` 来标识对齐的位置，结束后可使用 `\tag{...}` 标签编号。

```latex
$$
\begin{split}
a &= b \\
c &= d \\
e &= f 
\end{split}\tag{1.3}
$$
```

$$
\begin{split}
a &= b \\
c &= d \\
e &= f 
\end{split}\tag{1.3}
$$

注意：每行只允许出现一个`&`，使用`split`标签后，编号会**上下居中**显示。

#### 2.1.6 多行的独立公式

有时候需要罗列多个公式，可以用 `eqnarray*` 标签包围公式代码，在需要转行的地方使用 `\\`，每行需要使用2个 `&`来标识对齐位置，两个 `&...&` 号之间的是公式间对齐的位置，每行公式后可使用 `\tag{...}` 标签编号：

```latex
$$
\begin{eqnarray*}
x^n+y^n &=& z^n \tag{1.4} \\
x+y &=& z \tag{1.5}
\end{eqnarray*}
$$
```

$$
\begin{eqnarray*}
x^n+y^n &=& z^n \tag{1.4} \\
x+y &=& z \tag{1.5}
\end{eqnarray*}
$$

### 2.2 数组的其他使用

#### 2.2.1 划线

```latex
$$
\left(\begin{array}{|c|c|}
1 & 2 \\\\
\hline
3 & 4
\end{array}\right)
$$
```

$$
\left(\begin{array}{|c|c|}
1 & 2 \\\\
\hline
3 & 4
\end{array}\right)
$$

#### 2.2.2 制表

```
$$
\begin{array}{|c|c|}
\hline
{1111111111} & 2 \\\\
\hline
3 & 4 \\\\
\hline
\end{array}
$$
```

$$
\begin{array}{|c|c|}
\hline
{1111111111} & 2 \\\\
\hline
3 & 4 \\\\
\hline
\end{array}
$$

可以看到，其实其他很多东西都可以很灵活的表达出来。

## 3. 常用数学符号

> 这里提供一个[文档下载](http://files.cnblogs.com/houkai/LATEX%E6%95%B0%E5%AD%A6%E7%AC%A6%E5%8F%B7%E8%A1%A8.rar)，如果上面的链接失效，也可以到我的 [GitHub 下载 pdf 版](https://github.com/mk43/BlogResource/blob/master/LaTex/LATEX%E6%95%B0%E5%AD%A6%E7%AC%A6%E5%8F%B7%E8%A1%A8.pdf)。下面举几个例子。

### 3.1 希腊字母

```latex
$$
\begin{array}{|c|c|c|c|c|c|c|c|}
\hline
{\alpha} & {\backslash alpha} & {\theta} & {\backslash theta} & {o} & {o} & {\upsilon} & {\backslash upsilon} \\\\
\hline
{\beta} & {\backslash beta} & {\vartheta} & {\backslash vartheta} & {\pi} & {\backslash pi} & {\phi} & {\backslash phi} \\\\
\hline
{\gamma} & {\backslash gamma} & {\iota} & {\backslash iota} & {\varpi} & {\backslash varpi} & {\varphi} & {\backslash varphi} \\\\
\hline
{\delta} & {\backslash delta} & {\kappa} & {\backslash kappa} & {\rho} & {\backslash rho} & {\chi} & {\backslash chi} \\\\
\hline
{\epsilon} & {\backslash epsilon} & {\lambda} & {\backslash lambda} & {\varrho} & {\backslash varrho} & {\psi} & {\backslash psi} \\\\
\hline
{\varepsilon} & {\backslash varepsilon} & {\mu} & {\backslash mu} & {\sigma} & {\backslash sigma} & {\omega} & {\backslash omega} \\\\
\hline
{\zeta} & {\backslash zeta} & {\nu} & {\backslash nu} & {\varsigma} & {\backslash varsigma} & {} & {} \\\\
\hline
{\eta} & {\backslash eta} & {\xi} & {\backslash xi} & {\tau} & {\backslash tau} & {} & {} \\\\
\hline
{\Gamma} & {\backslash Gamma} & {\Lambda} & {\backslash Lambda} & {\Sigma} & {\backslash Sigma} & {\Psi} & {\backslash Psi} \\\\
\hline
{\Delta} & {\backslash Delta} & {\Xi} & {\backslash Xi} & {\Upsilon} & {\backslash Upsilon} & {\Omega} & {\backslash Omega} \\\\
\hline
{\Omega} & {\backslash Omega} & {\Pi} & {\backslash Pi} & {\Phi} & {\backslash Phi} & {} & {} \\\\
\hline
\end{array}
$$
```

$$
\begin{array}{|c|c|c|c|c|c|c|c|}
\hline
{\alpha} & {\backslash alpha} & {\theta} & {\backslash theta} & {o} & {o} & {\upsilon} & {\backslash upsilon} \\\\
\hline
{\beta} & {\backslash beta} & {\vartheta} & {\backslash vartheta} & {\pi} & {\backslash pi} & {\phi} & {\backslash phi} \\\\
\hline
{\gamma} & {\backslash gamma} & {\iota} & {\backslash iota} & {\varpi} & {\backslash varpi} & {\varphi} & {\backslash varphi} \\\\
\hline
{\delta} & {\backslash delta} & {\kappa} & {\backslash kappa} & {\rho} & {\backslash rho} & {\chi} & {\backslash chi} \\\\
\hline
{\epsilon} & {\backslash epsilon} & {\lambda} & {\backslash lambda} & {\varrho} & {\backslash varrho} & {\psi} & {\backslash psi} \\\\
\hline
{\varepsilon} & {\backslash varepsilon} & {\mu} & {\backslash mu} & {\sigma} & {\backslash sigma} & {\omega} & {\backslash omega} \\\\
\hline
{\zeta} & {\backslash zeta} & {\nu} & {\backslash nu} & {\varsigma} & {\backslash varsigma} & {} & {} \\\\
\hline
{\eta} & {\backslash eta} & {\xi} & {\backslash xi} & {\tau} & {\backslash tau} & {} & {} \\\\
\hline
{\Gamma} & {\backslash Gamma} & {\Lambda} & {\backslash Lambda} & {\Sigma} & {\backslash Sigma} & {\Psi} & {\backslash Psi} \\\\
\hline
{\Delta} & {\backslash Delta} & {\Xi} & {\backslash Xi} & {\Upsilon} & {\backslash Upsilon} & {\Omega} & {\backslash Omega} \\\\
\hline
{\Omega} & {\backslash Omega} & {\Pi} & {\backslash Pi} & {\Phi} & {\backslash Phi} & {} & {} \\\\
\hline
\end{array}
$$

写太累了😂😂😂。。。其他的详见 [PDF](https://github.com/mk43/BlogResource/blob/master/LaTex/LATEX%E6%95%B0%E5%AD%A6%E7%AC%A6%E5%8F%B7%E8%A1%A8.pdf)。

## 4. 总结

> 通过这样梳理一下基本的公式都能插入了，而且也会如何查资料。对于自己日后学习 LaTeX 写论文有很大帮助。以下建议带有很强的主观性，仅供参考。

- 公式一律使用另取一行，并且上下都空一行
- 一个公式一个语句，不要写在一个 `$$***$$` 里，保证 `独立性`，一个公式错误不影响另一个公式。
- 风格统一，不要混用。比如上下标的写法：`x_{balabala}^{bala}`
- 行间字母可以使用 `$a$` 代替 `a` ，养成自己的写作风格。

## 5. 参考资料

> 十分感谢以下作者的无私分享。

1. [MarkDown 插入数学公式实验大集合](http://fitzeng.org/2018/01/23/LaTexFormula/)
2. [Markdown中插入数学公式的方法](http://blog.csdn.net/xiahouzuoxin/article/details/26478179)
3. [LATEX数学公式基本语法](http://www.cnblogs.com/houkai/p/3399646.html)
4. [一份其实很短的 LaTeX 入门文档](https://liam0205.me/2014/09/08/latex-introduction/)
