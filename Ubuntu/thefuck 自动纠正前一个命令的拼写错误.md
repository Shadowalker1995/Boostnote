# thefuck: 自动纠正前一个命令的拼写错误
[**thefuck**](https://github.com/nvbn/thefuck)是一个使用Python编写的开源小工具，它可以自动纠正前一个命令的拼写错误。这个工具非常酷，尤其对于常常使用命令行的童鞋。
######
thefuck支持Mac OS X和Linux系统。

## Ubuntu安装thefuck
```shell
sudo apt install python3-dev python3-pip
sudo -H pip3 install thefuck
```

创建一个别名，首先编辑bashrc配置文件：
```shell
vim ~/.bashrc
```

在文件尾加入一行：
```shell
eval "$(thefuck --alias fuck)"
```

使生效：
```shell
source ~/.bashrc
```
使用示例：
```shell
sdo vim /etc/passwd
```

![img](http://blog.topspeedsnail.com/wp-content/uploads/2016/05/Screen-Shot-2016-05-15-at-09.42.30.png)
直接回车执行纠正过的命令。
```shell
sudo atp-get install python
```

![img](http://blog.topspeedsnail.com/wp-content/uploads/2016/05/Screen-Shot-2016-05-15-at-09.44.40.png)

![img](http://blog.topspeedsnail.com/wp-content/uploads/2016/05/Screen-Shot-2016-05-15-at-09.47.28.png)

![img](https://raw.githubusercontent.com/nvbn/thefuck/master/example.gif)

更多用法参看项目README。