# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/16 19:43
@Author  : 图南
@Email   : 935281275@qq.com
@File    : gui.py
@Description :
'''

import wx

app = wx.App()
frame = wx.Frame(None, title="Gui Test Editor", pos=(1000, 200), size=(500, 400))

path_text = wx.TextCtrl(frame, pos=(5, 5), size=(350, 24))
open_button = wx.Button(frame, label="打开", pos=(370, 5), size=(50, 24))
save_button = wx.Button(frame, label="保存", pos=(430, 5), size=(50, 24))
