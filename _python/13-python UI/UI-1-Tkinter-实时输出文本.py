# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 18:15
@Author  : 图南
@Email   : 935281275@qq.com
@File    : UI-1-Tkinter-实时输出文本.py
@Description :
'''

from tkinter import *


def counter(i):
    if i > 0:
        t.insert(END, "%s\n" % str(i))
        t.after(100, counter, i - 1)


if __name__ == "__main__":
    root = Tk()
    root.title("图南")
    t = Text(root)
    t.pack()
    scroll = Scrollbar()
    scroll.pack(side=RIGHT, fill=Y)      # side是滚动条放置的位置，上下左右。
    scroll.config(command=t.yview)       # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    t.config(yscrollcommand=scroll.set)  # 将滚动条关联到文本框
    counter(50)
    root.mainloop()
