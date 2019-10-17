# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 10:16
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多线程.py
@Description :
'''

import multiprocessing as mp
import threading as td


def job(a, d):
    print("aaa")

# t1 = td.Thread(target=job, args=(1, 2))
# t1.start()
# t1.join()


if __name__ == '__main__':

    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()  # 阻塞主进程，子进程执行完才能继续执行主进程
