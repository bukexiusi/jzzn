# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 13:41
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-filter.py.py
@Description :
'''

print(filter(lambda a: a % 2 == 0, range(20)))
print(list(filter(lambda a: a % 2 == 0, range(20))))