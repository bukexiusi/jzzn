# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/4 22:59
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 装饰器.py
@Description :
'''


# 装饰器原理（无参）
def functin(func):
    def func_in():
        print("装饰器内容")
        func()
    return func_in


