# Ubuntu 16.04 安装 Node.js

Node.js 是基于Javascript语言，应用在服务器端，允许用户快速创建网络应用。在前端和后端都是用Javascript，保持了设计的一致性。

## 安装发行稳定版

Ubuntu默认仓库里带有Node.js，版本较旧，这并不是最新版，但是应该很稳定。执行如下命令：

```sh
sudo apt-get update
sudo apt-get install nodejs
```

在大多数情况下，我们还需要安装npm包管理工具：

```sh
sudo apt-get install npm
```

下面，我们介绍一下更灵活的安装方法。

## 用PPA安装

用PPA你可以得到更新版本的node.js

执行如下命令安装PPA

```sh
curl -sL https://deb.nodesource.com/setup | sudo bash -
```

安装node.js：

```sh
sudo apt-get install nodejs
```

nodejs 包含有nodejs和npm，所以没必要单独安装npm。但是为了使一些npm包正常工作（例如需要从源码构建的包），你需要安装 build-essentials 包：

```sh
sudo apt-get install build-essential
```

## 使用NVM安装

nvm是node.js版本管理器。要安装nvm之前：

```sh
sudo apt-get update
sudo apt-get install build-essential libssl-dev
```

下载nvm安装脚本并执行：

```sh
curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh | sh
```

更行环境变量

```sh
source ~/.profile
```

nvm安装完成，现在安装node.js

列出可用的node.js版本

```sh
nvm ls-remote
```

![1526621683534](/home/zzhenry/Boostnote/Ubuntu/assets/1526621683534.png)

最新版本为v10.1.0：

```sh
nvm install 5.1.0
```

你可以安装多个版本，然后指定使用的版本:

```sh
nvm use 0.12.7
```

当你安装完node.js它的可执行文件为node：

```sh
node -v
```

