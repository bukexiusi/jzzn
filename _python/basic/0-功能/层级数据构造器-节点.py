# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/28 17:32
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 层级数据构造器.py
@Description :
'''

'''
{
    "menu_name": "",
    "menu_path": "",
    "type": ""
}
'''

from 雪花算法 import get_snow_id
from functools import reduce
import copy

menu_data = [
    {
        "menu_name": "工作台",
        "menu_path": "",
        "type": "MENU",
    }, {
        "menu_name": "案件列表",
        "menu_path": "",
        "type": "CATA",
        "children": [
            {
                "menu_name": "全部案件",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "我的案件",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "待接收",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "待我审批",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "我已审批",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "我催办的",
                "menu_path": "",
                "type": "MENU",
            }
        ]
    }, {
        "menu_name": "效能管理",
        "menu_path": "",
        "type": "CATA",
        "children": [
            {
                "menu_name": "节点配置",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "消息中心",
                "menu_path": "",
                "type": "MENU",
            }
        ]
    }, {
        "menu_name": "系统设置",
        "menu_path": "",
        "type": "CATA",
        "children": [
            {
                "menu_name": "组织管理",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "角色管理",
                "menu_path": "",
                "type": "MENU",
            }, {
                "menu_name": "标签管理",
                "menu_path": "",
                "type": "MENU",
            }
        ]
    }
]


def recursive(inputs, export, **kw):
    '''
    递归构造层级数据
    :param inputs:
    :param export:
    :param kw:
    :return:
    '''
    for i, inp in enumerate(inputs):
        temp = dict((key, value) for key, value in inp.items() if not isinstance(value, list))
        temp["id"] = get_snow_id()
        if kw.get("order_mode"):
            temp["order_num"] = i

        ancestor_id = kw.get("ancestor_id")
        if kw.get("ancestor_mode"):
            temp["ancestor_id"] = ancestor_id

        layer = 0 if kw.get("layer") is None else kw.get("layer")
        if layer == 0:
            ancestor_id = "%s-" % temp.get("id")
        else:
            ancestor_id = "%s%s-" % (kw.get("ancestor_id"), temp.get("id"))

        if isinstance(layer, int):
            if kw.get("layer_mode"):
                temp["layer"] = layer
            layer += 1
        export.append(temp)
        if inp.get("children"):
            kww = {
                "layer_mode": kw.get("layer_mode"),
                "layer": layer,
                "ancestor_mode": kw.get("ancestor_mode"),
                "ancestor_id": ancestor_id,
                "order_mode": kw.get("order_mode")
            }
            recursive(
                inp.get("children"),
                export,
                layer_mode=kw.get("layer_mode"),
                layer=layer,
                ancestor_mode=kw.get("ancestor_mode"),
                ancestor_id=ancestor_id,
                order_mode=kw.get("order_mode")
            )
    return export


def list2sql(table_name, array):
    '''
    列表转sql
    :param table_name:
    :param array:
    :return:
    '''
    result = []
    for element in array:
        columns = []
        values = []
        for key, val in element.items():
            columns.append("`%s`" % key)
            if val is None:
                values.append("%s" % "null")
            elif isinstance(val, str):
                values.append("'%s'" % val)
            else:
                values.append("%s" % val)
        columns_str = "(%s)" % ','.join(columns)
        values_str = "(%s);" % ','.join(values)
        sql = "insert into %s %s values %s" % (table_name, columns_str, values_str)
        result.append(sql)
    return result





if __name__ == "__main__":
    # 清空语句
    print("truncate table sys_role;")
    print("truncate table sys_role_menu;")
    print("truncate table sys_menu;")
    # 菜单列表
    menu = []
    recursive(menu_data, menu, layer_mode=True, ancestor_mode=True, order_mode=True)
    # 菜单层级
    menu_array = list2sql("sys_menu", menu)
    for ma in menu_array:
        print(ma)

