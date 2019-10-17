# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/20 10:36
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 作用域.py
@Description :
'''
a = 1


def b():
    a = 2
    global a
    print(a)

b()
