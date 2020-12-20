# Vim 使用技巧总结

## 0x00 Vim模式

Vim可分为3种模式，分别是Normal模式、Visual模式和Insert模式。以下的基本操作都是在Normal模式进行。三种模式的区别这里不详解了，Bing搜索有很多相关的基础教程。
三者的关系可用下图简单描述

![img](https://mmbiz.qpic.cn/mmbiz_jpg/k2yQfhlbU3rugw073ibYs1LelJibkQMzkQRndvGRjM3WNCrJUlrSCIsmEC8rPic2OTfwblj2e6AJn8TG8lyBSTLXA/?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

## 0x01 基本操作

### 光标移动

注意区分字母大小写

#### 上下左右

直接看表格，简单易懂。一开始会有点别扭，但是熟悉之后你会爱上他的。

|          | k（上）  |          |
| -------- | -------- | -------- |
| h （左） |          | l （右） |
|          | j （下） |          |

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download.gif)

#### 单词间定位

键位

> 如果是大写，则单词允许包含标点
> w（向前跳到单词词首）
> e（向前跳到单词词尾）
> b（向后跳到单词词首）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634758120.gif)

#### 行内定位

键位

> $（定位到行尾）
> 0（定位到行首）
> ^（定位到行首，忽略空格）
> f 正向搜索ch字符，ch如果是字母则区分大小写
> F 反向搜索ch字符，ch如果是字母则区分大小写

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634771551.gif)

#### 块定位

键位

> {（跳到上一个代码块）
> }（跳到下一个代码块）
> %（定位到另一个匹配的括号）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634784547.gif)

#### 页面定位

键位

> gg（定位到页面的第一行）
> G（定位到页面的最后一行）
> H（定位到当前页面的顶部，High首字母大写）
> M（定位到当前页面的中部，Middle首字母大写）
> L（定位到当前页面的底部，Low首字母大写）
>
> nG或ngg（定位到指定行，n表示行数，需大于0，
> 如果大于最大行数，则会直接跳转到页面最后一行）
>
> m<a>和'<a>（这是一对很强大的命令，可标记一个位置，然后在同页面快速定位到该标志。m表示mark，a是一个字母，可以是26字母的其中一个，'是单引号，后面跟上前面标记的字母）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634816159.gif)

### 0x02 屏幕滚动

#### 整屏滚动

键位

> Ctrl + f （向下滚动一屏内容，Foward首字母小写）
> Ctrl + b （向上滚动一屏内容，Backward首字母小写）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634854107.gif)

#### 半屏滚动

键位

> Ctrl + d（向下滚动半屏内容，Down首字母小写）
> Ctrl + u（向上滚动半屏内容，Up首字母小写）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634862058.gif)

#### 行滚动

键位

> Ctrl + e（向下滚动一行内容） 
> Ctrl + y（向上滚动一行内容）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634870082.gif)

### 0x03 编辑模式

#### 插入

键位

> i（在光标处插入，insert首字母小写）
> I（在行首插入，insert首字母大写）
> a（在光标处后一个字符插入，append首字母小写）
> A（在行尾插入，append首字母大写）
> o（在上一行插入）
> O（在下一行插入）
> cc/S（清除当前行并进入插入模式）
> s（清除当前字符并进入插入模式）

恩，这个很简单，就不贴图了。

#### 查找

键位

> /pattern（正向查找）
> ?pattern（反向查找）
> n（查找下一个）
> N（查找上一个）
> *（当光标定位在某个单词时，查找下一个该单词）
> \#（当光标定位在某个单词时，查找上一个该单词）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634887171.gif)

#### 替换

键位

> :%s/old/new/g（全局替换old为new）
> :s/old/new/g（替换当前行old为new）

**注意，替换操作仅在当前页面生效，使用该替换操作需谨慎。建议使用IDE自带的重命名操作，可以将对应的引用也一起重命名！**

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634897447.gif)

#### 剪切、复制、粘贴

键位

> dd（剪切当前行的内容）
> D（剪切光标后到行尾的内容）
> yy/Y（复制当前行的内容）
> p（粘贴到光标后）
> P（粘贴到光标前）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634905950.gif)

#### 撤销

键位

> u（撤销上一步，IDE一般都是Cmd + Z）

这个简单，也不贴图了。

## 0x04 组合操作

组合操作可以看作是op+i/a+scope公式的应用，解释一下这个公式，op就是我们前面提到的插入（c）、剪切（d）、复制（y）以及还未提到的选择（v），i表示scope范围内，a表示包含scope标签，scope就是操作的范围了。这样讲比较抽象，下面举例几个常用组合。

### 选择文本

键位

> 以下如果将i换成a，则会将符号也包含进去
> vib（选中小括号内的内容）
> viB（选中大括号内的内容）
> vi"（选中双引号内的内容）
> vi'（选中单引号内的内容）
> vi<（选中尖括号内的内容）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634924023.gif)

同理，将选择操作（v）替换成插入（c）、剪切（d）或者复制（y），也能实现类似的效果。

## 0x05 神奇操作

IDE支持跳转到变量（方法）的定义处或者调用处，Vim也支持，而且也很方便。只需要将光标定位到方法名，然后输入`gd`即可。配合Android Studio的Navigate Back，可以十分方便地查看方法的调用。

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download-1528634952902.gif)

Navigate Back设置

![img](/home/zzhenry/Boostnote/Ubuntu/assets/download)

## 0x06 总结

当掌握了Vim，以后如果使用了新的IDE或者开发环境，只要支持Vim，我们就能很快的熟悉开发环境。当然，很多IDE提供了更完善的快捷键，笔者的观点是，Vim和IDE配合着使用，互补缺点。

## 0x07 参考链接

- https://jasonliao.me/posts/2016-08-09-you-dont-know-vim.html
- https://vim.rtorr.com/lang/zh_cn/
- https://mp.weixin.qq.com/s/w35pfdETK7mr19w_O5FOZg