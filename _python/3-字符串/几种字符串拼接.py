# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/3 23:01
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 几种字符串替换(拼接)及其性能比较.py
@Description :
'''

import timeit


def add():
    status = 200
    body = 'hello world'
    return 'Status: ' + str(status) + '\r\n' + body + '\r\n'


def old_style():
    status = 200
    body = 'hello world'
    return 'Status: %s\r\n%s\r\n' % (status, body)


def formatter1():
    status = 200
    body = 'hello world'
    return 'Status: {}\r\n{}\r\n'.format(status, body)


def formatter2():
    status = 200
    body = 'hello world'
    return 'Status: {status}\r\n{body}\r\n'.format(status=status, body=body)


def f_string():
    '''3.6后支持，推荐，最快'''
    status = 200
    body = 'hello world'
    return f'Status: {status}\r\n{body}\r\n'


print("start")
perf_dict = {
    'add': min(timeit.repeat(lambda: add())),
    'old_style': min(timeit.repeat(lambda: old_style())),
    'formatter1': min(timeit.repeat(lambda: formatter1())),
    'formatter2': min(timeit.repeat(lambda: formatter2())),
    'f_string': min(timeit.repeat(lambda: f_string()))
}
print(perf_dict)
print("end")
