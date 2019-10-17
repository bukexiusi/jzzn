# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/6 11:06
@Author  : 图南
@Email   : 935281275@qq.com
@File    : basic.py
@Description :
'''

import copy

a = {"a": {"a": "a"}}
b = a
b["a"] = {"b": "b"}
print(a)

c = copy.copy(a)
c["c"] = "c"
print(a)
print(c)
