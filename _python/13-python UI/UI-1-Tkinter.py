# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 17:10
@Author  : 图南
@Email   : 935281275@qq.com
@File    : UI-1-Tkinter.py
@Description :
'''

from tkinter import *


def onGo():
    def counter(i):
        if i > 0:
            t.insert(END, 'a_' + str(i))
            t.after(1000, counter, i - 1)
        else:
            goBtn.config(state=NORMAL)

    goBtn.config(state=DISABLED)
    counter(50)


root = Tk()
t = Text(root)
t.pack()
goBtn = Button(text="Go!", command=onGo)
goBtn.pack()
root.mainloop()
