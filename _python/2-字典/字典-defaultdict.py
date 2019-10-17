# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 13:52
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 字典-defaultdict.py
@Description :
'''

import collections

dict_ = collections.defaultdict(lambda: 0)
string = 'abbccc'
for c in string:
    dict_[c] += 1
print(dict_)
print(dict(dict_))
