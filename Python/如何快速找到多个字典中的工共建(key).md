# 如何快速找到多个字典中的工共建(key)

## 实际问题

随机生成三个字典：

```python
from random import randint, sample

# sample 为随机取样函数，第二个参数为取样的个数
s1 = {x: randint(1, 4) for x in sample('avcdefg', randint(3,6))}
s2 = {x: randint(1, 4) for x in sample('avcdefg', randint(3,6))}
s3 = {x: randint(1, 4) for x in sample('avcdefg', randint(3,6))}

s1 = {'d': 1, 'g': 2, 'v': 3}
s2 = {'c': 4, 'e': 4, 'd': 2, 'g': 1, 'f': 3, 'v': 1}
s3 = {'a': 3, 'g': 3, 'f': 4}
```

找出其中的的公共键。

## 解决方案

1. **使用字典的 viewkeys() 方法，得到一个字典 keys 的集合。**

   ```python
   s1.viewkeys()
   Out[7]: dict_keys(['d', 'g', 'v'])
       
   s2.viewkeys()
   Out[8]: dict_keys(['c', 'e', 'd', 'g', 'f', 'v'])
       
   s3.viewkeys()
   Out[9]: dict_keys(['a', 'g', 'f'])
       
   s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
   Out[10]: {'g'}
   ```

   对于字典个数有限的情况，我们可以通过 & 运算符做集合的交集操作，如果是对于字典个数N不确定的时候，应该使用 map 函数。

2. **使用 map 函数，得到所有字典的 keys 的集合。**

   ```python
   map(dict.viewkeys, [s1, s2, s3])
   Out[11]: 
   [dict_keys(['d', 'g', 'v']),
    dict_keys(['c', 'e', 'd', 'g', 'f', 'v']),
    dict_keys(['a', 'g', 'f'])]
   ```

3. **使用 reduce 函数，取所有字典的 keys 的集合的交集。**

   ```python
   reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))
   Out[12]: {'g'}
   ```