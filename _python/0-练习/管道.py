# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 9:35
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 管道.py
@Description :
'''

from multiprocessing import Pipe, Process


def func(conn1, conn2):
    conn2.close()
    while True:
        try:
            msg = conn1.recv()
            print(msg)
        except EOFError:  # 抛出无数据时异常
            conn1.close()
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    Process(target=func, args=(conn1, conn2)).start()
    conn1.close()
    for i in range(20):
        conn2.send('吃了么')
    conn2.close()
