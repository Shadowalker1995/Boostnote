# MATLAB split 字符串分割

我们在这里借助正则表达式函数regexp的split模式。一般语法：

```matlab
S = regexp(str, char, 'split')
```

其中str是待分割的字符串，char是作为分隔符的字符（可以使用正则表达式）。分割出的结果存在S中。

以下面这样一串字符为例

Hello       Nocturne       Studio

首先去除首尾的多余空格：

```matlab
str = deblank(str)
```

例1：设这几个字符串是以制表符分隔的，可以这样来做：

```matlab
S = regexp(str, '\t', 'split')
```

例2：设这些字符串是以一个或多个空格分隔的，可以用正则表达式来描述：

```matlab
S = regexp(str, '\s+', 'split')
```

这样，`S{1}='Hello'，S{2}='Nocturne'，S{3}='Studio'`。 

注意，上面得到的结果S是一个cell型变量，它的每个元素比如S{1}仍然是cell型的，只能用来display，不能直接用来进行字符串操作（比如获取其中的某个字符），所以我们在使用需要执行一次：

```matlab
s1 = char(S{1})
```

这样的s1才是一个真正的字符串，可以进行后续的操作。