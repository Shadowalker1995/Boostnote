# Ubuntu20.04 安装搜狗输入法

点击左下角菜单选择语言支持，将语言选择为fcitx

<img src="Ubuntu20.04%20%E5%AE%89%E8%A3%85%E6%90%9C%E7%8B%97%E8%BE%93%E5%85%A5%E6%B3%95.assets/imageurl=%252F_next%252Fstatic%252Fmedia%252Fhelp7.d6d18871.png&w=3840&q=75" alt="点击左下角菜单选择语言支持，将语言选择为fcitx（如下图二）" style="zoom: 33%;" />

<img src="https://shurufa.sogou.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhelp8.7e2ac26c.png&w=1080&q=75" alt="点击左下角菜单选择语言支持，将语言选择为fcitx（如下图二）" style="zoom: 67%;" />

```bash
sudo apt-get update
sudo apt-get install fcitx
# 设置fcitx开机自启动
sudo cp /usr/share/applications/fcitx.desktop /etc/xdg/autostart/
# 卸载系统ibus输入法框架
sudo apt-get purge ibus
# 安装搜狗输入法
sudo dpkg -i $HOME/Softwares/start/sogoupinyin_4.0.1.2800_x86_64.deb
# 安装依赖
sudo apt-get install libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2
sudo apt-get install libgsettings-qt1
```

重启电脑