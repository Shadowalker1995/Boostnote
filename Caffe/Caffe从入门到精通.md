# Caffe从入门到精通

[TOC]

## Caffe源码解读

### 文件夹结构说明

- data: 用于存放下载的训练数据
- docs: 帮助文档
- examples: 一些代码样例
- matlab: Matlab接口文件
- python: Python接口文件
- models: 一些预训练好的模型参数
- scripts: 一些文档和数据用到的脚本

### 核心代码文件夹

- tools: 保存的源码是用于生成二进制处理程序的, 也是我们直接使用命令行时候调用的程序
- include: Caffe的头文件 `.hpp`, 命名方式一般为网络名字开头
- src: Caffe的源文件 `.cpp`对应CPU程序, `.cu`对应GPU程序

### src/caffe核心源码结构

- test: 用gtest测试caffe的代码
- util: 用于数据转换
- proto: 是一种数据存储格式, 帮助caffe提速, 注意: 我们在添加网络的时候, 需要在这个文件夹中添加相应的配置, 除此之外, 还需要添加相应的`.hpp`和`.cpp`文件到include和src中
- layers: 定义并实现了网络的前向、反向等方法
- Solvers: 定义并实现了一系列优化方法, 入SGD, Adam等

## Caffe必备文件

1. solver.prototxt: 配置模型训练的超参数
2. train_val.prototxt: 训练网络
3. deploy.prototxt: 测试网络

###solver.prototxt

- `net :=` 指定带训练模型结构文件, 若没有明确指定训练和测试网络, 则使用同一个网络结构文件 train_val.prototxt
- `test_interval :=` 测试间隔
- `test_iteration :=` 测试时进行的迭代次数, 等于测试集容量/测试网络的batch size
- `based_lr :=` 基本学习率
- `lr_policy :=` 学习率变更策略
- `gamma :=` 学习率变更策略需要用到的参数
- `power :=` 同上
- `stepsize :=` 学习率变更策略Step的变更步长 (固定步长)
- `stepvalue :=` 学习率变更策略Multistep的变更不长 (可变步长)
- `max_iter :=` 模型训练的最大迭代次数
- `momentum :=` 动量, 这是优化策略 (Adam, SGD, ...) 用到的参数
- `momentum2 :=` 优化策略Adam用到的参数
- `weight_decay :=` 权重衰减率
- `display :=` 每隔几次迭代显示一次结果
- `snapshot :=` 快照, 每隔几次保存一次模型参数
- `snapshot_prefix :=` 保存模型文件的前缀, 可以是路径
- `type :=` sover优化策略, 即SGD, Adam等
- `solver_mode :=` 模型训练模式, 即GPU/CPU
- `device_id :=` 指定设备号 (使用GPU模式), 默认为0

## 深度学习中的标准层

- 数据输入层: Data, ImageData, MemoryData 等
- 视觉层: Convolution, Pooling, BN, LRN, im2col 等
- 激活层: relu, sigmoid 等
- 损失层: softmax-loss, Euclidean 等
- 循环层: RNN, LSTM 等
- 工具层: reshape, concat, flatten, slice 等
- 普通层: dropout层, 全连接层, embed层