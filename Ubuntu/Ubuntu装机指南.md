```bash
zzhenry@5016-Ubuntu:~$ ll
total 88
drwxr-xr-x 18 zzhenry zzhenry 4096 9月  30 12:55 ./
drwxr-xr-x  4 root    root    4096 9月  30 10:53 ../
-rw-------  1 zzhenry zzhenry  288 9月  30 12:39 .bash_history
-rw-r--r--  1 zzhenry zzhenry  220 9月  30 10:53 .bash_logout
-rw-r--r--  1 zzhenry zzhenry 3771 9月  30 10:53 .bashrc
drwxrwxr-x 13 zzhenry zzhenry 4096 9月  30 12:51 .cache/
drwx------ 15 zzhenry zzhenry 4096 9月  30 12:55 .config/
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Desktop/
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Documents/
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Downloads/
drwx------  3 zzhenry zzhenry 4096 9月  30 12:38 .gnupg/
drwxr-xr-x  3 zzhenry zzhenry 4096 9月  30 11:01 .local/
drwx------  4 zzhenry zzhenry 4096 9月  30 12:51 .mozilla/
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Music/
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Pictures/
drwx------  3 zzhenry zzhenry 4096 9月  30 12:55 .pki/
-rw-r--r--  1 zzhenry zzhenry  807 9月  30 10:53 .profile
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Public/
drwxrwxr-x  2 zzhenry zzhenry 4096 9月  30 12:53 Softwares/
drwx------  2 zzhenry zzhenry 4096 9月  30 12:39 .ssh/
-rw-r--r--  1 zzhenry zzhenry    0 9月  30 11:05 .sudo_as_admin_successful
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Templates/
drwxr-xr-x  2 zzhenry zzhenry 4096 9月  30 11:01 Videos/


```



```bash
sudo passwd
sudo apt-get update
sudo apt-get upgrade
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
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
# sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install g++ gcc make cmake vim ssh git nvidia-driver-515 net-tools samba smbclient barrier vlc liferea goldendict openssh-server rhythmbox qbittorrent x11vnc ubuntu-restricted-extras smplayer okular fcitx-bin fcitx-table flameshot -y
```



## install Typora

```bash
wget -qO - https://typoraio.cn/linux/public-key.asc | sudo tee /etc/apt/trusted.gpg.d/typora.asc

# add Typora's repository

sudo add-apt-repository 'deb https://typoraio.cn/linux ./'

sudo apt-get update

# install typora

sudo apt-get install typora
```

## No password for sudoer

edit `/etc/sudoer`

```bash
%sudo	ALL=(ALL:ALL) NOPASSWD: ALL
```

## 中文输入法



## Chrome

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

## Change source

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup

```





