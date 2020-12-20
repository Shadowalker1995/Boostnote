# Ubuntu 开机自动挂载磁盘

获取分区类型

```sh
sudo blkid
```

![2018-06-10 15-48-21 的屏幕截图](/home/zzhenry/Pictures/2018-06-10 15-48-21 的屏幕截图.png)

编辑`/etc/fstab`文件:

```sh
sudo gedit /etc/fstab
```

在末行加上:

```sh
UUID=E6C26CCFC26CA591	/media/zzhenry/E6C26CCFC26CA591	ntfs	default	0	0
```

