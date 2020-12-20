# Ubuntu 中更改所有子文件和子目录所有者权限

Ubuntu中有两个修改命令可以用到：“change mode“ & “change owner”

即`chmod`以及`chown`，其中可以用递归参数`-R`来实现更改所有子文件和子目录的权限。

## 1. 利用`chmod`修改权限：

对`Document/`目录下的所有子文件与子目录执行相同的权限变更：

```sh
chmod -R 700 Document/
```

`-R`参数是递归处理目录下的所有文件以及子文件夹，`700`是变更后的权限表示（只有所有者有读和写以及执行的权限），`Document/ `是需要执行的目录

## 2. 利用`chown`改变所有者：

对`Document/ `目录下的所有文件与子目录执行相同的所有者变更，修改所有者为`users`用户组的`username`用户

```sh
chown -R username:users Document/
```

`username:users` users用户组的username，用户组参数非必须