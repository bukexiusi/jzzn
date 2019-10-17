# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/22 15:01
@Author  : 图南
@Email   : 935281275@qq.com
@File    : demo.py
@Description :
'''


def add(x: int, y: int=5)-> int:  # :int 标识了参数应该出现的类型。为参数注解。->int 标注返回值为int类型
    """
    加法函数
    :param x: int类型
    :param y: int类型
    :return:  int类型
    """
    return x+y
