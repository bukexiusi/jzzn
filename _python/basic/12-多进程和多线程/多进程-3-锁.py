# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 14:22
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多线程-3-锁.py
@Description :
'''

import multiprocessing as mp
import time


def job(v, num):
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)


def multicore():
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def job_lock(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()


def multicore_lock():
    l = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job_lock, args=(v, 1, l))
    p2 = mp.Process(target=job_lock, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    # multicore()  # 不加锁
    multicore_lock()  # 加锁
