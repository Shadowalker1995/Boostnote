# MATLAB save函数的使用

**MATLAB储存变数的基本命令是save，在不加任何选项(Options)时，save会将变量以二进制(Binary)的方式储存至扩展名为mat的档案，如下述：**

- `save`：将工作空间的所有变量储存到名为matlab.mat的二进制档案。
- `save filename`：将工作空间的所有变量储存到名为filename.mat的二进制档案。
- `save filename x y z`：将变量x、y、z储存到名为filename.mat的二进制档案。

以下为使用save命令的一个简例：

```matlab
>> a =[1 2 3]
a =

 1     2     3

>> b=[2 3 4;4 5 6]
b =

2     3     4

4     5     6

>> save %就会产生一个名为mtalb.mat的文件 包括所有变量
Saving to: D:\USER\Desktop\matlab.mat

>> save test1  %就会产生一个名为test1.mat的文件 包括所有变量

>> save test1 a  %就会产生一个名为test1.mat的文件 包括变量a
```

**以二进制的方式储存变量，通常档案会比较小，而且在载入时速度较快，但是就无法用普通的文书软体看到档案内容。若想看到档案内容，则必须加上-ascii选项，详见下述：**

- `save filename x -ascii`：将变量x以八位数存到名为filename的ASCII档案。
- `Save filename x -ascii -double`：将变量x以十六位数存到名为filename的ASCII档案。

> 另一个选项是-tab，可将同一列相邻的数目以定位键（Tab）隔开。

小提示：二进制和ASCII档案的比较 在save命令使用-ascii选项後，会有下列现象:save命令就不会在档案名称後加上mat的扩展名。

因此以扩展名mat结尾的档案通常是MATLAB的二进位资料档。

若非有特殊需要，我们应该尽量以二进制方式储存资料。

### load命令可将档案载入以取得储存之变量：

- `load filename`：load会寻找名称为filename.mat的档案，并以二进制格式载入。若找不到filename.mat，则寻找名称为filename的档案，并以ASCII格式载入。
- `load filename -ascii`：load会寻找名称为filename的档案，并以ASCII格式载入。

若以ASCII格式载入，则变量名称即为档案名称（但不包含扩展名）。

若以二进制载入，则可保留原有的变量名称，如下例：

```matlab
clear all; % 清除工作空间中的变量  

x = 1:10;  

save testfile.dat x -ascii % 将x以ASCII格式存至名为testfile.dat的档案  

load testfile.dat % 载入testfile.dat  

who % 列出工作空间中的变量 

Your variables are:

testfile x  
```

> 注意在上述过程中，由於是以ASCII格式储存与载入，所以产生了一个与档案名称相同的变量testfile，此变量的值和原变量x完全相同。

### 如何用save命令将数据存到指定的文件夹中？

- 命令：

  `save('D:\mywork\filename.mat')` or `save D:\mywork\filename.mat`

  把工作空间中的所有变量存到D盘mywork目录下，文件名为filename.mat。

- 命令： 
  `save('D:\\mywork\\filename.mat','v1','v2',...)` or `save D:\\mywork\\filename.mat v1 v2 ...`
  把工作空间中的变量v1,v2,…存到D盘mywork目录下，文件名为filename.mat
- 命令： 
  `save('.\filename.mat','v1','v2',...)` or `save .\filename.mat v1 v2 ...`
  把工作空间中的变量v1,v2,…存到当前目录下，文件名为filename.mat
- 命令： 
  `save('..\filename.mat','v1','v2',...)` or `save ..\filename.mat v1 v2 ...`
  把工作空间中的变量v1,v2,…存到上级目录下，文件名为filename.mat
- 命令： 
  `save('..\..\filename.mat','v1','v2',...)` or `save ..\..\filename.mat v1 v2 ...`
  把工作空间中的变量v1,v2,…存到上级的上级目录下，文件名为filename.mat 
  **如果要保存二进制文件，那么文件名不需要加后缀.mat（可以将后缀写成.dat），然后加上’-ascii’选项**
- 命令： 
  `save('..\..\filename.dat','-ascii','v1','v2',...)` or `save ..\..\filename.dat -ascii v1 v2 ...`