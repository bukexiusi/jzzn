# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 11:23
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程-进程池.py
@Description :
'''

import multiprocessing as mp


def job(x):
    return x ** 2


def multicore():
    pool = mp.Pool()  # 默认所有cpu
    # pool = mp.Pool(processes=2)  # 使用两个cpu
    res = pool.map(job, range(10))  # map传入多份值（多次调用方法）分配给多个进程处理
    print(res)

    res = pool.apply_async(job, (2,))  # apply_async传入一份值（一次调用方法）分配给单个进程处理
    print(res.get())

    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == "__main__":
    multicore()
