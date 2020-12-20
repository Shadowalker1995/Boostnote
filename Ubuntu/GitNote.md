# GitNote

## 0. 前言

> 在使用 Git 时有一种感觉就是只会 `add | commit | push` 三个命令。因为这三个命令似乎足以把代码提交到 GitHub 上，即使是碰到某个问题，也可以直接 Google。但是对于其中的逻辑和版本管理的精髓没有体会到，而只是作为一个在线代码仓库在使用。
>
> 官方的 Git 入门教程 [Git 官方教程（中字）](https://www.nowcoder.com/courses/2#chapter-14) 里面通过描述对命令的使用情景进而选择命令进行操作的方式，使得命令很容易理解也容易加深记忆。比起单一的命令用文字解释这种方式，对于不熟悉 Git 的人来说是十分友好的。但是，看完容易忘，所以写了这篇整理笔记用作辅助查询。

## 1. 基本命令

### 1.1 了解帮助命令

- `git help` : 查看命令
- `git help add` : 查看 `git add` 命令的具体解释

### 1.2 仓库初始化

- `git init` : 创建 `.git`, 适合在已存在项目追加版本控制
- `git init projectname` : 创建 `projectname/.git`, 适合项目开始时加入版本控制

### 1.3 文件基本操作

- `git add filename/*` : 添加文件[产生暂存文件]
- `git commmit -m "message"` : 将添加的文件提交到本地仓库[产生提交文件]
- `git rm filename` : 移除文件，使用 `rm filename` 的有暂存
- `git add -u .` : 如果之前使用非 git 命令删除文件，可以使用这个命令把当前目录的文件重新遍历清除
- `git rm --cache filename` : 暂存但是不参与跟踪
- `git mv filepath newfilepath` : 移动文件
- `git rm filepath && git add newfilepath` : 移动文件，之前使用非 git 命令移动文件
- `git add -A .` : 如果之前使用非 git 命令移动文件，可以使用这个命令把当前目录的文件重新遍历移动，和 `rm` 命令类似
- `git reset etc...` : 历史提交管理(回退，合并…)，checkout 更关注文件

### 1.4 查看文件修改

- `git status` : 查看文件信息
- `git diff` : 查看修改[工作树和暂存文件]
- `git diff --staged` : 查看修改[暂存文件和最近提交文件]
- `git diff HEAD` : 查看修改[工作树和最近提交文件]
- `git diff --word-diff` : 查看修改的单词用颜色标出
- `git diff --stat` : 查看修改的文件名

> 参考资料 [0. Git 学习（三）本地仓库操作——git add & commit](http://www.cnblogs.com/feeland/p/4500721.html)了解 git 版本库实现

### 1.5 查看提交 Log

- `git log` : 显示提交信息
- `git log --oneline` : 显示提交 Message
- `git log --stat` : 显示提交文件名级详细修改信息
- `git log --patch` : 显示提交文件内容级详细修改信息
- `git log --graph` : 用图显示提交记录
- `git log --graph --all --decorate --oneline` : 去除冗余信息，更加直观显示每条分支每次提交
- `git log --stat -- filename` : 文件提交记录（不记录路径移动）
- `git log --stat -M --follow -- filename` : 看到完整的文件操作过程

### 1.6 忽略文件

- `touch .gitignore` : 创建文件(次级目录也可以创建)
- `vim .gitignore` : 编辑文件添加 ignore 文件。`*.log | tmp/ | .sass-cache etc...`
- `git ls-files --others --ignored --exclude-standard` : 查看被 ignore 的文件
- `git reflog` : 详细修改日志

### 1.7 分支操作

- `git branch branchname` : 创建分支
- `git branch` : 显示分支
- `git branch -d branchname` : 删除分支
- `git branch -D branchname` : 删除未合并分支
- `git checkout branchname` : 切换分支
- `git checkout commitID` : 工作树切换到 commitID 时
- `git checkout -- filename` : 清理掉最后一次提交内容
- `git checkout -b branchname` : 创建新分支并且进入该分支
- `git merge branchname` : 合并 branchname 分支到目前所在分支(合并时文件冲突要手动解决)
- `git merge --abort` : 清除工作目录和暂存区
- `git merge squash branchname` : 将合并的分支改变变成一个 commit
- `git rebase branchname` : 将当前分支历史提交合并到 branchname 分支

> 参考资料 [2. 代码合并：Merge、Rebase 的选择](https://github.com/geeeeeeeeek/git-recipes/wiki/5.1-%E4%BB%A3%E7%A0%81%E5%90%88%E5%B9%B6%EF%BC%9AMerge%E3%80%81Rebase-%E7%9A%84%E9%80%89%E6%8B%A9)

### 1.8 远程操作

- `git remote add origin https://github.com/accountname/projectname`
- `git remote set-url origin newUrl` : 改变 URL
- `git remote rm origin` : 删除
- `git remote -v` : 查看 URL
- `git fetch origin` : 抓取远程分支，本地会有一个 `remotehostname/branchname` 的分支，一般用于查看伙伴代码
- `git pull origin` : 和 fetch 类似，但是是取回远程更新和本地合并。相当于先 fetch 再 merge。
- `git push origin` : push 到远程仓库

> 参考资料 [1. Git远程操作详解](http://www.ruanyifeng.com/blog/2014/06/git_remote.html)

## 2. 参考资料

- [1. GitHub&Git入门基础](https://www.nowcoder.com/courses/2#chapter-14)
- [0. Git 学习（三）本地仓库操作——git add & commit](http://www.cnblogs.com/feeland/p/4500721.html)
- [1. Git远程操作详解](http://www.ruanyifeng.com/blog/2014/06/git_remote.html)
- [2. 代码合并：Merge、Rebase 的选择](https://github.com/geeeeeeeeek/git-recipes/wiki/5.1-%E4%BB%A3%E7%A0%81%E5%90%88%E5%B9%B6%EF%BC%9AMerge%E3%80%81Rebase-%E7%9A%84%E9%80%89%E6%8B%A9)
- [3. GitHub 高质量的Git中文教程](https://github.com/geeeeeeeeek/git-recipes)