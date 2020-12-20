# Ubuntu 设置 sudo 为不需要密码

通常我们并不以root身份登录，但是当我们执行某些命令 (command)时需要用到root权限，我们通常都是用`sudo command`来执行command。

 假设我的用户名为`zzhenry`（属于 admin组），使sudo不用密码的方法如下。

`sudo visudo` 或者 `sudo vim /etc/sudoers`

如果vi来编辑，则保存时记得用`wq!`强制保存，否则会提示只读不能保存的。

默认情况我们会看到有`%admin ALL=(ALL) ALL`一句话，就是允许admin组在所有主机上执行所有命令，当然是需要passwd的。

1. 如果想把admin组的用户都sudo不用密码那么可以将这一行换为 `%admin ALL=(ALL) NOPASSWD:NOPASSWD ALL` 即可。
2. 如果仅仅想让zzhenry用户sudo不需密码，则可添加`zzhenry ALL=(ALL:ALL) NOPASSWD:ALL`这样一行。
3. 如果让zzhenry用户sudo不用密码即可执行某几个命令，可这样写`zzhenry ALL=(ALL:ALL) NOPASSWD:/usr/bin/abc.sh,/usr/sbin/adduser` 
4. 其他更多配置方式，运行`man sudoers`看帮助文档。
5.  注意：`zzhenry ALL=(ALL:ALL) NOPASSWD: ALL` 这一行必须在 `%admin ALL=(ALL) ALL` 之后，不然后面的组配置覆盖了前面的配置，而zzhenry属于admin组，所以zzhenry执行sudo时还是需要输入密码。

