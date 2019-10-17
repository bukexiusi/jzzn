# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 10:51
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多线程.py
@Description :  多线程例子
'''

import threading as td
import multiprocessing as mp


def a(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)


# 多进程一定要放在main函数执行，否则报错
if __name__ == "__main__":
    q1 = mp.Queue()
    q2 = mp.Queue()
    t1 = td.Thread(target=a, args=(q1,))
    t2 = td.Thread(target=a, args=(q2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(q1.get() + q2.get())
