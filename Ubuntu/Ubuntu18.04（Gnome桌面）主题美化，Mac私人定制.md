# Ubuntu18.04（Gnome桌面）主题美化，Mac私人定制

开始之前，请安装美化管理器`sudo apt install gnome-tweak-tool` ,中文名优化

# 1. Gnome-shell Extensions

### 1.1 何为Gnome-shell Extensions 以及如何安装与应用 ？

Gnome-shell extensions(Gnome-shell 扩展，也可以说成Gnome extensions，以下简称GSE)是每个美化Gnome桌面童鞋的必经之路。它是可以安装在Gnome之上的第三方附件组件和插件，简单的理解，它类似谷歌、火狐等一些浏览器的插件。有了GSE，你可以非常轻便的制定你的Gnome桌面。 
GSE的的安装有三种方式[1]，这里主要介绍web浏览器安装的方式，这也是最常用的方式： 
所需要的web浏览器必须是能够支持附件组件的浏览器，如chrome、firfox、opera等，用此浏览器打开<https://extensions.gnome.org/> (这是一个GSE下载网站，里面有各种各样的插件)。打开后，你可能会看到如下图的提醒： 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180430202521791.png)
所以按照提醒点击链接为当前浏览器安装扩展，之后，你会发现你的浏览器多出了一个插件。完成这步安装后，你可能会还会收到如下图的警告： 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180430202749382.png)
链接中的documentation是告诉你要为系统安装chrome-gnome-shell (虽然有chrome，但与chrome没有关系)，如果你是Ubuntu，请执行`sudo apt install chrome-gnome-shell` 。 
之后，你就可以根据需要找到相应的Gnome-shell扩展，如下图所示，只需要点击类似开关的按钮即可自动安装。 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/2018043020343621.png)
安装之后，你需要在gnome-tweak-tool（优化）工具中的扩展栏进行扩展插件的管理。 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180501125857848.png)

### 1.2 本文安装的Gnome-Shell Extensions

本文的美化安装了如下的扩展： 
**1.User Themes**: 作用是从用户目录加载主题。通俗的说就是，正常的主题包下载后，要放置在`user/share/themes` 下，这是多用户共同使用的主题，而且系统重装后将失去该主题，而User Themes扩展能允许你把主题包放置在自己家目录`.local/share/themes`(themes文件夹是自己新建的)下，并使其生效。

**2.Dash to Dock** : 作用是制定Dock和Dash，Dock就是类似windows系统的任务栏的东东，而Dash就是搜索的东东。你也可以用**Dash to Panel** 这个扩展

**3.Gnome Global Application Menu** ：作用看下图，将一个应用窗口的菜单项放置在了桌面顶部栏中。 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180501125809454.png)

**4.TopIcons Plus** : 起到了任务栏的作用,一些程序的图标会显示出来

# 2.主题、图标与shell

对于Gnome桌面，你最需要连接的就是这个网站<https://www.gnome-look.org/>，它提供了包括主题、图标、字体等在内的很多包。 
因为在上述中安装了`User Themes` 扩展，所以我们可以把下载好的主题放置在自己的家目录下，为此，在家目录下的`.local/share`中新建`themes`、`fonts`、`icons` 三个文件夹，分别存放主题、字体和图标 。

### 2.1主题

![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180501130916901.png)
本文下载如上图所示的主题，下载后，将`Gnome-OSC-HS-(transparent)` 文件复制到`.local/share/themes` 中，然后在Gnome-tweak-tool中进行设置。 
![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180501131211650.png)

### 2.2 shell主题

![这里写图片描述](/home/zzhenry/Boostnote/Ubuntu/assets/20180501131522933.png)
本文下载如上图所示的shell主题，下载后，将`Human-NEXT` 文件复制到`.local/share/themes` 中，然后在Gnome-tweak-tool中进行设置。

### 2.3 图标

你可以在侧栏*Icon Themes* 找到需要的图标，然后下载，放置在`.local/share/icons` 中。而本人并不喜欢Mac的图片，却独爱一款扁平化的图片。安装方式如下：

```sh
sudo add-apt-repository ppa:snwh/pulp
sudo apt-get update  
sudo apt-get install paper-icon-theme123
```

安装之后，依然在Gnome-tweak-tool中进行设置

---

# Reference

\[1\][桌面应用|如何使用Gnome Shell 扩展](https://linux.cn/article-9447-1.html) 
[2] <https://linuxhint.com/gnome-tweak-tool-ubuntu-17-10/>
[3]<https://blog.csdn.net/zyqblog/article/details/80152016>