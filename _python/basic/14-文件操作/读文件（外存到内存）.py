# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/20 15:26
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 读文件（外存到内存）.py
@Description :
'''


def m1():
    with open("test.txt", 'r') as f:
        line = f.readline()[:-1]
        while line:
            print(line)
            line = f.readline()[:-1]


def m2():
    for line in open("test.txt", "r"):
        print(line[:-1])


def m3():
    with open("test.txt", 'r') as f:
        print(f.readlines())


if __name__ == "__main__":
    m3()
