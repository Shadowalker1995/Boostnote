# Linux tar 命令示例

在Linux平台，tar是主要的打包工具。tar命令通常用来把文件和目录压缩为一个文件（ **tarball** 或 **tar**, **gzip** 和 **bzip）。**

### Tar选项：

- **c** – 创建压缩文件
- **x** – 解压文件
- **v** – 显示进度.
- **f** – 文件名.
- **t** – 查看压缩文件内容.
- **j** – 通过bzip2归档
- **z** –通过gzip归档
- **r** – 在压缩文件中追加文件或目录
- **W** – 验证压缩文件
- **wildcards**

### 把目录/home/abc/code 打包为code.tar

```bash
tar -cvf code.tar /home/abc/code/
```

### 压缩为 tar.gz 格式的包

```bash
tar -cvzf code.tar.gz /home/abc/code
```

### 压缩率更高的 tar.bz2 格式的包

```bash
tar -cvfj code.tar.bz2 /home/abc/code/
```

### 解压 tar 包

```bash
tar -xvf code.tar -C /home/abc/code
```

### 解压 tar.gz 包

```bash
tar -xvf code.tar.gz
```

### 解压 tar.bz2 包

```bash
tar -xvf code.tar.bz2
```

### 列出 tar 包内容

```bash
tar -tvf code.tar
```

### 解压tar包中的单个文件

```bash
tar --extract --file=code.tar Readme.txt
```

### 解压tar包中的多个文件

```bash
tar -xvf code.tar "file 1" "file 2"
```

### 解压同一种类型的文件(下面代码是解压txt)

```bash
tar -xvf code.tar --wildcards *.txt'
```

### 在tar包中加入文件或目录

```bash
tar -rvf code.tar abcd.txt   // 文件
tar -rvf code.tar Doc        // 目录
```



http://blog.topspeedsnail.com/archives/202