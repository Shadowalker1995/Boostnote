# Python 设置文件缓冲

文件的缓冲通常分为：全缓冲，行缓冲，无缓冲

在某些tty设备（比如终端设备）就是使用的行缓冲

串口设备就是无缓冲

设置文件的缓冲行为：

- 全缓冲：open 函数中的 buffering 设置为大于 1 的整数 n , n 为缓冲区大小
- 行缓冲：open 函数中的 buffering 设置为1
- 无缓冲：open 函数中的 buffering 设置为0

### 全缓冲：

```python
f = open('demo1.txt', 'w', buffering=20)
f.write('=' * 20)
```

在 terminal 中使用 `tail -f demo1.txt` 监测到：

```shell
====================
```

### 行缓冲：

```python
f = open('demo2.txt', 'w', buffering=1)
f.write('1234\n')
```

在 terminal 中使用 `tail -f demo2.txt` 监测到：

```shell
1234
```

### 无缓冲

```python
f = open('demo3.txt', 'w', buffering=0)
f.write('abcde')
```

在 terminal 中使用 `tail -f demo3.txt` 监测到：

```shell
abcde	# 直接显示
```