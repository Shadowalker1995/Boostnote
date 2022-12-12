# DarkNet-Yolo使用指南

## 数据准备

1. 数据目录 `<data_root>`：建议将数据放在`<darknet_root>/data/<dataset>`目录下。
2. 数据标签预处理：
   - 根据`scripts/voc_labels.py`文件建立自己数据集的预处理文件，建议为`scripts/<dataset>_labels.py`。
   - 预处理目标：
     - `<data_root>`下有`train.txt`和`valid.txt`两个文件，分别保存训练和测试图片路径，每行一个，带拓展名，绝对路径。
     - 在每个测试图片所在的目录下，有与其同名的标签文件，文件类型`.txt`，内容为所有的标签框，每行一个，格式为：`class_id x_center y_center width height`，后四个值的范围是[0, 1]，为其与图像宽或者高的比值（x对应宽，y对应高）。
3. 其他文件准备：
   - `<darknet_root>/data/<dataset>.names`存储每个类别的名称，每行一个，按编号顺序。
   - `<darknet_root>/cfg/<dataset>.data`存储数据集的信息，可参考`<darknet_root>/cfg/voc.data`进行修改。

## 命令参数

1. 训练模型
   - 单GPU训练：`./darknet -i <gpu_id> detector train <data_cfg> <train_cfg> <weights>`
   - 多GPU训练，格式为`0,1,2,3`：`./darknet detector train <data_cfg> <model_cfg> <weights> -gpus <gpu_list>`
   - CPU训练：`./darknet -nogpu detector train <data_cfg> <model_cfg> <weights>`
2. 测试图片
   - 测试单张图片，需要编译时有OpenCV支持：`./darknet detector test <data_cfg> <test_cfg> <weights> <image_file>`
   - `<test_cfg>`文件中`batch`和`subdivisions`两项必须为1。
   - 测试时还可以用`-thresh`和`-hier`选项指定对应参数。
3. 生成预测效果
   - `./darknet detector valid <data_cfg> <test_cfg> <weights> <out_file>`
   - `<test_cfg>`文件中`batch`和`subdivisions`两项必须为1。
   - 结果生成在`<data_cfg>`的`results`指定的目录下以`<out_file>`开头的若干文件中，若`<data_cfg>`没有指定`results`，那么默认为`<darknet_root>/results`。
4. 计算 recall
   - `./darknet detector recall <data_cfg> <test_cfg> <weights>`
   - `<test_cfg>`文件中`batch`和`subdivisions`两项必须为1。
   - 输出在stderr里，重定向时请注意。
   - `RPs/Img`、`IOU`、`Recall`都是到当前测试图片的均值。
   - `detector.c`中对目录处理有错误，可以参照`validate_detector`对`validate_detector_recall`最开始几行的处理进行修改。
5. 执行这些命令的时候在`<darknet-root>`下进行。

## detector.c 的修改方法：

489行和845行 `validate_detector_recall`函数定义和调用改为：

```c++
void validate_detector_recall(char *datacfg, char *cfgfile, char *weightfile)
validate_detector_recall(datacfg, cfg, weights);
```

`validate_detector_recall`内的`plist`和`paths`的如下初始化带吗：

```c++
list *plist = get_paths("data/voc.2007.test");
char **paths = (char **)list_to_array(plist);
```

修改为：

```c++
list *options = read_data_cfg(datacfg);
char *valid_images = option_find_str(options, "valid", "data/train.list");
list *plist = get_paths(valid_images);
char **paths = (char **)list_to_array(plist);
```

## Darknet 评估训练好的网络的性能

