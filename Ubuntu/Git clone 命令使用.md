# Git clone 命令使用

## Git clone 命令参数：

```sh

```

参数挺多，但常用的就几个：

1. 最简单直接的命令

```sh
git clone xxx.git
```

2. 如果想clone到指定目录

```sh
git clone xxx.git "指定目录"
```

3. clone时创建新的分支替代默认Origin HEAD（master）

```sh
git clone -b [new_branch_name]  xxx.git
```

4. clone 远程分支

　　git clone 命令默认的只会建立master分支，如果你想clone指定的某一远程分支(如：dev)的话，可以如下：

　　A. 查看所有分支(包括隐藏的)  git branch -a 显示所有分支，如：　　　　

```sh
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
```

　　B.  在本地新建同名的("dev")分支，并切换到该分支

```sh
git checkout -t origin/dev 该命令等同于：
git checkout -b dev origin/dev
```

