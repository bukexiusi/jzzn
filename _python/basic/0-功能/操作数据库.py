# -*- coding: utf-8 -*-
'''
@Time    : 2019/10/17 10:25
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 操作数据库.py
@Description :
'''

import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='930210',
    db='clever-spiders-local',
    charset='utf8'
)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典类型数据
try:
    cursor.execute('select * from sys_role_data_authority')
    result = cursor.fetchall()
    print(result)
finally:
    cursor.close()
    conn.close()
