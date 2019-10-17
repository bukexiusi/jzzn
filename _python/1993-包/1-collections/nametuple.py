# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 14:01
@Author  : 图南
@Email   : 935281275@qq.com
@File    : nametuple.py
@Description :
'''

import collections

'''定义tuple，且用属性访问，而不是索引'''
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# p.x = 2  此句报错,tuple不允许修改值