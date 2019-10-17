# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/4 11:04
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)_生成列表.py
@Description :
'''

range(1, 100, 5)  # 第一个参数表示开始位，第二个参数表示结束位（不含），第三个参数表示步长，就是每5个数返回一次。

a = [i for i in range(1, 10)]  # 列表生成式表示返回i的值，并且返回9次，每次返回的是i的值。
print(a)

a = [2 for i in range(1, 10)]  # 这里表示返回2，并且返回9次，但是每次的值都是2。
print(a)

a = [i for i in range(10) if i % 2 == 0]  # 表示在生成式内部加入if判断，当i除以2的余数等于0的时候将数值返回。
print(a)

a = [(i, j) for i in range(5) for j in range(5)]  # 表示将i和j的值以元组为元素的形式返回，当i循环一次的时候j循环5次，以此类推
print(a)
