# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 11:10
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程多线程效率对比.py
@Description :
'''
import threading as td
import multiprocessing as mp
import time

num = 10000000


def a(q):
    res = 0
    for i in range(num):
        res += i + i ** 2 + i ** 3
    q.put(res)


def normal():
    res = 0
    for _ in range(2):
        for i in range(num):
            res += i + i ** 2 + i ** 3
    # print(res)


def multipro():
    q1 = mp.Queue()
    q2 = mp.Queue()
    p1 = mp.Process(target=a, args=(q1,))
    p2 = mp.Process(target=a, args=(q2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # print(q1.get() + q2.get())


def multith():
    q1 = mp.Queue()
    q2 = mp.Queue()
    t1 = td.Thread(target=a, args=(q1,))
    t2 = td.Thread(target=a, args=(q2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # print(q1.get() + q2.get())


if __name__ == "__main__":
    st = time.time()
    normal()
    ed = time.time()
    print("主线程：", ed - st)

    st = time.time()
    multipro()
    ed = time.time()
    print("多进程：", ed - st)

    st = time.time()
    multith()
    ed = time.time()
    print("多线程：", ed - st)
