# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/29 11:00
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 字典_一行过滤字典组成新字典.py
@Description :
'''

i = {
    "str": "str",
    "list": []
}
temp = dict((key, value) for key, value in i.items() if isinstance(value, str))