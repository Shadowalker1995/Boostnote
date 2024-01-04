# Calibre中使用Fcitx搜狗输入法

安装 `fcitx-libs-qt5` 与 `libfcitx-qt5-1`

```bash
sudo apt-get install fcitx-libs-qt5 libfcitx-qt5-1
```

定位 `libFcitxQt5DBusAddons.so.1` 与 `libfcitxplatforminputcontextplugin.so` 文件的位置

```bash
dpkg -L fcitx-frontend-qt5

# output
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/qt5
/usr/lib/x86_64-linux-gnu/qt5/plugins
/usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts
/usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so
/usr/share
/usr/share/doc
/usr/share/doc/fcitx-frontend-qt5
/usr/share/doc/fcitx-frontend-qt5/README
/usr/share/doc/fcitx-frontend-qt5/changelog.Debian.gz
/usr/share/doc/fcitx-frontend-qt5/copyright
```

```bash
dpkg -L libfcitx-qt5-1

# output
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/fcitx
/usr/lib/x86_64-linux-gnu/fcitx/libexec
/usr/lib/x86_64-linux-gnu/fcitx/libexec/fcitx-qt5-gui-wrapper
/usr/lib/x86_64-linux-gnu/libFcitxQt5DBusAddons.so.1.0
/usr/lib/x86_64-linux-gnu/libFcitxQt5WidgetsAddons.so.1.0
/usr/share
/usr/share/doc
/usr/share/doc/libfcitx-qt5-1
/usr/share/doc/libfcitx-qt5-1/changelog.Debian.gz
/usr/share/doc/libfcitx-qt5-1/copyright
/usr/lib/x86_64-linux-gnu/libFcitxQt5DBusAddons.so.1
/usr/lib/x86_64-linux-gnu/libFcitxQt5WidgetsAddons.so.1
```

执行以下命令

```bash
sudo cp /usr/lib/x86_64-linux-gnu/libFcitxQt5DBusAddons.so.1 /opt/calibre/lib
sudo cp /usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so /opt/calibre/plugins/platforminputcontexts
```