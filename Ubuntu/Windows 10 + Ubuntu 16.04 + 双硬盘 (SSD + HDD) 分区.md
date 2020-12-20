# Windows 10 + Ubuntu 16.04 + 双硬盘 (SSD + HDD) 分区

有一种需求是双系统双硬盘(Win 10 + Linux, ssd + hdd)，那么处理好两个系统之间的关系和充分发挥ssd的功效则非常重要，网上查了很多资料，发现双硬盘双系统方面的资料相对比较少，所以本文会详细讲清楚如何在ssd+hdd硬盘上搭建Linux(Ubuntu)，并处理好与Windows的关系。好了，废话少说，开始吧！

[TOC]

## 1. 材料准备

### 1.1 Ubuntu镜像文件

> <http://www.ubuntu.com/download>

### 1.2 U盘一个，装完大小如下图，大小自己定（至少4G）

![img](/home/zzhenry/Boostnote/Ubuntu/assets/PiBello.png)

### 1.3 足够的磁盘空间(大小自己定，网上有说明)

建议至少给50-100G吧，看需求，如果一个开发SDK就要用20G，那至少也得准备60-70G吧 
我准备了SSD 70G左右 + HDD 110G左右(用作仓库）)
最终效果图如下： 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/MxoWFPH.png)

### 1.4 EasyBCD，为了系统引导 

（网上大把）

## 2. 磁盘准备

磁盘必须设置成未分配样子，也就是如上图的黑色状态，那么如何变成黑色状态呢？这里以最麻烦的逻辑分区为例：(如果是主分区直接删除该分区就变成未分配黑色了)

### 2.1 可以看到，我的整个hd盘都是扩展分区

(如果本来就是主分区，直接删除就变成未分配了，这一段就请无视)
![img](/home/zzhenry/Boostnote/Ubuntu/assets/9Z2tYAf.png)

### 2.2 将扩展分区的前部或者尾部通过拆分或者调整分区大小，转成空闲状态，如上图最左边所示

好像如果空闲分区在中间的话，转换成主分区会不可点击，我当时是这样子，所以只能放边上

### 2.3 将空闲分区建立新分区，并右键转换为主分区

![img](/home/zzhenry/Boostnote/Ubuntu/assets/7eYTZQw.png)

### 2.4 然后再删除当前分区，磁盘空间处理完毕

![img](/home/zzhenry/Boostnote/Ubuntu/assets/wVGTwrr.png)

### 2.5 最终效果图再放一遍：

![img](/home/zzhenry/Boostnote/Ubuntu/assets/Z6xlSbf.png)

## 3. 关于ubuntu分区方案

（建议提前想好怎么分区，这里贴上各分区解释，如果不想看直接跳过本段看第4点推荐方案）

### 3.1 首先贴上目录详解

/bin 存放着使用者最经常使用的命令。例如：cp,ls,cat 
/boot 这里存放的是启动LINUX时使用的一些核心文件 
/dev 所有LINUX的外部设备，其功能类似DOS下的.sys和Win下的.vxd 
/etc 这个目录用来存放所有的系统管理所需要的配置文件和子目录 
/lib 这个目录里存放着系统最基本的动态链接共享库，其作用类似于Windows里的.dll文件 
/lost+found 这个目录平时是空的，当系统不正常关机后，这里就成了一些无家可归的文件的避难所 
/mnt 这个目录是空的，系统提供这个目录是让用户临时挂载别的文件系统 
/proc 这个目录是一个虚拟的目录，它是系统内存的映射，我们可以通过直接访问这个目录来获取系统信息 
/root 系统管理员，也叫作超级权限者的用户主目录。当然系统的拥有者 
/sbin 就是Super User的意思，也就是说这里存放的是一些系统管理员使用的系统管理程序 
/tmp 这个目录不用说，一定是用来存放一些临时文件的地方了 
/usr 这是个最庞大的目录，装软件和软件的数据都在这个里面

> /usr具体说明： 
> /usr/X11R6 存放X-Windows的目录； 
> /usr/bin 存放着许多应用程序； 
> /usr/sbin 存放给超级用户使用的一些管理程序 
> /usr/doc 这就是LINUX文档的大本营 
> /usr/include 存放LINUX下开发和编译应用程序需要的头文件 
> /usr/lib 存放一些常用的动态链接共享库和静态档案库； 
> /usr/local 这是提供给一般用户的/usr目录，在这安装软件最适合 
> /usr/man 帮助文档目录 
> /usr/src LINUX开放的源代码

/opt 分区 附加程序存放地方 
/var 为了保持/usr的相对稳定的目录，经常被修改的目录可以放在这个目录下，并且系统的日志文件就在/var/log目录中

/home —-用户的主目录（类似我的文档和常用软件的自动生成的数据仓库，比如windows上QQ的本地文件什么的)。你可以把Ubuntu的“/”分区看为Windows的C盘，重装Ubuntu时只格式化“/”分区，不格式化“/home”，这样就可以保留“/home”中的数据了

/swap —-交换分区 内存不够用的时候就使用这里的空间，休眠时候也保存到这里，如果不需要休眠功能切内存大于8G的，可以禁用swap分区。需要说明的是，swap分区尽量放在机械硬盘上，如果放在SSD上也需要做一定的优化（具体原因可以自行搜索）

/ 根分区 如不独立划分以上介绍的分区，则都归于此分区

根分区 —-这里可以理解成，其实以上目录都是平行的，/分区就是我们的c盘，目录分区就是D，E，F盘。你不主动划分，那么整个硬盘就是一个C盘，你装软件也好，放数据也好，就都在这个C盘下。但是你分了区，那么根分区就是C盘，/home分区就是D盘………………/swap分区就是F盘，就是这个意思。

参考自：<http://blog.csdn.net/le284/article/details/6746981>

### 3.2 然后是分区原则

**安全的分区方案原则：** 
系统数据和普通用户数据分离放置于不同的分区 （即使用单独的 home 分区）； 
不经常变化的系统数据和经常变化的系统数据分离放置于不同的分区 
（即使用单独的 usr 分区和 var 分区） 
一般地，在一个实际系统中至少要创建单独的“/home”分区。

**所以个人建议，至少要分3个目录：** 
“/”、一个“swap”和一个“/home”的三分区方案 
如果，觉得有必要保留自己安装的软件，那么也可以为/usr单独设立一个分区

swap是交换分区，home是类似我的文档，也是很多软件默认放本地文件的位置，而其他的所有目录均是在/目录下

**关于swap分区** 
建议如果物理内存比较小（根据自己需求），建议分配实际物理内存容量2倍大小的swap；物理内存大于512MB，建议分配与物理内存等容量的swap。比如你只有2G内存，但是你平时要用到6G，那么就swap给4G；如果你平时怎么也不会用到超过4G，那swap就给2G，不过目前经济水平随随便便就上8G了。

## 4. 推荐及作者分区方案

（网上有很多分区方案，大家可以自行搜索，这个东西正所谓仁者见仁智者见智，适合自己才是最好的，这里只是贴出我觉得比较合适我的，不喜勿喷，仅供参考。） 
**所以建议采用一个“/”、一个“swap”和一个“/home”的三分区方案** 
我的双硬盘是分了70G SSD给linux系统，那么就放/和/home 
机械硬盘分了115G给linux，虽然swap分区基本上用不上，但是为了休眠，但还是给了同等内存大小的空间（我内存大小是10G，swap就给了10G，内存比较小就给到内存大小的两倍） 
剩下的自定义了一个目录，用作私人仓库。

关于boot分区，一般老一点的教程和老一点的系统会要求单独分200M给boot，并且必须挂在磁盘的开始，但是现在的系统和硬件基本都没有那些限制了，故不用考虑太多，暂时就不分boot了，要是想分也可以，这个无所谓。

**所以我的最终方案是：**

/目录：SSD剩余 
/home：15G（home放在SSD上有利于文件存储什么的，而且很多软件都是默认把工作目录放在home下，放机械太影响效率）

/自定义：机械剩余（自己做仓库用的） 
/swap：10G（机械）

（需要说明一点的是，对速度没什么要求的可以把/home放机械上，但是由于我是做Android开发的，AS自动创建的项目目录和自动创建的虚拟机文件都是home路径，而且我懒得去折腾修改路径，所以把home分了15G专门搞开发和放一些文件用，大文件就放自定义目录下了）

**另外一种推荐方案：** 
/目录：SSD 
/home：机械剩余 
/swap：10G（机械）

## 5. 制作ubuntu安装U盘

材料准备好了，分区方案自己也想好了，接下来就开始制作启动U盘 
网上有很多教程，这里我折腾了蛮久，后来发现原来我的电脑用作启动盘的时候，USB3.0的接口居然有点不兼容，老是报错，所以大家如果遇到问题可以换个接口试试。这里贴上教程链接：

> <http://jingyan.baidu.com/article/b24f6c82cf50e086bfe5dae9.html>

（亲测这个UltraISO可用，并适用于ubuntu 16.04.1，不行的请换个usb接口或者参考以下：)

> <http://www.linuxidc.com/Linux/2016-04/130520.htm>

## 6. 设置U盘启动

**BIOS设置** 
最好关闭windows的快速启动（其实不关可能也没事） 
并且在BIOS中设置U盘为第一启动项，每个电脑情况不一样，这个自己查一下。

（比如我的戴尔笔记本，没有关快速启动，也没有设置U盘第一启动，开机直接按F12选择从哪里启动，然后选U盘就行了，反正最终目标是从U盘启动，强行百度下吧）

## 7. 开始安装

### 7.1 从U盘启动后会进入如下界面

![img](/home/zzhenry/Boostnote/Ubuntu/assets/qTW3Byk.jpg)

------

### 7.2 联网，有就连上，然后是如下：(有网就尽量都勾上，否则后期还要自己更新，不然会出问题)：
![img](/home/zzhenry/Boostnote/Ubuntu/assets/rr8l86h.jpg)

------

### 7.3 选择其他选项(选别的有文字提示，根据自己需求，别乱选，不然windows都没了)
![img](/home/zzhenry/Boostnote/Ubuntu/assets/v9Se8cp.jpg)

------

### 7.4 分区
**第一张是刚进来的样子** 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/tVu6diJ.jpg)

------

**分区详情** 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/ER9bMkQ.jpg) 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/6QjVuD2.jpg) 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/dgtHhgz.jpg)

![img](/home/zzhenry/Boostnote/Ubuntu/assets/TPPHwIt.jpg)

**最终图如下：** 

![img](/home/zzhenry/Boostnote/Ubuntu/assets/1488597-1f035ea711309bf2.jpg)

**注意，要将安装的启动引导器(grub2)设备选择在efi分区上**也就是我们安装windows时设置的分区。

**选择键盘布局（可以用自动探测，大多数都是美式英语键盘）** 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/Wr6UrOW.jpg)

接下来就是安装了，安装完后重启会进入windows，接下来是用easyBCD添加ubuntu引导

## 8. 在windows下添加ubuntu的引导

![img](/home/zzhenry/Boostnote/Ubuntu/assets/wkeNFTt.jpg) 
![img](/home/zzhenry/Boostnote/Ubuntu/assets/LbaIxU5.jpg)

这样子就好了，其他不用改，重启后就可以看到蓝色的metro有两项引导了，点击第二个ubuntu会重启进入ubuntu的grub2 引导，然后进入ubuntu系统，至此双系统双硬盘安装告一段落。

## 9. 可能会碰到的问题

### 9.1 开机黑屏，出现`mmc0 unknown controller version (3)`

1. At the first menu select "try Ubuntu", press "e" to edit and add `nomodeset` after `quiet splash`

2. 进去系统之后编辑`/etc/default/grub`:

   ```sh
   sudo vim /etc/default/grub
   ```

   将`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`修改为`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"` 

   再更新Grub：

   ```sh
   sudo update-grub
   ```

3. 重启

## 10. References

> <https://blog.csdn.net/tuzhenlei/article/details/52098046>
>
> <https://askubuntu.com/questions/999544/uefi-install-mmc0-unknown-controller-version-3-error>