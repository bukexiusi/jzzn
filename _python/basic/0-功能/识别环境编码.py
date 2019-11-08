# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/12 10:37
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 识别环境编码.py
@Description :
'''

import sys

print(sys.getdefaultencoding())
print(sys.stdout.encoding)
print('仙剑奇侠传'.encode("gbk"))
print(b"\xcf\xc9\xbd\xa3\xc6\xe6\xcf\xc0\xb4\xab".decode("gbk"))

bb = b'0xb3'
# bb = b'\xe4\xb8\xad\xe6\x96\x87'

print(bb.decode("utf-8", errors='strict'))

ue = "翊通rpa执行开始".encode('unicode_escape').decode("utf-8")
print(ue)

