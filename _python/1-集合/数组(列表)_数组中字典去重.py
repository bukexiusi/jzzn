# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 11:48
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-数组中字典去重.py
@Description :
'''
from functools import reduce
arr = [
    {'text': 'wuyuan','value': 1},
    {'text': '默认','value': 2},
    {'text': '默认','value': 2},
    {'text':  'wyy', 'value': 4}
]
f = lambda x, y: x if y in x else x + [y]
array = [[]] + arr  # 真正迭代的数组
print(array)
arr = reduce(f, array)
print(arr)


def func(x, y):
    if y in x:
        return x
    else:
        return x + [y]
