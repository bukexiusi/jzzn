# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 14:43
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程-4-2-管道.py
@Description :
'''

from multiprocessing import Process, Pipe, Lock
import time

def consumer(p, name, lock):
    produce, consume = p
    produce.close()
    while True:
        time.sleep(0.1)
        lock.acquire()
        baozi = consume.recv()
        lock.release()
        if baozi:
            print('%s 收到包子:%s' % (name, baozi))
        else:
            consume.close()
            break


def producer(p, n):
    produce, consume = p
    consume.close()
    for i in range(n):
        produce.send(i)
    produce.send(None)
    produce.send(None)
    produce.close()


if __name__ == '__main__':
    produce, consume = Pipe()
    lock = Lock()
    c1 = Process(target=consumer, args=((produce, consume), 'c1', lock))
    c2 = Process(target=consumer, args=((produce, consume), 'c2', lock))
    p1 = Process(target=producer, args=((produce, consume), 100))
    c1.start()
    c2.start()
    p1.start()

    produce.close()
    consume.close()

    c1.join()
    c2.join()
    p1.join()
    print('主进程')
