# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/27 23:35
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 集合.py
@Description :
'''

set_a = {0, 1, 2, 3}
set_b = set([1, 2, 3, 4])
print(type(set_a))
print(type(set_b))

# 常用方式 并集、交集、差集、子集
print("a是b的子集 %s" % str(set_a.issubset(set_b)))

