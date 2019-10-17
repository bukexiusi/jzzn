# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/30 21:01
@Author  : 图南
@Email   : 935281275@qq.com
@File    : datetime.py
@Description :
'''

import datetime

# datetime.datetime类型
now = datetime.datetime.now()
print(now)
print(type(now))

# 时间戳
print(now.timestamp())

# str -> datetime.datetime
cday = datetime.datetime.strptime('2019-7-30 21:05:11', '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))

# datetime.datetime -> str
print(now.strftime('%Y-%m-%d %H:%M:%S'))

# 日期加减
print(now + datetime.timedelta(days=1))
print(now + datetime.timedelta(hours=1))
print(now + datetime.timedelta(days=1, hours=1))


