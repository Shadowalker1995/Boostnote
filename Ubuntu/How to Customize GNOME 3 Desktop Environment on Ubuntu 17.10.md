# How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10

Ubuntu 17.10 Artful Aardvark comes with GNOME 3 Desktop pre-installed. GNOME 3 is a customizable desktop environment. You can tweak it to fit your everyday need. The icons, theme, cursor theme and many other things can be changed.

In this article, I will show you how to customize the GNOME 3 Desktop Environment on Ubuntu 17.10 Artful Aardvark. Let’s get started.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/gnom.png)



------

### **Installing Required Tools:**

In this article, I will use GNOME Tweak Tool to customize the GNOME 3 Desktop Environment on Ubuntu 17.10 Artful Aardvark. If you don’t have it installed already, you can install GNOME Tweak Tool using the following command:

```shell
sudo apt-get update
sudo apt-get install gnome-tweak-tool
```

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/g1.png)

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/g2.png)

Once it’s installed, you can start GNOME Tweak Tool from GNOME 3 Application Menu. Just click on Show Applications icon ![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/icon-1.png) on the bottom left.

Now search for “tweak” and click on the Tweaks icon as shown below.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/search.png)

GNOME Tweak Tool should start.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/tweak-tool.png)

------

### **Change the Position of the Titlebar Buttons:**

On Ubuntu 17.10, the default placement of the Titlebar buttons has changed. On earlier versions of Ubuntu, the buttons were on the left side of the Titlebar. In Ubuntu 17.10, the buttons are in the right side of the Titlebar.

If you prefer the Titlebar buttons to be on the left of the Titlebar as in Ubuntu 16.04, open GNOME Tweak Tool and go to Windows.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/tw-2.png)

Then on the bottom right, on “Titlebar Buttons” section, flip the Placement Switch to Left. By default, it’s Right.

Before:

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/t.png)

After:

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/ta.png)

All the Titlebar buttons should show up on the left side of the Titlebar from now on.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/tweaks.png)

------

### **Show and Hide Icons from Desktop:**

You can show and hide icons from your Ubuntu 17.10 GNOME 3 desktop. You can also display specific icons like Home, Network, Trash, Mounted Volumes.

By default, some icons are shown in the desktop. If you don’t like icons on the desktop, open GNOME Tweak Tool and go to Desktop.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/desktop.png)

On the “Icons on Desktop” section, flip the “Show Icons” switch to “OFF”. It’s on by default.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/desktop-1.png)

You can see that; all the icons are gone from the desktop.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/desktop-2.png)

------

### **Changing Cursor Theme:**

You can change the default cursor of Ubuntu 17.10 Desktop. Open GNOME Tweak Tool and go to “Appearances”.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/appear.png)

On the “Themes” section, click on the “Cursor” selector. A list of cursors that are installed on Ubuntu 17.10 should pop-up. Select any of them, and your cursor should change.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/theme.png)

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/app.png)

------

### **Installing new Cursor Theme:**

You can also install a new Cursor Theme. Go to <https://www.gnome-look.org/p/1148692> and download the Mac OS X cursor theme. This is the one I will use for the demonstration but you may use a different one.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/c1-2.png)

Once the download is complete, go to the HOME directory, and from the Nautilus menu, click on “Show Hidden Files”. You should be able to see all the hidden files now.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/c2-2.png)

Create a new directory, ‘.icons’ in the HOME directory.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/icon-2.png)

Now open the downloaded archive by double clicking it.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/icon-3.png)

Right click on the directory inside the compressed file as shown in the screenshot and click on “Extract”.

![img](https://linuxhint.com/wp-content/uploads/2017/11/cap.png)

Now select the “.icons” folder you just created in the HOME directory and click on the green “Extract” button.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/extract-1.png)

Now close GNOME Tweak Tool if it’s opened and open it again. Go to “Appearances” and select the new cursor theme from there.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/app2.png)

You can see that the cursor has changed.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/app-3-1.png)]

------

### **Changing GNOME 3 Desktop Theme:**

First, we have to enable “User Theme” GNOME Shell Extension to use custom GNOME Shell Themes. To do that, install the following package from the command line:

```shell
$ sudo apt-get install gnome-shell-extensions
```

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/1.png)

Once the installation is complete, restart your computer.

Once your computer starts, open GNOME Tweak Tool and go to “Extensions”.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/2.png)

From here scroll down a little bit till you find “User themes” and enable “User themes” by flipping the switch as shown below.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/3-1545880720454.png)

Once you enable “User themes”, close GNOME Tweak Tool and open it again. Go to “Appearances” tab and you should see the following window:

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/4.png)

Did you notice any change? Take a look, the Shell in “Themes” section is enabled now.

Now find a theme of your choice.

 I will install Pop GTK Icon theme in this article.

To install Pop GTK icon theme, run the following commands:

```shell
$ sudo add-apt-repository ppa:system76/pop
```

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/5.png)

```shell
$ sudo apt-get update
$ sudo apt-get install pop-theme
```

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/6.png)

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/7.png)

Once the installation is complete, open your GNOME Tweak Tool and change the “Applications”, “Cursor”, “Icons” and “Shell” themes to Pop as shown in the screenshot.

Before:

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/8.png)

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/9.png)

After:

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/10-1.png)

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/11-1.png)

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/12.png)

------

### **Installing Icons and Themes from Compressed Archives:**

You may find some icons and themes developers distribute their work as compressed archives. If this happens, then you can just extract these icons or themes and put them in either “.icons” or “.themes” directory inside your HOME directory. If these directories don’t exist already, just create them.

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/13-1.png)

If what you’re installing is an icon or cursor, put the extracted directory in the “.icons” directory inside HOME directory.

If what you’re installing is a theme, put the extracted directory in the “.themes” directory inside HOME directory.

Then just open GNOME Tweak Tool and select the Theme, Icons or Cursor you installed from the list.

It’s not possible to show everything because there are so many themes and icons out there. But I can assure you, if the theme you’re trying to install is compatible with the version of GNOME Shell you’re using, it will work.

Run the following command to find out what version GNOME Shell you’re using:

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/14.png)

This is how you customize GNOME 3 Desktop Environment on Ubuntu 17.10 using GNOME Tweak Tool. Thanks for reading this article.

------

看完上面的文章基本就已经了解的差不多了，老外的文章说的还是很详细的。

上面的文章实际上已经给出了一个主题的安装方式，而我想换一个主题，下面正式开始安装

------

https://www.opendesktop.org/s/Gnome/p/1171688/

去这个链接

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429121803984-914082047.png)

网页上有好几个标签：Prodect、FIles、Changelogs等等

找到Files标签，去下载文件。点击文件名就可以下载。

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429121841955-578359059.png)

可以看到这里一共有6个压缩文件，分别包装各种主题。通过文件名能发现每一个文件都有一个“2”，这个2的意思是该压缩包下有两个主题。

随便选中一个比如Gnome-OSC-HS--2themes.tar.xz（第一个文件），下载下来。

通过xz和tar命令解压

```shell
xz -d Gnome-OSC-HS--2-themes.tar.xz
tar xvf Gnome-OSC-HS--2-themes.tar.xz
```

 解压后得到的文件夹中有两个文件夹

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429122442367-1915958074.png)

这两个文件夹分别是两个主题，把这两个文件夹移动到/usr/share/themes下就可以了。

然后打开前面安装的工具Tweaks（中文下叫“优化”）,在“应用程序”英文是“Applications”这个选项下就可以选择刚刚安装的主题了。这几个截图是我安装主题后的截图。

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429122823939-394497790.png)

刚刚是两个文件夹，就是两个主题，这两个主题从名字上看只有transparent前面是否有个not，顾名思义就是有没有透明效果。

到现在已经修改了外观样式，最大化最小化的样式已经很苹果了，接下来修改文件夹等图标，去下面的链接下载

https://www.opendesktop.org/s/Gnome/p/1102582/

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429154102972-127816603.png)

解压后把文件都放到/usr/share/icons目录下，如下图（这是已经应用过主题的截图）所示：

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429154233688-1776948414.png)

然后去Tweaks中应用一下

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180429154346719-2011249705.png)

 

------

再更新点别的东西：

https://www.opendesktop.org/s/Gnome/p/1013741/

下载下面的

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180430224507785-1703816949.png)

应用下

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180430224439646-1134731024.png)

效果：

![img](/home/zzhenry/Boostnote/Ubuntu/How to Customize GNOME 3 Desktop Environment on Ubuntu 17.10.assets/871381-20180430224613985-870334125.png)

------

### **Reference**

[1]	http://www.cnblogs.com/feipeng8848/p/8970556.html/