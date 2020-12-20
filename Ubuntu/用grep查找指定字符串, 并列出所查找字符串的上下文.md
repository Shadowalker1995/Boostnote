# 用grep查找指定字符串, 并列出所查找字符串的上下文

grep 的 -B 参数指定显示所查找字符串之前的几行， -A 参数指定显示所查找字符串之后的几行

```bash
grep -B 3 -A 3 string filename.txt
```

-C 参数显示所查找字符串前后相同的行数，效果同上命令。

```bash
grep -C 3 string filename.txt
```



http://blog.topspeedsnail.com/archives/72