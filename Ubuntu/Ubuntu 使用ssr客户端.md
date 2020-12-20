# Ubuntu 使用ssr客户端

```sh
wget https://github.com/the0demiurge/CharlesScripts/raw/master/charles/bin/ssr
sudo mv ssr /usr/local/bin

ssr install
ssr config
```

修改其中的ssr install()，在sleep 1之前加入

```sh
gsettings set org.gnome.system.proxy.http host '127.0.0.1'
gsettings set org.gnome.system.proxy.http port 1080
gsettings set org.gnome.system.proxy mode 'manual'
```

在ssr stop()里，在`sudo python local.py -d stop`之前加入

```sh
gsettings set org.gnome.system.proxy mode 'auto'
```

修改完成，更改权限并且移动

```sh
sudo chmod 777 /usr/local/bin/ssr
```

在终端运行：

```sh
ssr install
ssr config #填入你的ssr设置，也可以yong自带的 ssr update
ssr start
```

## 设置开机自启动

```sh
sudo vim /etc/rc.local
```

里面直接添加要运行的命令

```sh
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

sudo ssr start
exit 0
```



然后就会发现并不能翻墙，这时候先检查一下防火墙或者安全组。 然后就会遇到下一个问题了：

**Shadowsocks**是一个使用SOCKS5（或者SOCK4之类）协议的代理，它只接受 SOCKS5 协议的流量，不接受 HTTP 或者 HTTPS 的流量。所以当你在 Chrome 上能穿墙的时候，是 Proxy SwitchyOmega 插件把 HTTP 和 HTTPS 流量转换成了 SOCKS 协议的流量，才实现了 Shadowsocks 的代理。而终端是没有这样的协议转换的，所以没法直接使用 Shadowsocks 进行代理。这时候就需要一个协议转换器，这里我用了 **Privoxy**。

所以就要开始配置 **Privoxy** 了： 
那么 Privoxy 到底是什么呢？维基百科上是这么说的。

> Privoxy 是一款带过滤功能的代理服务器，针对 HTTP、HTTPS 协议。通过 Privoxy 的过滤功能，用户可以保护隐私、对网页内容进行过滤、管理 cookies，以及拦阻各种广告等。Privoxy 可以用作单机，也可以应用到多用户的网络。 
>
> 修改 HTTP 请求头的字段，如referrer和user agent，从而隐藏用户上一个查看的网页和用户正在使用的浏览器。

## 安装Privoxy

```sh
sudo apt-get install privoxy
```

安装好后进行配置，Privoxy 的配置文件在 ``/etc/privoxy/config`，这个配置文件中注释很多。

找到 **4.1. listen-address** 这一节，确认监听的端口号。 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20171228115516947.jpg)
找到 **5.2. forward-socks4, forward-socks4a, forward-socks5 and forward-socks5t** 这一节，加上如下配置，注意最后的点号。 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20171228115544356.jpg)

有关Privoxy的配置就结束了，重启一下Privoxy：

```sh
sudo /etc/init.d/privoxy restart
```

接着配置一下终端的环境：

```sh
export http_proxy=”127.0.0.1:8118”
export https_proxy=”127.0.0.1:8118”
```

然后就可以测试一下穿墙效果了。

```sh
wget http://www.google.com
```