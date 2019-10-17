# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/16 17:40
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 鼠标点击坐标.py
@Description :
'''

from ctypes import Structure, windll, POINTER, pointer
from ctypes.wintypes import WORD
import win32api
import win32gui

class SYSTEMTIME(Structure):
    _fields_ = [("wYear", WORD), ("wMonth", WORD), ("wDayOfWeek", WORD), ("wDay", WORD),
                ("wHour", WORD), ("wMinute", WORD), ("wSecond", WORD),
                ("wMilliseconds", WORD), ]


def printlocaltime():  # decl
    GetLocalTime = windll.kernel32.GetLocalTime
    GetLocalTime.argtypes = [POINTER(SYSTEMTIME), ]
    # invoke
    t = SYSTEMTIME()
    GetLocalTime(pointer(t))
    print("%04d-%02d-%02d %02d:%02d:%02d" % (t.wYear, t.wMonth, t.wDay, t.wHour, t.wMinute, t.wSecond))


if __name__ == "__main__":
    printlocaltime()
    print(win32gui.GetActiveWindow())
    print(win32gui.GetFocus())
    print(win32api)


