# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 13:22
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-reduce.py.py
@Description :
'''

from functools import reduce

a = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, a))

'''进阶-参考数组(列表)-数组中字典去重.py'''
l1 = [1, 2, 3, 4, 4]
print(list(set(l1)))
l1 = ["1", "2", "3", "4", "4"]
print(list(set(l1)))
l1 = [{"a": "1"}, {"a": "2"}, {"a": "2"}, {"s": "4"}]
print(list(set(l1)))


