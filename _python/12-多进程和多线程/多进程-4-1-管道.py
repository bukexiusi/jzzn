# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 14:38
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程-4-管道.py
@Description :
'''

from multiprocessing import Pipe, Process


def func(conn1, conn2):
    conn2.close()  # 子进程只需使用connection1,故关闭connection2
    while True:
        try:
            msg = conn1.recv()
            print(msg)
        except EOFError:  # 没收数据接收的时候,才抛出的异常
            conn1.close()
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe()                # 建立一个管道,管道返回两个connection,全双工
    # conn1, conn2 = Pipe(duplex=False)  # 建立一个管道,管道返回两个connection,conn1只能用于接收,conn2只能用于发送
    Process(target=func, args=(conn1, conn2)).start()
    conn1.close()  # 主进程只需要一个connection,故关闭一个
    for _ in range(20):
        conn2.send('吃了吗')  # 主进程发送
    conn2.close()  # 主进程关闭connection2
