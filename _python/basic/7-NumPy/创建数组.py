# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/16 8:12
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 创建数组.py
@Description :
'''

import numpy as np


# 空数组，但是输出的数组包含值，是内存上次运行未清空的遗留值
x = np.empty([3, 3], dtype=int)
print(x)

# 全零数组
x = np.zeros([3, 3], dtype=int)
print(x)

# 全一数组
x = np.ones([3, 3], dtype=int)
print(x)

# asarray复制后内存共享 array复制后内存不共享
# asarray???
x = [1, 2, 3]
a = np.asarray(x)
print(a)
x.append(4)
x = (1, 2, 3)
a = np.asarray(x)
print(a)

# numpy.arange
x = np.arange(5)
print(x)
x = np.arange(5, dtype=float)
print(x)
x = np.arange(10, 20, 2)
print(x)

# numpy.linspace -> 一维数组，数组是一个等差数列
a = np.linspace(1, 10, 10)  # 1到10 10等分
print(a)
a = np.linspace(1, 10, 10, retstep=True)  # 输出等差值
print(a)
