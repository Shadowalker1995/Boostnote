# caffe 中多GPU的使用方法

由于在ubuntu中使用caffe的程序时，都使用.sh文件，该文件中常见的命令为：

```sh
./build/tools/caffe train --solver=examples/testXXX/solver.prototxt
```

当电脑中有多个GPU时，默认使用GPU0。如果想使用其他的GPU，可以将该文件内容修改如下：

```sh
./build/tools/caffe train --solver=examples/testXXX/solver.prototxt --gpu 2
```

注意，caffe中默认编号从0开始，因而 `--GPU 2` 的意思是使用第3个GPU。

如果要使用多个GPU，可以使用如下命令：

```sh
./build/tools/caffe train --solver=examples/testXXX/solver.prototxt --gpu 0,1,2,3
```

则使用0,1,2,3这4个GPU。

如果要使用所有的GPU，可使用如下命令：

```sh
./build/tools/caffe train --solver=examples/testXXX/solver.prototxt --gpu all
```

注意，使用的GPU越多，开始初始化时时间越久。当然，训练速度越快。