# matlab 字符串拼接

在Matlab中，想要将两个字符串连接在一起，有以下的方法：

假定有两个字符串 `Iloveyou` `123`

```matlab
>> str1='Iloveyou'; str2='123';
```

### 方法一：用中括号将str1和str2像矩阵元素一样包含起来：

```matlab
>> SC=[str1,str2]
>> SC =
Iloveyou123
```

（若想验证str1和str2确实被连接起来，可调用length函数测试SC的长度。）

### 方法二：用strcat函数

```matlab
>> SB=strcat(str1,str2)
SB =
Iloveyou123
```

**注意**，strcat函数有许多用法，如下例：

```matlab
>> strcat({'Red','Yellow'},{'Green','Blue'})
ans =

    'RedGreen'    'YellowBlue'
```

但下句则结果就不一样了：

```matlab
>> strcat(['Red','Yellow'],['Green','Blue'])
ans =

RedYellowGreenBlue
```

### 方法三：利用sprintf函数

```matlab
>> number=123;

>> STR=sprintf('%s%d',str1,number)
STR =

Iloveyou123
```