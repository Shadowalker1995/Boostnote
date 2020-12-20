# Latex 语法学习

<details><summary>I have keys but no locks. I have space but no room. You can enter but can't leave. What am I?</summary>     A keyboard. </details>

- **点乘：**

  <center><span style='font-family:monospace'>a \cdot b</span></center>
  
$$
  a \cdot b
$$

- **分子分母线：**

  <center><span style='font-family:monospace'>\frac{分子}{分母}</span></center>
  
$$
  \frac{分子}{分母}
$$



- **上下标：**

  <center><span style='font-family:monospace'>x_{1}^{2}</span></center>

  $$
x_{1}^{2}
  $$
  
- **根号：**

  <center><span style='font-family:monospace'>\sqrt{n}</span></center>

  $$
  \sqrt{n}
  $$

- **大于等于、小于等于：**

  <center><span style='font-family:monospace'>a \geq b\\</br>
  a \leq b</span></center>


$$
  a \geq b\\
  a \leq b
$$

- **组合数($$C_{n}^{m}$$)**

  <center><span style='font-family:monospace'>\tbinom{n}{m}</span></center>

  <center><span style='font-family:monospace'>C_{n}^{m} 不推荐</span></center>
  
  $$
\tbinom{n}{m} \\
  

C_{n}^{m}
$$
## 常用数学符号的 LaTeX 表示方法

1. 指数和下标可以用`^`和`_`后加相应字符来实现。比如：

    <center><span style='font-family:monospace'>a{1} \qquad x^{2} \qquad</br>
    e^{-\alpha t} \qquad</br>
    a^3{ij} \\</br>
    e^{x^2} \neq {e^x}^2</span></center>
$$
a{1} \qquad x^{2} \qquad
e^{-\alpha t} \qquad
a^3{ij} \\
e^{x^2} \neq {e^x}^2
$$
2. 平方根 (square root) 的输入命令为：`\sqrt`，n 次方根相应地为: `\sqrt[n]`。方根符号的大小由LATEX自动加以调整。也可用`\surd` 仅给出符号。比如：

    <center><span style='font-family:monospace'>\sqrt{x} \qquad </br>
        \sqrt{ x^{2}+\sqrt{y} } \qquad </br>
    \sqrt [3] {2} \\[3pt] </br>
    \surd [x^2 + y^2]</span></center>
$$
\sqrt{x} \qquad
\sqrt{ x^{2}+\sqrt{y} } \qquad
\sqrt [3] {2} \\[3pt]
\surd [x^2 + y^2]
$$
3. 命令`\overline`  和 `\underline` 在表达式的上、下方画出水平线。比如：

    <center><span style='font-family:monospace'>\overline{m+n} \qquad</br>
    \underline{m+n}</span></center>
$$
\overline{m+n} \qquad
\underline{m+n}
$$
4. 命令 `\overbrace` 和 `\underbrace` 在表达式的上、下方给出一水平的大括号。

    <center><span style='font-family:monospace'>\underbrace{ a+b+\cdots+z }_{26}</span></center>
$$
\underbrace{ a+b+\cdots+z }_{26}
$$
5. 向量 (Vectors) 通常用上方有小箭头 (arrow symbols) 的变量表示。这可由 `\vec` 得到。另两个命令`\overrightarrow` 和 `\overleftarrow` 在定义从A 到B 的向量时非常有用。

    <center><span style='font-family:monospace'>\vec a\quad \overrightarrow{AB}</span></center>
$$
\vec a\quad \overrightarrow{AB}
$$
6. 分数 (fraction) 使用 `\frac{...}{...}` 排版。一般来说，1/2 这种形式更受欢迎，因为对于少量的分式，它看起来更好些。

    <center><span style='font-family:monospace'>1\frac{1}{2} ~hours\\ </br>
    \frac{ x^{2} }{ k+1 } \qquad </br>
    x^{ \frac{2}{k+1} } \qquad </br>
    x^{ 1/2 }</span></center>
$$
1\frac{1}{2} ~hours\\
\frac{ x^{2} }{ k+1 } \qquad
x^{ \frac{2}{k+1} } \qquad
x^{ 1/2 }
$$
7. 积分运算符 (integral operator) 用 `\int` 来生成。求和运算符 (sum operator) 由 `\sum` 生成。乘积运算符 (product operator) 由 `\prod` 生成。上限和下限用 `^` 和 `_` 来生成，类似于上标和下标。

    <center><span style='font-family:monospace'>\sum_{i+1}^{n} \qquad </br>
    \int_{0}^{\frac{\pi}{2}} \qquad </br>
    \prod_\epsilon</span></center>
$$
\sum_{i+1}^{n} \qquad
\int_{0}^{\frac{\pi}{2}} \qquad
\prod_\epsilon
$$

## 以下提供一些常用符号的表示方法

![img](assets/1.GIF)

![img](assets/2.GIF)
$$
\int_{0}^{\frac{\pi}{2}}
$$


![img](assets/3.GIF)

![img](assets/4.GIF)

![img](assets/5.GIF)

![img](assets/6.GIF)

![img](assets/7-1529038509748.GIF) 