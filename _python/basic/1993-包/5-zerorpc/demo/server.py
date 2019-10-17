# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/16 10:04
@Author  : 图南
@Email   : 935281275@qq.com
@File    : demo.py
@Description :
'''

import zerorpc
import threading as td
import multiprocessing as mp

def aa(a):
    with open("1.txt", 'a') as f:
        for i in range(1000000):
            f.write(str(i))

class HelloRPC(object):

    def hello(self, name):
        print("请求成功")
        # mp.Process(target=aa, args=(0,)).start()
        td.Thread(target=aa, args=(0,)).start()
        return "Hello, %s" % name


if __name__ == "__main__":
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()

