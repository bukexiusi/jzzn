# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 11:48
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-数组中字典去重.py
@Description :
'''

# 循环取字典中某值组成新数组
aa = [
    {"id": 1, "name": "张三"},
    {"id": 2, "name": "李四"},
    {"id": 3, "name": "王五"}
]
bb = list(map(lambda x: x.get("name"), aa))
print(bb)
