# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/30 11:44
@Author  : 图南
@Email   : 935281275@qq.com
@File    : demo.py
@Description : *args-匹配无参数名输入，元组输出， **kw-匹配有参数名输入，字典输出
'''


def a(aa, bb, cc):
    print(aa, bb, cc)


def b(aa, *args):
    print(aa, args)


if __name__ == "__main__":
    a(1, 2, 3)
    li = [4, 5, 6]
    a(*li)
    li2 = [8, 9]
    a(7, *li2)

    b(1, 2, 3, 4)
    b(1, [2, 3, 4])
    b(1, (2, 3, 4))

