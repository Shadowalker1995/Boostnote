# Ubuntu 搭建php开发环境

前段时间在阿里云上花了99(学生特惠 = =)买了一个一年的ECS，系统选的是Ubuntu 16.04，记录下搭建LAMP Web环境的过程

## Apache安装

```sh
sudo apt-get install apache2
```

安装好后打开浏览器，输入localhost查看是否安装成功

![img](/home/zzhenry/Boostnote/Ubuntu/assets/940343-20171214224820732-1215136517-1526988345553.png)

## PHP 安装

```sh
sudo apt-get install php7.0
```

安装完成后输入：`php -v` 查看PHP是否安装成功

![img](/home/zzhenry/Boostnote/Ubuntu/assets/940343-20171214225632170-870726331.png)

PHP和Apache都安装好后就需要让Apache能够识别解析PHP文件，我们先搜一下有没有适合PHP7的插件，输入命令：

```sh
apt-cache search libapache2-mod-php
```

可以看到搜出来的结果里面有一个是PHP7.0版本的，我们就安装这个：

```sh
sudo apt-get install libapache2-mod-php7.0
```

下面我们就可以随便写一个php文件看是否可以解析访问。输入命令: `cd /var/www/html` 切换到apache项目目录下，新建文件：`sudo vim test.php`

```php
<?php
    phpinfo();
?>
```



![img](/home/zzhenry/Boostnote/Ubuntu/assets/940343-20171214231125013-1040218057.png)

保存后浏览器访问：localhost/test.php

![img](/home/zzhenry/Boostnote/Ubuntu/assets/940343-20171214231252107-1043090460.png)

如果一切正常的话，就会看到php的一些信息。

## Mysql 安装

接下来就是安装数据库Mysql了,数据库需要装服务端和客户端两个，输入命令：

```sh
sudo apt-get install mysql-server mysql-client
```

安装过程中会提示设置root账号的登录密码，输入后选择OK继续安装

![img](/home/zzhenry/Boostnote/Ubuntu/assets/940343-20171214232507467-394077377.png)

安装完成后，输入`mysql -V `查看安装的版本信息

同样的，我们还需要让mysql能够和php互动，安装php的mysql插件：

```sh
sudo apt-get install php7.0-mysql
```

最后我们还可以安装一些常用的php扩展

```sh
sudo apt-get install php7.0-gd php7.0-mbstring php7.0-xml
```

到此关于lamp的软件就安装完成了，最后还可以安装一下composer：

```sh
sudo apt-get install composer
```

安装好后输入命令：`composer` 查看是否成功

![img](/home/zzhenry/Boostnote/Ubuntu/assets/940343-20171215142212433-206514006.png)

## 安装 curl

```sh
sudo apt-get install curl libcurl3 libcurl3-dev php7.0-curl
```

恭喜，PHP cURL安装完毕。记得重启Apache服务器

```sh
sudo /etc/init.d/apache2 restart
```

如果仍然有问题，尝试编辑你的`php.ini`文件（我的是`/etc/php5/apache2/php.ini`),在最后加上一行：

```sh
extension=curl.so
```

保存文件后重启Apache服务器。