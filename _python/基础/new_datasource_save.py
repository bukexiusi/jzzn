# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/15 9:34
@Author  : 图南
@Email   : 935281275@qq.com
@File    : new_datasource_save.py
@Description :
'''

import requests
import json


def save(row_data, field_data):
    '''
    保存至数据库
    :param row_data: 取自execute_data()方法
    :param field_data:    {
                        "执行时长": 60,
                        "结案日期": "2019-06-03"
                     }
    :return:
    '''
    if isinstance(row_data, dict):
        row_data = [row_data]
    if not isinstance(row_data, list):
        raise Exception("好好学习sdk，天天向上")

    if isinstance(field_data, dict):
        field_data = [field_data]
    if not isinstance(field_data, list):
        raise Exception("好好学习sdk，天天向上")

    if len(row_data) != len(field_data) or len(row_data) == 0:
        raise Exception("好好学习sdk，天天向上")

    resp = requests.post(
        "http://{}:{}/table/data/save/data".format("localhost", "8000"),
        json={"row_data": row_data, "field_data": field_data},
        timeout=10)

    if not resp:
        raise Exception("网络原因，获取数据失败")

    result = json.loads(resp.text)
    return result


def a():
    row_datas = [{'id': 135997134292912133, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7784号', '创建者': 'admin',
                  '创建时间': 1565940121761, '更新者': '', '更新时间': 1565940728475.0, '执行说明': '执行成功', '执行时间': '', '执行时长': '',
                  '批次': 1565940121},
                 {'id': 135997134292912134, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7785号', '创建者': 'admin',
                  '创建时间': 1565940121761, '更新者': '', '更新时间': '', '执行说明': '', '执行时间': '', '执行时长': '', '批次': 1565940121},
                 {'id': 135997134292912135, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7786号', '创建者': 'admin',
                  '创建时间': 1565940121761, '更新者': '', '更新时间': '', '执行说明': '', '执行时间': '', '执行时长': '', '批次': 1565940121},
                 {'id': 135997134301300743, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7787号', '创建者': 'admin',
                  '创建时间': 1565940121762, '更新者': '', '更新时间': 1565940728855.0, '执行说明': '执行成功', '执行时间': '', '执行时长': '',
                  '批次': 1565940121},
                 {'id': 135997134301300744, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7788号', '创建者': 'admin',
                  '创建时间': 1565940121762, '更新者': '', '更新时间': '', '执行说明': '', '执行时间': '', '执行时长': '', '批次': 1565940121},
                 {'id': 135997134301300745, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7789号', '创建者': 'admin',
                  '创建时间': 1565940121762, '更新者': '', '更新时间': 1565940729105.0, '执行说明': '执行成功', '执行时间': '', '执行时长': '',
                  '批次': 1565940121},
                 {'id': 135997134301300746, '数据表名': 'zn_business_table_24', '案号': '(2019)闽0203执7790号', '创建者': 'admin',
                  '创建时间': 1565940121762, '更新者': '', '更新时间': '', '执行说明': '', '执行时间': '', '执行时长': '', '批次': 1565940121}]
    field_data = {"执行说明": "执行成功"}
    for row_data in row_datas:
        save(row_data, field_data)


def b():
    row_data = [{"数据表名": "zn_business_table_26"}]
    field_data = [{"案号": "123123", "车辆信息": "zn测试", "pid": 138748673155663879, "数据表名": "zn_business_table_28"}]
    print(save(row_data, field_data))


def c():
    row_data = [
        {"数据表名": "zn_business_table_26", "id": 138748673155663879},
        {"数据表名": "zn_business_table_26", "id": 138748673155663879, "数据子表名": "测试从表2"}
    ]
    field_data = [
        {"执行说明": "执行成功"},
        {"案号": "123123"}
    ]
    print(save(row_data, field_data))


def d():
    row_data = {"id": 139716143488174086, "数据表名": "测试从表2"}
    field_data = {"案号": "34567"}
    print(save(row_data, field_data))


if __name__ == "__main__":
    print(14,593,279*7)
