# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 13:56
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程-共享数据.py
@Description :
'''

import multiprocessing as mp

value = mp.Value('d', 1)
array = mp.Array('i', [1, 3, 4])  # 只支持一维

# 数据类型参考pic/2019-09-11_141711.png

