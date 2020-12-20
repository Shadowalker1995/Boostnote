## Ubuntu 18.04 同时安装 Anaconda2 与 Anaconda3

## 1. 安装 Anaconda3

Anaconda installer archive：<https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/>

```sh
cd ~/Softwares/installed/Anaconda/
./Anaconda3-5.1.0-Linux-x86_64.sh
```

## 2. 创建并安装 Anaconda2 环境

不需要create新环境，直接运行以下代码，其中py2是新的环境名：

```sh
bash Anaconda2-5.1.0-Linux-x86_64.sh -b -p ~/anaconda3/envs/py2
rm -f ~/anaconda3/envs/py2/bin/conda*
rm -f ~/anaconda3/envs/py2/conda-meta/conda-*
rm -f ~/anaconda3/envs/py2/bin/activate
rm -f ~/anaconda3/envs/py2/bin/deactivate
cd ~/anaconda3/envs/py2/bin
ln -s ../../../bin/conda .
ln -s ../../../bin/activate .
ln -s ../../../bin/deactivate .
```

现在让来检查一下我们安装的环境，打开一个新终端，输入下面命令来查看它：

```sh
conda info --envs
```

如果提示错误，则说明没有配置好，需要进行下面的步骤：

```sh
sudo gedit ~/.bashrc
```

打开文件后在末尾输入

```sh
export PATH="/home/zzhenry/anaconda3/bin:$PATH"
```

此处anaconda2的路径根据你自己的做相应的修改即可。

输入后打开一个新终端，输入`python`

会看到anaconda，如下图所示



至此，anaconda即安装成功。以后如果需要安装python的包的话直接conda install 包名就可以了，像下面这样：

```sh
conda install numpy
```

可以通过以下命令来激活anaconda2的环境：

```sh
source activate py2
```

取消激活：

```sh
source deactivate py2
```

## 3. 更新/替换 python 版本

anaconda的命令既可以更新python3至该版本最新同时也可以指定版本，anaconda将自动更新所有的依赖包：

```sh
conda update python
conda install python=3.6
```

如果遇到CondaHTTPError的联网问题，执行以下命令即可：

```sh
anaconda logout
```

如果需要删除anaconda的话，直接删掉anaconda的文件夹就行

## 4. Conda/pip 换源 

### 4.1 更换conda源

设置Anaconda镜像源以减少等待时间。同样，我的镜像源是[科大镜像](https://blossomnoodles.github.io/cnBlogs/2018/04/30/mirror.ustc.edu.cn)。

```sh
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

###4.2 更换pip源

pip国内的一些镜像：

1. 阿里云 <http://mirrors.aliyun.com/pypi/simple/> 
2. 中国科技大学 <https://pypi.mirrors.ustc.edu.cn/simple/> 
3. 豆瓣(douban) <http://pypi.douban.com/simple/> 
4. 清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple/> 
5. 中国科学技术大学 <https://pypi.mirrors.ustc.edu.cn/simple/>

#### 临时使用：

可以在使用`pip`的时候在后面加上`-i`参数，指定pip源

```sh
 pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 永久修改：

**linux:** 
修改` ~/.pip/pip.conf` (没有就创建一个)， 内容如下：

```sh
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

**windows:** 
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

```sh
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
## 5. 查看、安装、更新库

1. 查看已安装的库

   ```sh
   pip list
   # 或者
   conda list
   ```

   其中，`pip list` 只能查看库，而 `conda list` 则可以查看库以及库的版本

2. 安装或更新库

   以安装/更新 scipy 为例

   ```sh
   pip install scipy
   pip install scipy --upgrade
   # 或者
   conda install scipy
   conda update scipy
   
   # 更新所有库
   conda update --all
   
   # 更新 conda 自身
   conda update conda
   
   # 更新 anaconda 自身
   conda update anaconda
   ```

   

## 6. 管理自带的python2.7

系统自带的 python2.7 执行路径为 `/usr/bin/python2.7`，故将 `/usr` 路径软链接到 `/home/zzhenry/anaconda3/envs/` 目录中：

```sh
sudo ln -s /usr /home/zzhenry/anaconda3/envs/py27
```

使用命令 `source activate py27` 激活之。