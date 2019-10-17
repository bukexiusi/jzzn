# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/12 10:51
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 多进程_管道通信cmd实时输出.py
@Description :
'''

from multiprocessing import Pipe, Process, Value
import shlex
import subprocess
import codecs
import locale
from tkinter import *
import time
import sys


def func(conn1, conn2):
    conn2.close()

    def counter():
        try:
            output = conn1.recv()
            lb.insert(END, output)
            print(output)
            lb.after(1, counter)
        except EOFError as e:
            return

    root = Tk()
    sb = Scrollbar(root)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(root, yscrollcommand=sb.set)
    lb.pack(side=RIGHT)
    counter()
    sb.config(command=lb.yview)
    mainloop()


if __name__ == '__main__':
    conn1, conn2 = Pipe(duplex=False)  # 建立一个管道,管道返回两个connection
    Process(target=func, args=(conn1, conn2)).start()
    conn1.close()

    shell_cmd = "python test.py"
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    conn2.send("PID-DATA:{}".format(str(p.pid)))
    '''编码的选择，应该选取stdout中的编码，第三种方式得到'''
    # decode_str = 'utf-8'
    # decode_str = codecs.lookup(locale.getpreferredencoding()).name
    decode_str = sys.stdout.encoding
    stdout_ = p.stdout
    while True:
        data = stdout_.readline().strip()
        if data:
            content = data.decode(decode_str)
            conn2.send(content)
            if content == "翊通执行完毕":
                break
    print("结束")
    conn2.close()
