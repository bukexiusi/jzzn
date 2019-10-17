# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/16 20:16
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 光标.py
@Description :
'''


f = open('1.txt', 'r')
f.seek(3)
print(f.tell())  # 显示当前光标位置
