# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/16 10:10
@Author  : 图南
@Email   : 935281275@qq.com
@File    : client.py
@Description :
'''

import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
print(c.hello("RPC"))

