# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/2 22:57
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 基础.py
@Description :
'''

import numpy as np

# 生成对角矩阵
print(np.eye(4))

# 创建一维ndarray对象
a = np.array([1, 2, 3])
print('a数组:', a)

# 创建多维ndarray对象
b = np.array([[1, 2], [3, 4]])

# 最小维度 默认为0 注意和a数组的区别
c = np.array([1, 2, 3], ndmin=2)
print('c数组', c)


'''
ndarray对象 存放同类型元素 -> 其中的每个元素在内存中都有相同存储大小的区域
            支持数据类型
                布尔
                数值（整数、小数、复数）
'''

'''
声明数据类型
'''
dt = np.dtype(np.int32)
print(dt)
dt = np.dtype('i4')
print(dt)
dt = np.dtype('<i4')  # 字节顺序标注
print(dt)
dt = np.dtype('i8')
print(dt)


dt = np.dtype([('age', np.int8)])
a = np.array([(10, ), (20, ), (30, )], dtype=dt)
print(a)
print(a['age'])

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])  # 取别名
a = np.array([('a', 18, 100), ('b', 19, 99)], dtype=student)
print(a)
print(a[0][1])
print(a['age'])

'''
秩        ndarray.ndim
维度      ndarray.shape     -> reshape改变数组维度（元素总数不变）
个数      ndarray.size
数据类型  ndarray.dtype
元素大小  ndarray.itemtype
内存信息  ndarray.flags
元素实部  ndarray.real
元素虚部  ndarray.imag
缓冲区    ndarray.data
'''