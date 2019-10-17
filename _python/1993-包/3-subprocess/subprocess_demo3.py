# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/7 12:09
@Author  : 图南
@Email   : 935281275@qq.com
@File    : subprocess_demo3.py
@Description :
'''
import subprocess
import locale
import codecs
import time
import threading


def popen1(cmd):
    try:
        popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        popen.wait()
        lines = popen.stdout.readlines()
        result = [line.decode('gbk') for line in lines]
        print(result)
        return result
    except BaseException as e:
        return -1


def popen2(cmd):
    try:
        popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = popen.communicate()
        for line in out.splitlines():
            print(line)
    except BaseException as e:
        return -1


def popen3(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        p.stdout.flush()
        line = p.stdout.readline().strip()
        if line:
            # content = line.decode(codecs.lookup(locale.getpreferredencoding()).name)
            content = line.decode('gb18030')
            print(content)
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')


alist = []


def getstdout(p, asy):
    while True:
        data = p.stdout.readline()
        if data == b'':
            if p.poll() is not None:
                break
        else:
            print(data.decode(codecs.lookup(locale.getpreferredencoding()).name))

# 2019-9-6更新
def getstdout_2(p, asy):
    code_name = codecs.lookup(locale.getpreferredencoding()).name
    while True:
        p.stdout.flush()
        data = p.stdout.readline().strip()
        if p.poll() is not None:
            break
        if data:
            print(data.decode(code_name))


def popen4(cmd):
    ps = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    resultlist = getstdout(ps, False)


if __name__ == "__main__":
    popen4("python ./demo.py")

    # 在Linux系统下，必须加入sys.stdout.flush()
    # 才能一秒输一个数字
    #
    # 在Windows系统下，加不加sys.stdout.flush()
    # 都能一秒输出一个数字
