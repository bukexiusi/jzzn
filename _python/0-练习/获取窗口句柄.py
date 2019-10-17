# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/16 18:04
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 获取窗口句柄.py
@Description :
'''

import win32gui
import win32api

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)

