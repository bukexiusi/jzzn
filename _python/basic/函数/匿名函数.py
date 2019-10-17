# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/27 23:14
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 匿名函数.py
@Description :
'''


def make_incrementor(n):
    # lambda标识匿名函数     参数:返回值
    return lambda x: x + n


if __name__ == "__main__":
    # 以下代码还涉及闭包概念
    func = make_incrementor(210)
    print(func(0))
    print(func(1))

    array = [(1, 'z'), (2, 'y'), (3, 'x')]
    # sort改变自身 sorted返回新数组
    # key要接收一个函数，函数的参数是数组的元素，返回值是比较的值（数值默认从小到大，字符串默认遵从阿斯特妈表）
    array.sort(key=lambda item: item[0])
    print(array)
    array.sort(key=lambda item: item[1])
    print(array)


