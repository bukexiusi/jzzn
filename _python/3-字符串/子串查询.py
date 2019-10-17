# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/3 23:27
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 子串查询.py
@Description :
'''

import timeit


def in_(s, other):
    '''最佳推荐'''
    return other in s


def contains(s, other):
    return s.__contains__(other)


def find(s, other):
    return s.find(other) != -1


def index(s, other):
    try:
        s.index(other)
    except ValueError:
        return False
    return True


perf_dict = {
    'in:True': min(timeit.repeat(lambda: in_('superstring', 'str'))),
    'in:False': min(timeit.repeat(lambda: in_('superstring', 'not'))),
    '__contains__:True': min(timeit.repeat(lambda: contains('superstring', 'str'))),
    '__contains__:False': min(timeit.repeat(lambda: contains('superstring', 'not'))),
    'find:True': min(timeit.repeat(lambda: find('superstring', 'str'))),
    'find:False': min(timeit.repeat(lambda: find('superstring', 'not'))),
    'index:True': min(timeit.repeat(lambda: index('superstring', 'str'))),
    'index:False': min(timeit.repeat(lambda: index('superstring', 'not'))),
}
print(perf_dict)
