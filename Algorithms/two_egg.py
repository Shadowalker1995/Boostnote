#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
FileName: two_egg.py
Author:   Zhu Zhan
Email:    henry664650770@gmail.com
Date:     2022-11-03 15:01:03
"""

def two_egg(n: int) -> int:
    """
    双蛋问题的递归求解
    :param n: 楼层数
    :return: 最糟糕的情况下, 找到临界楼层所需最少尝试数目
    """
    if n == 0:      # 没有楼就不需要试
        return 0
    elif n == 1:    # 有一层楼, 试一次
        return 1;
    result_list = []
    for k in range(1, n + 1):   # 在每一层都试一下
        # 把每一层的情况都记录下来
        result_list.append(max(k - 1, two_egg(n - k)) + 1)

    return min(result_list)     # 最好的结果就是我们想要的

# 用 1 到 11 的数字测试, 不用 100 是因为电脑性能不够, 测到 11 是因为 10 和 11 的结果不同
for f in range(1, 12):
    print(f'{f} -------> {two_egg(f)}')

# --------------------------------------------------------------

def two_egg_opt(n: int, result_dict: dict) -> int:
    """
    双蛋问题递归求解的优化
    :param n: 楼层数
    :param result_dict: 储存结果的字典
    :return: 最糟糕的情况下, 找到临界楼层所需最少尝试数目
    """
    if n in result_dict:
        return result_dict[n]
    else:
        result_list = []
        for k in range(1, n + 1):   # 在每一层都试一下
            # 把每一层的情况都记录下来
            result_list.append(max(k - 1, two_egg_opt(n - k, result_dict)) + 1)
        result_dict[n] = min(result_list)   # 最好的结果就是我们想要的
        return min(result_list)

# 从前计算的结果记录在result_dict中, 下次使用可以直接拿, 极大减少了递归层数
result_dict = {0: 0, 1: 1}
for i in range(1, 101):
    result_dict[i] = two_egg_opt(i, result_dict)
print(result_dict)

# --------------------------------------------------------------

def two_egg_general(m: int, n:int) -> int:
    """
    普遍双蛋问题的解决
    :param m: 鸡蛋数量
    :param n: 楼层总层数
    :return: 最糟糕的情况下, 找到临界楼层所需最少尝试数目
    """
    if n == 0:      # 如果没有楼, 不需要试
        return 0
    if n == 1:      # 只有 1 层楼, 试一次就足够
        return 1
    if m == 1:      # 只有 1 个蛋, 有几层楼就要使几次
        return n
    result_list = []
    for k in range(1, n + 1):
        result_list.append(max(two_egg_general(m - 1, k - 1), two_egg_general(m, n-k)) + 1)
    return min(result_list)

for i in range(1, 12):
    for j in range(1, 12):
        print(f'({i}, {j}) --> {two_egg_general(i, j)}', end=' | ')
    print()

# --------------------------------------------------------------

def two_egg_gen_opt(m: int, n: int, result_dict: dict) -> int:
    """
    普遍双蛋问题递归解决的优化
    :param m: 鸡蛋数量
    :param n: 楼层总层数
    :param result_dict: 储存结果的字典
    :return: 最糟糕的情况下, 找到临界楼层所需最少尝试数目
    """
    if (m, n) in result_dict:
        return result_dict[(m, n)]
    if n == 0:      # 如果没有楼, 不需要试
        result_dict[(m, n)] = 0
        return 0
    elif n == 1:    # 如果没有楼, 不需要试
        result_dict[(m, n)] = 1
        return 1
    if m == 1:      # 只有 1 个蛋, 有几层楼就要使几次
        result_dict[(m, n)] = n
        return n
    result_list = []
    for k in range(1, n + 1):
        result_list.append(max(two_egg_gen_opt(m - 1, k - 1, result_dict), two_egg_gen_opt(m, n - k, result_dict)) + 1)
    result_dict[(m, n)] = min(result_list)
    return min(result_list)

result_dict = {}
for i in range(1, 20):
    for j in range(1, 1002):
        print(f'({i}, {j}) --> {two_egg_gen_opt(i, j, result_dict)}', end=' | ')
    print()

