# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 11:40
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-zip.py
@Description :
'''

l = [1, 2, 3]
for index, val in enumerate(l):
    print('index is %d, val is %d' % (index, val))

print(*l, sep="\n")
print(l, sep="\n")
