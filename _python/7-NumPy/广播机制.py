# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/27 12:41
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 广播机制.py
@Description :
'''

'''broadcast 广播'''
'''对于不同shape的数组进行数值计算'''

import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
print(a * b)

'''以上例子触发了broadcast机制'''
'''实际上是[1, 2, 3] * [2, 2, 2]'''

c = np.array([
    [0.0, 0.0, 0.0],
    [10.0, 10.0, 10.0],
    [10.0, 10.0, 10.0]
])
d = np.array([1, 2, 3])
print(c + d)

'''以上例子触发了broadcast机制'''
'''实际上是
[
    [0.0, 0.0, 0.0],
    [10.0, 10.0, 10.0],
    [10.0, 10.0, 10.0]
]
+
[
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
'''

'''
broadcast机制
1、相互运算的数组的末位秩必须相等
    3*3 和 1*3
2、相互运算的数组的末位秩为1

以下例子无法计算
4 * 3 和 1 * 4，原因末位秩不相等
'''

e = np.array([1, 2, 3, 4])
f = np.array([1, 2, 3])
print(e[:, np.newaxis])
print(e[:, np.newaxis] + f)
print(f[:, np.newaxis])
print(f[:, np.newaxis] + e)

