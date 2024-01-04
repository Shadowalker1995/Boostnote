# 旧版pytorch中`torch.rfft`和`irfft`在新版本中的对应

pytorch旧版本 (1.7之前) 中有一个函数 `torch.rfft()`，但是新版本 (1.8、1.9) 中被移除了，添加了 `torch.fft.rfft()`，但它并不是旧版的替代品。

傅里叶的相关知识都快忘光了，网上几乎没有相关资料，看了老半天官方文档，终于找到了对应的函数。

虽然整个过程的细节我还没有完全搞懂，但是网上相关的资料实在太少了，所以我把我都知道的都写上来，希望对后来者有点帮助

## rfft

**旧版 pytorch**

首先，我是在[一篇论文的开源代码](https://github.com/chosj95/MIMO-UNet/blob/4a523544e3c5192f5305610b761ee3a4d5d74648/train.py#L59)里面看到的旧版 `rfft`

```python
label_fft1 = torch.rfft(label_img4, signal_ndim=2, normalized=False, onesided=False)
# label_img4为一张图片，dtype=torch.float32，size比如为[1,3,64,64]
```

旧版本中 [torch.rfft()](https://pytorch.org/docs/1.7.1/generated/torch.rfft.html#torch-rfft) 的参数说明为

> **input** (*[Tensor](https://pytorch.org/docs/1.7.1/tensors.html#torch.Tensor)*) – the input tensor of at least `signal_ndim` dimensions
>
> **signal_ndim** (*[int](https://docs.python.org/3/library/functions.html#int)*) – the number of dimensions in each signal. `signal_ndim` can only be 1, 2 or 3
>
> **normalized** (*[bool](https://docs.python.org/3/library/functions.html#bool),* *optional*) – controls whether to return normalized results. Default: `False`
>
> **onesided** (*[bool](https://docs.python.org/3/library/functions.html#bool),* *optional*) – controls whether to return half of results to avoid redundancy. Default: `True`

在上述的代码中，`signal_ndim=2` 因为图像是二维的，`normalized=False` 说明不进行归一化，`onesided=False` 则是希望不要减少最后一个维度的大小

在 1.7 版本 `torch.rfft` 中，有一个 warning，表示在新版中，要 "one-side ouput" 的话用 `torch.fft.rfft()`，要 "two-side ouput" 的话用 `torch.fft.fft()`。**这里的 one/two side，跟旧版的 onesided 参数对应，所以我们要的是新版的 `torch.fft.fft()`**

![img](%E6%97%A7%E7%89%88pytorch%E4%B8%ADtorch.rfft%E5%92%8Cirfft%E5%9C%A8%E6%96%B0%E7%89%88%E6%9C%AC%E4%B8%AD%E7%9A%84%E5%AF%B9%E5%BA%94.assets/v2-35516c9bd0dd59c03fa5e0c6932596cd_r.jpg)

需要注意的是，假设输入 tensor 的维度为 $[N_1,N2,\dots,N_d]$，则输出tensor的维度为 $[N_1,N2,\dots,N_d,2]$ (多一个维度) 。最后一个维度 2 表示复数中的实部、虚部，即 $z=a+bi$ 这样的复数，在旧版 pytorch 中表示为一个二维向量 $[a,b]$

**新版 pytorch**

新版pytorch中，各种在[新版本中各种fft的解释](https://pytorch.org/blog/the-torch.fft-module-accelerated-fast-fourier-transforms-with-autograd-in-pyTorch/)如下:

> `fft`, which computes a complex FFT over a single dimension, and `ifft`, its inverse
>
> the more general `fftn` and `ifftn`, which support multiple dimensions
>
> The "real" FFT functions, `rfft`, `irfft`, `rfftn`, `irfftn`, designed to work with signals that are real-valued in their time domains
>
> The "Hermitian" FFT functions, `hfft` and `ihfft`, designed to work with signals that are real-valued in their frequency domains
>
> Helper functions, like `fftfreq`, `rfftfreq`, `fftshift`, `ifftshift`, that make it easier to manipulate signals

可以看到这里也有 [`rfft`](https://pytorch.org/docs/stable/generated/torch.fft.rfft.html?highlight=fft#torch.fft.rfft)，官方文档说是用来处理都是实数的输入。但是它在前面的 warning 中说了是 one-side，而我们要的是 two-side。此外实数也可以看作是虚部都为 0 的复数，所以用 [`fft`](https://pytorch.org/docs/stable/generated/torch.fft.fft.html?highlight=fft#torch.fft.fft) 没问题

新版的 `rfft` 和 `fft` 都是用于一维输入，而我们的图像是二维，所以应该用 `rfft2` 和 `fft2`。在 [`fft2`](https://pytorch.org/docs/stable/generated/torch.fft.fft2.html?highlight=fft) 中，参数 `dim` 用来指定用于傅里叶变换的维度，默认 $(-2,-1)$，正好对应 $H,W$ 两个维度。

新版所有的 `fft` 都不将复数 $z=a+bi$ 存成二维向量了，而是一个数 $[a+bj]$，数据类型为 complex，输出 tensor 的维度还是 $[N_1,N2,\dots,N_d]$。所以如果要跟旧版中一样存成二维向量 (多一个维度)，需要用 `.real()` 和 `.imag()` 提取复数的实部和虚部，然后用 `torch.stack()` 堆到一起 (具体操作方式见总结)

## irfft

同理新版 pytorch 中，`torch.fft.ifft2()` 对应旧版中 `torch.irfft(xxx, signal_ndim=2, onesided=False)`; `torch.fft.irfft2()` 对应旧版中`torch.irfft(xxx, signal_ndim=2, onesided=True)`

同理，如果旧版中 `signal_ndim` 不管为多少，新版中都可以用 `torch.fft.ifftn()` 和 `torch.fft.irfftn()`

需要注意的是， 新版中要求输入的数据类型为 complex，即要求输入的维度不跟旧版一样将复数的实部和虚部存成二维向量 (即在最后多出一个值为2的维度)。如果说输入时以二维向量存复数，则需要使用 `torch.complex()` 将其转化成 complex 类型 (具体操作方式见总结)

## 总结

```python
import torch
input = torch.randn(1, 3, 64, 64)
### 旧版 ###
# 参数 normalized 对这篇文章的结论没有影响，加上只是为了跟文章开头同步
# 时域 => 频域
output_fft_old = torch.rfft(input, signal_ndim=2, normalized=False, onesided=False)
# 频域 => 时域
output_ifft_old = torch.irfft(output_fft_old , signal_ndim=2, normalized=False, onesided=False)

### 新版 ###
# 时域 => 频域
output_fft_new = torch.fft.fft2(input, dim=(-2, -1))
output_fft_new_2dim = torch.stack((output_fft_new.real, output_fft_new.imag), -1) # 根据需求将复数形式转成数组形式
# 频域 => 时域
output_ifft_new = torch.fft.ifft2(output_fft_new, dim=(-2, -1)) # 输入为复数形式
output_ifft_new = torch.fft.ifft2(torch.complex(output_fft_new_2dim[..., 0], # 输入为数组形式
							  output_fft_new_2dim[..., 1]), dim=(-2, -1))    
# 注意最后输出的结果还是为复数，需要将虚部丢弃
output_ifft_new = output_ifft_new.real
print((output_ifft_new - input).sum()) # 输出应该趋近于0 (因为存在数值误差)
```

