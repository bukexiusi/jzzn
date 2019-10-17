# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 18:33
@Author  : 图南
@Email   : 935281275@qq.com
@File    : aaa.py
@Description :
'''

from tkinter import *


def counter(i):
    if i > 0:
        lb.insert(END, "%s\n" % str(i))
        lb.after(100, counter, i - 1)


root = Tk()
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
lb = Listbox(root, yscrollcommand=sb.set)
lb.pack(side=RIGHT)
counter(50)
sb.config(command=lb.yview)
mainloop()
