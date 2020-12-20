# Ubuntu 系统备份还原

## 系统备份

```sh
sudo su
cd /
tar -cvpzf /home/zzhenry/Documents/BACKUP_SYSTEM/backup.tgz --exclude=/proc --exclude=/lost+found --exclude=/mnt --exclude=/media --exclude=/sys --exclude=/home /
```

- `tar`是用来备份的程序
- `c` - 新建一个备份文档
- `v` - 详细模式，tar 程序将在屏幕上实时输入所有信息
- `p` - 保存许可，并且应用到文件
- `z` - 采用 ‘gzip’ 压缩备份文件，以减小备份文件体积
- `f` - 指明备份文件存放的路径
- `--exclude` - 排除制定的目录。使其不被备份

有人可能会建议你把`/dev`目录排除在外，但是我认为这样做很不妥，具体原因这里就不讨论了。

在备份命令结束时你可能会看到这样一个提示：`tar: Error exit delayed from previous errors`，多数情况下你可以忽略它。

你还可以用 Bzip2 来压缩文件，Bzip2 比 gzip 的压缩率高，但是速度慢一些。如果压缩率对你来说很重要，那么你应该使用 Bzip2，用`j`代替命令中的`z`，并且给档案文件一个正确的扩展名 bz2。完整的命令如下：

```sh
tar -cvpjf /home/zzhenry/Documents/BACKUP_SYSTEM/backup.tar.bz2 --exclude=/proc --exclude=/lost+found --exclude=/mnt --exclude=/media --exclude=/sys --exclude=/home /
```

## 恢复系统

在 Linux 中有一件很美妙的事情，就是你可以在一个运行的系统中恢复系统，而不需要用 boot-cd 来专门引导。当然，如果你的系统已经挂掉不能启动了， 你可以用Live CD来启动，效果是一样的。

使用下面的命令来恢复系统：

```sh
sudo su
tar -xvpzf /home/zzhenry/Documents/BACKUP_SYSTEM/backup.tgz -C /
```

如果你的档案文件是使用 Bzip2 压缩的，应该用：

```sh
sudo su
tar -xvpjf /home/zzhenry/Documents/BACKUP_SYSTEM/backup.tar.bz2 -C /
```

- `C` - 指定 tar 程序解压缩到的目录，在这里是 /

重新创建剔除的目录：

```sh
cd /
mkdir /proc /lost+found /mnt /media /sys
```



**注意：上面的命令会用档案文件中的文件覆盖分区上的所有文件。**

执行恢复命令之前请再确认一下你所键入的命令是不是你想要的，执行恢复命令可能需要一段不短的时间。

当你重启电脑，你会发现一切东西恢复到你创建备份时的样子了！