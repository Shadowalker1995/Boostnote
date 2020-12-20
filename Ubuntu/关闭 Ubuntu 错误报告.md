# 关闭 Ubuntu 错误报告

Ubuntu 桌面版预装了 Apport，它是一个错误收集系统，会收集软件崩溃、未处理异常和其他，包括程序 Bug，并为调试目的生成崩溃报告。当一个应用程序崩溃或者出现 Bug 时候，Apport 就会通过弹窗警告用户并且询问用户是否提交崩溃报告。

好像 Linux 的发行版里只有 Ubuntu 有这个错误报告？不管出于什么原因，这个东西我觉得很烦人，所以我把他关掉了

- 临时关闭 
  `sudo service apport stop`
  这个会在重启系统后失效。

- 永久关闭 
  我喜欢这个，因为感觉这个东西没什么卵用，可能是我菜。

  ```sh
  sudo gedit /etc/default/apport
  ```

  修改 `enabled=0`，重启生效

- 还有一个方法，但是个人感觉没有必要，就是永久性的移除这个功能 
  `sudo apt-get purge apport`