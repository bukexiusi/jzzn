# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/4 11:33
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 迭代器.py
@Description :
'''

# 字符窜、数组、元组、字典为可迭代对象，可以用for循环的对象都是可迭代对象
for i in '', [], (), {}:
    print(i)

# 可以用for循环的对象都是可迭代对象
a = (j for j in range(100))
print(a)
print(list(a))

# 判断是否为可迭代对象
from collections import Iterable

isinstance('abc', Iterable)
b = [1, 2, 3, 4, 5]
c = iter(b)  # 使用iter()方法可以将可迭代对象转换为可迭代器。

pass
