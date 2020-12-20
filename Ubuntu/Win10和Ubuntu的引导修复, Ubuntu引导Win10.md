# Win 10 和 Ubuntu 的引导修复, Ubuntu 引导 Win 10

## 1. Win10 启动失败, bootmgr is missing(启动项管理器文件丢失)

### 1.1 错误原因:

- 重要系统文件丢失。
- 文件被病毒或恶意软件损坏或摧毁。
- 不适当的BIOS模拟等导致不能访问桌面环境。
- 不正确的重装系统或者是C盘系统奔溃。
- 系统盘符默认启动优先顺序错误。

### 1.2 解决方法:

- 如果Win10系统所在磁盘的盘符不是C,则修改成C
- PE系统盘修复bootmgr
  1. 插入PE系统盘也可以是U盘启动盘
  2. 选择分区工具
  3. 选中系统所在分区,标记此分区为活动分区,其他分区为逻辑分区
  4. 选中系统所在分区,点击硬盘选项,重建MBR

![重建MBR](https://img-blog.csdn.net/20171129152310757?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGhhb2ppYW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 2. Ubuntu引导修复

由于在修复win10引导时损坏了Ubuntu的引导,导致电脑开机指显示一个J

```
# 进入root用户
sudo -i 
# 添加软件源并更新
add-apt-repository ppa:yannubuntu/boot-repair &&　apt-get update
# 安装boot-repair并启动软件
apt-get install -y boot-repair && boot-repair
```

**在弹出界面中选择Recommend repair。** 
![选择Recommend repair](https://img-blog.csdn.net/20171129144830896?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGhhb2ppYW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

执行中

![执行中](https://img-blog.csdn.net/20171129145121172?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGhhb2ppYW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

修复成功！

![修复成功](https://img-blog.csdn.net/20171129145229956?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGhhb2ppYW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3. Ubuntu 引导 Win 10

重启电脑，在选择系统时，按下”C”键，进入grub

![输入C，进入grub](https://img-blog.csdn.net/20171129151557251?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGhhb2ppYW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 3.1 查看 Win 10 所在磁盘的信息

> 系统的第一个硬盘驱动器表示成(hd0)，其上的第一个分区表示为(hd0,0)，也就是说对于硬盘,采用(hdx,y)的形式来表示，x表示硬盘号，y表示分区号。主分区只能有四个。
>
> 在Windows系统中逻辑分区则从(hd0,4)开始算,第一硬盘的四个主分区分别用(hd0,0)~(hd0,3)来表示,第一逻辑分区用(hd0,4)，第二逻辑分区用(hd0,5)来表示。 
> 在Linux系统中，如ubuntu，(hdx,y)中的y是从1开始计数的。第一硬盘的四个主分区分别用(hd0,1)~(hd0,4)来表示,第一逻辑分区用(hd0,5)，第二逻辑分区用(hd0,6)来表示

```sh
# 查看所有硬盘
grub>ls 
(hd0) (hd0,msdos4) (hd0,msdos3) (hd0,msdos2) (hd0,msdos1) (hd1)...
# 查看单个磁盘,可以根据你的磁盘大小来判断哪个是Win10盘
grub>ls (hd1,msdos2) 
分区 hd1,msdos2 : 文件系统ntfs - Label 'XXXX',UUID 2A74AC5774AC2791 - Partition start  at 1024KiB - Total size XXXXXkiB
```

找到Win10所在盘的信息记录下（hd1,msdos2） UUID 2A74AC5774AC2791 
**继续输入以下代码(未试过)或者进入3.2(试过可用)**

```sh
grub>title Win10
grub>rootnoverify (hd1,msdos2)
grub>makeactive
grub>chainloader +11234
```

### 3.2 进入 Ubuntu，添加引导

root用户下修改grub.cfg文件

```sh
sudo -i
vim /boot/grub/grub.cfgsh
```

在文件末尾添加:

```
menuentry 'Win10' {
    insmod ntfs
    set root='hd1,msdos2'
    search –-no-floppy –-fs-uuid –-set 2A74AC5774AC2791
    # 将指定的文件作为一个链式装载程序载入。为了获取在一个指定分区第一扇区内的文件，使用+1作为文件名。(指示GRUB读入分区的第一个扇区的引导记录)
    chainloader +1
}
```

更新引导

```sh
grub-mkconfig -o /boot/grub/grub.cfg1
```

重启电脑即可看见Win10的启动项