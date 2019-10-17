# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/22 12:36
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)_无序去重和有序去重.py
@Description :
'''


a = ["a", "b", "c", "c", "d", "e", "e"]
b = list(set(a))  # 无序去重
print(b)

c = list(set(a))
c.sort(key=a.index)  # 有序去重
print(c)

'''
原有的有序序列被转成无序序列，原有序列的索引值也不会被改变
'''
