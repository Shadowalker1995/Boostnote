# Ubuntu 22.04国内镜像阿里云/163源/清华大学/中科大 & PPA

Ubuntu 22.04 LTS这是一个长期支持版本，它将被支持五年，直到2027年4月。已发布的LTS版本带来了一些新的功能。

如果你正在使用Ubuntu 20.04 LTS，你会注意到许多视觉上的变化。

当然作为国内用户首要任务安装完成之后首要任务就是更改ubuntu 22.04的镜像/软件源。

国内有很多Ubuntu 22.04的镜像源，包括阿里、网易，还有很多教育网的镜像源，比如清华源、中科大源。

在教程中我们将介绍如何更改镜像在ubuntu 22.04。国内的包括有镜像阿里云/163源/清华大学/中科大。

首先我们需要先备份Ubuntu官方的软件源，执行以下命令将备份原来的软件源。

编辑`/etc/apt/sources.list`文件, 在文件最前面添加以下条目(操作前请做好相应备份)：

```bash
sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak
```

## 20.04 focal

### 清华大学镜像

清华大学开源软件镜像站，致力于为国内和校内用户提供高质量的开源软件镜像、Linux镜像源服务。

帮助用户更方便地获取开源软件。镜像站由清华大学TUNA协会负责运行维护。

复制以下命令即可一键切换到清华大学ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```

### 163镜像

复制以下命令即可一键切换到163 ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
deb http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
# 预发布软件源，不建议启用
# deb http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse
```

### 阿里云镜像

阿里巴巴开源镜像站，免费提供Linux镜像下载服务，拥有Ubuntu、CentOS、Deepin、MongoDB、Apache、Maven、Composer等多种开源软件镜像源。

此外还提供域名解析DNS、网络授时NTP等服务，致力于为互联网用户提供全面，高效和稳定的基础服务。

复制以下命令即可一键切换到阿里云 ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
```

### 中科大镜像

中国科学技术大学开源软件镜像由中国科学技术大学网络信息中心提供支持。

mirrors.ustc.edu.cn是Debian, Ubuntu, Fedora, Archlinux, CentOS等多个发行版的官方源。目前是中国大陆高校访问量最大，收录最全的开源软件镜像。

中国科学技术大学Linux用户协会是由中国科学技术大学在校的GNU/Linux爱好者发起并组成的一个全校性群众团体。

成立协会的目的在于联合科大的GNU/Linux使用者，搭建信息交流共享的平台，宣传自由软件的价值，提高自由软件社区文化氛围，推广自由软件在科大校园乃至合肥地区的应用。

复制以下命令即可一键切换到中科大ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
# 默认注释了源码仓库，如有需要可自行取消注释
deb https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
EOF"
```

## 22.04 Jammy

### 清华大学镜像


```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
EOF"
```

### 163镜像

复制以下命令即可一键切换到163 ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
deb http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
EOF"
```

### 阿里云镜像

阿里巴巴开源镜像站，免费提供Linux镜像下载服务，拥有Ubuntu、CentOS、Deepin、MongoDB、Apache、Maven、Composer等多种开源软件镜像源。

此外还提供域名解析DNS、网络授时NTP等服务，致力于为互联网用户提供全面，高效和稳定的基础服务。

复制以下命令即可一键切换到阿里云 ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
deb http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
EOF"
```

### 中科大镜像

中国科学技术大学开源软件镜像由中国科学技术大学网络信息中心提供支持。

mirrors.ustc.edu.cn是Debian, Ubuntu, Fedora, Archlinux, CentOS等多个发行版的官方源。目前是中国大陆高校访问量最大，收录最全的开源软件镜像。

中国科学技术大学Linux用户协会是由中国科学技术大学在校的GNU/Linux爱好者发起并组成的一个全校性群众团体。

成立协会的目的在于联合科大的GNU/Linux使用者，搭建信息交流共享的平台，宣传自由软件的价值，提高自由软件社区文化氛围，推广自由软件在科大校园乃至合肥地区的应用。

复制以下命令即可一键切换到中科大ubuntu 22.04镜像：

```bash
sudo bash -c "cat << EOF > /etc/apt/sources.list && apt update 
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
EOF"
```

## 解决apt-get install E: 无法定位软件包问题

```sh
deb http://archive.ubuntu.com/ubuntu/ trusty main universe restricted multiverse
```

然后执行命令：

```sh
sudo apt-get update
sudo apt-get upgrade
```

### PPA

PPA，表示 Personal Package Archives，也就是个人软件包集。有很多软件因为种种原因，不能进入官方的 Ubuntu 软件仓库。为了方便 Ubuntu 用户使用，launchpad.net 提供了 ppa，允许用户建立自己的软件仓库， 自由的上传软件。PPA 也被用来对一些打算进入 Ubuntu 官方仓库的软件，或者某些软件的新版本进行测试。

添加ppa的源：

```sh
sudo add-apt-repository ppa:ubuntu-wine/ppa
sudo apt-get update
sudo apt-get upgrade
```

有时一些旧的源会失效，因此可以使用以下的命令查出就的源，然后对其进行删除。

```sh
sudo apt-get update | grep "Failed"	# 先对源进行更新，然后在流中查出Failed的内容
sudo add-apt-repository --remove ppa:finalterm/daily
```
