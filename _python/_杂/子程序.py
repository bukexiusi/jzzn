# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/5 17:13
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 子程序.py
@Description :
'''
import shlex
import subprocess
import timeit


def a():
    shell_cmd = "python demo.py"
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout_ = p.stdout
    while True:
        data = stdout_.readline().strip()
        if p.poll() is not None:
            break
        if data:
            content = data.decode('gb18030')
            print(content)
    p.kill()
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')


def b():
    shell_cmd = "python demo.py"
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        data = p.stdout.readline().strip()
        if not data:
            break
        content = data.decode('gb18030')
        # print(content)
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')


if __name__ == "__main__":
    a()
    # print(min(timeit.repeat(lambda: a(), number=1, repeat=20)))
    # print(min(timeit.repeat(lambda: b(), number=1, repeat=20)))
