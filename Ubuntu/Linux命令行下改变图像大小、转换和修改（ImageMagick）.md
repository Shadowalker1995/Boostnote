# Linux命令行下改变图像大小、转换和修改（ImageMagick）
ImageMagick是linux命令行工具，用来操作图片。ImageMagick提供了对图像的基本操作，可以处理多个图像，也可以和bash脚本集成。
## 安装ImageMagick
对于Ubuntu：
```shell
sudo apt-get install imagemagick
```

## 转换格式
例如把png格式图像转换为jpg格式：
```shell
convert source.png dest.jpg
```

你还可以指定压缩等级：
```shell
convert source.png -quality 95 dest.jpg
```

质量的等级范围1-100。
## 改变图像大小
例如要把图像改为200×100像素，执行：
```shell
 convert example.png -resize 200×100 example1.png
```

上面命令不会改变图像的比例，所以转换后的图像不一定完全是200×100。如果要强制改变比例，使用如下命令：
```shell
convert example.png -resize 200×100! example1.png
```

也可以使用单独指定一个高或宽（保持比例）。以下命令将调整图像的宽度为200：
```shell
convert example.png -resize 200 example1.png
```

以下命令将调整图像的高度为100：
```shell
convert example.png -resize x100 example1.png
```

## 旋转图像
如果您指定了相同的文件名，ImageMagick会将旋转的图像保存在原始图像文件上。
```shell
convert abc.jpg -rotate 90 abc-rotated.jpg
```

## 添加效果
ImageMagick可以应用多用效果，例如：
```shell
convert abc.jpg -charcoal 2 abc-charcoal.jpg
convert abc.jpg -implode 1 abc-imploded.jpg
```

## 组合操作
上面的操作都可以放到一条命令中，例如：
```shell
convert abc.png -resize 400×400 -rotate 180 -charcoal 4 -quality 95 abc1.jpg
```

## 对多个图片进行处理
旋转当前目录的所有png图像。
```shell
for file in *.png; do convert $file -rotate 90 rotated-$file; done
```