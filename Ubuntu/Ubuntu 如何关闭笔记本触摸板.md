# Ubuntu 如何关闭笔记本触摸板

在 `~/.zshrc` 中加入：

```sh
alias opentp='sudo modprobe psmouse'		# open touchpad
alias closetp='sudo modprobe -r psmouse'	# close touchpad
```

