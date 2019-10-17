# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/1 10:50
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 创建excel.py
@Description :
'''
import os
import pandas

file_name = 'F:\_python\project\demo\excel相关/%s-%s.%s' % ("数据", "1", "xlsx")
if not os.path.exists("F:\_python\project\demo\excel相关"):
    os.makedirs("F:\_python\project\demo\excel相关")
if not os.path.exists(file_name):
    df1 = pandas.DataFrame()
    df1.to_excel(file_name, index=False)
