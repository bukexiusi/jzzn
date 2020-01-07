# -*- coding: utf-8 -*-
'''
@Time    : 2019/10/17 10:25
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 操作数据库.py
@Description :
'''

import pymysql
import random


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='node-management-test',
    charset='utf8'
)

node_name_array = ['', '收案', '查控', '送达通知书', '签发审批表', '送达文书']
status_array = [0, 1, 2, 4, 8, 16]
receipt_time_array = [1577808000, 1577894400, 1577980800, 1578067200, 1578153600, 1578240000]
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

try:
    # 定义要执行的sql语句
    sql1 = 'insert into nm_case(ID, CASE_NUM, `DELETE`) values(%s, %s, 0);'
    sql2 = 'insert into nm_case_node(ID, CASE_ID, NODE_ID, NODE_NAME, RECEIPT_TIME, STATUS, NODE_TIME_LIMIT, `DELETE`) values(%s, %s, %s, %s, %s, %s, 24*60*60*1000*3, 0);'
    case_data = []
    case_node_data = []
    for i in range(1, 10000):
        tuple_ = (i, '(2020)闽0203执%s号' % str(i))
        case_data.append(tuple_)
        for j in range(1, 6):
            random_num = random.randint(0, 5)
            tuple__ = (6*i+j, i, j, node_name_array[j], receipt_time_array[random_num], status_array[j])
            case_node_data.append(tuple__)
    # 拼接并执行sql语句
    cursor.executemany(sql1, case_data)
    cursor.executemany(sql2, case_node_data)
    # 涉及写操作要注意提交
    conn.commit()
except Exception as e:
    print(e)
finally:
    # 关闭连接
    cursor.close()
    conn.close()
