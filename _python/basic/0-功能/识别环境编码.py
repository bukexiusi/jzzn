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
print('中文')

bb = b'0xb3'
# bb = b'\xe4\xb8\xad\xe6\x96\x87'

print(bb.decode("utf-8", errors='strict'))
