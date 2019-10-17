# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/30 20:46
@Author  : 图南
@Email   : 935281275@qq.com
@File    : itertools.py
@Description :
'''

import itertools

# 串联迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# 相邻的重复元素
for c, group in itertools.groupby('AABCAB'):
    print(c, list(group))

data = [
    ("1", "张三", 93),
    ("1", "李四", 94),
    ("1", "王五", 95),
    ("2", "赵六", 95),
    ("2", "鬼七", 95),
    ("3", "神八", 95),
]
for key, group in itertools.groupby(data, key=lambda m: m[0]):
    print(key, list(group))

for key, group in itertools.groupby(data, key=lambda m: m[2]):
    print(key, list(group))
