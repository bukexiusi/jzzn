# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 10:42
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程.py
@Description : 多进程例子，不涉及进程之间的通信
'''

import multiprocessing as mp


def a(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)


# 多进程一定要放在main函数执行，否则报错
# 不允许有返回值，只要通过队列实现返回
if __name__ == "__main__":
    q1 = mp.Queue()
    q2 = mp.Queue()
    p1 = mp.Process(target=a, args=(q1,))
    p2 = mp.Process(target=a, args=(q2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(q1.get() + q2.get())
