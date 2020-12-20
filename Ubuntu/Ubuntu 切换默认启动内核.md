# Ubuntu 切换默认启动内核

1. 查看可更新的内核：

   ```sh
   sudo apt-cache search linux
   ```

   该命令将会显示所有可以获取的内核

2. 安装内核，假设你要安装的内核为2.6.39-0，则使用下面的命令

   ```sh
   
   ```

   重启后，即是以新内核启动

   如果要换回原来的内核，比如现在是3.2.0-23，则先使用命令

   ```sh
   grep menuentry /boot/grub/grub.cfg
   ```

   该命令显示内核的顺序，比如显示为：

   ```sh
   menuentry 'Ubuntu, with Linux 3.2.17experimental' --class ubuntu --class gnu-linux --class gnu --class os {
   menuentry 'Ubuntu, with Linux 3.2.17experimental (recovery mode)' --class ubuntu --class gnu-linux --class gnu --class os {
   menuentry 'Ubuntu, with Linux 3.2.17-chipsee' --class ubuntu --class gnu-linux --class gnu --class os {
   menuentry 'Ubuntu, with Linux 3.2.17-chipsee (recovery mode)' --class ubuntu --class gnu-linux --class gnu --class os {
   menuentry 'Ubuntu, with Linux 3.2.0-23-generic' --class ubuntu --class gnu-linux --class gnu --class os {
   menuentry 'Ubuntu, with Linux 3.2.0-23-generic (recovery mode)' --class ubuntu --class gnu-linux --class gnu --class os {
   menuentry "Memory test (memtest86+)" {
   menuentry "Memory test (memtest86+, serial console 115200)"
   ```

3. 假设你要以3.2.17内核版本启动，则将文件 `/etc/default/grub` 中

   `GRUB_DEFAULT=0`

   改为

   `GRUB_DEFAULT=2` 

   保存后使用命令 `sudo update-grub`

   重启后，使用命令 `uname -a` 查看，内核即为你想要的内核