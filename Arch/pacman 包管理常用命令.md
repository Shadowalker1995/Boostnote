# pacman 包管理常用命令

## `-S` 指令

**安装**

```bash
sudo pacman -S 		#安装软件
sudo pacman -Sy		#获取最新打软件情况，如果已经是最新了，直接会提示已经更新到最新了。
sudo pacman -Syy 	#强行更新你的应用的软件库(源)
sudo pacman -Su 	#更新所有软件
sudo pacman -Syu 	#更新软件源并更新你的软件
sudo pacman -Syyu 	#强行更新一遍，再更新软件
```

**查询一个软件**

```bash
sudo pacman -Ss <pkg_name>	#查询所有软件名里面带有<pkg_name>相关的软件。并且查询名支持正则表达
```

**删除软件/var目录下的缓存**

```bash
sudo pacman -Sc 
```

## `-R` 指令

```bash
sudo pacman -R <pkg_name> #删除软件
sudo pacman -Rs <pkg_name> #删除软件，并删除<pkg>所有的依赖包
sudo pacman -Rns <pkg_name> #删除软件，并删除<pkg>所有的依赖，并删掉<pkg>的全局配置文件。 推荐！！ 
```

## `-Q` 指令

```bash
sudo pacman -Q 		#显示出所有软件 sudo pacman -Q | wc -l 查询数量
sudo pacman -Qe 	#查询所有自己安装的软件
sudo pacman -Qeq 	#查询所有自己安装的软件，只显示包名，不显示版本号等
sudo pacman -Qs <pkg_name>	#查询本地安装的所有带<pkg_name>的软件
sudo pacman -Qdt 	#查询所有孤儿软件，不再被需要的。
sudo pacman -Qdtq 	#查询所有不再被依赖的包名
```

**查询孤儿软件并删除掉他们**

```bash
sudo pacman -R $(sudo pacman -Qdtq)
```

