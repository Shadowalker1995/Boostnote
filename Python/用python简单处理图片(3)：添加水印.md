# 用python简单处理图片(3)：添加水印

## 一、添加文字水印

```
from PIL import Image, ImageDraw,ImageFont
im = Image.open("d:/pic/lena.jpg").convert('RGBA')
txt = Image.new('RGBA', im.size, (0,0,0,0))
fnt = ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
d = ImageDraw.Draw(txt)
d.text((txt.size[0]-80,txt.size[1]-30), "cnBlogs", font = fnt, fill = (255,255,255,255))
out = Image.alpha_composite(im, txt)
out.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201511/140867-20151126204356109-452054020.jpg)

## 二、添加小图片水印

```
from PIL import Image
im = Image.open("d:/pic/lena.jpg")
mark = Image.open("d:/logo_small.gif")
layer = Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-150, im.size[1]-60))
out = Image.composite(layer, im,layer)
out.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201511/140867-20151126205001906-1625795222.jpg)