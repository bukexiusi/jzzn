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
        "menu_name": "首页",
        "menu_path": "/home",
        "icon": "bank",
        "type": "MENU",
    },
    {
        "menu_name": "组织管理",
        "menu_path": "",
        "icon": "usergroup-delete",
        "type": "CATA",
        "children": [
            {
                "menu_name": "机构管理",
                "menu_path": "/company",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "导出数据",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "添加机构",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "删除机构",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "编辑机构",
                        "menu_path": "",
                        "type": "BTN"
                    }
                ]
            }, {
                "menu_name": "部门管理",
                "menu_path": "/user",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "新建同级部门",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "新建下级部门",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "编辑部门",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "删除部门",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "添加用户",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "删除用户",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "编辑用户",
                        "menu_path": "",
                        "type": "BTN",
                    }
                ]
            }
        ]
    }, {
        "menu_name": "授权管理",
        "menu_path": "",
        "icon": "unordered-list",
        "type": "CATA",
        "children": [
            {
                "menu_name": "机构授权",
                "menu_path": "/license",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "生成授权",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "更新授权",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "审批授权",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "查看记录",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "编辑授权",
                        "menu_path": "",
                        "type": "BTN",
                    }
                ]
            }, {
                "menu_name": "用户授权",
                "menu_path": "/authority",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "生成激活码",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "导出列表",
                        "menu_path": "",
                        "type": "BTN",
                    }, {
                        "menu_name": "修改计算机备注",
                        "menu_path": "",
                        "type": "BTN",
                    }
                ]
            }
        ]
    }, {
        "menu_name": "应用管理",
        "menu_path": "",
        "type": "CATA",
        "icon": "setting",
        "children": [{
            "menu_name": "应用列表",
            "menu_path": "/appList",
            "type": "MENU",
            "children": [
                {
                    "menu_name": "应用授权",
                    "menu_path": "",
                    "type": "BTN",
                }
            ]
        }, ]
    }, {
        "menu_name": "系统管理",
        "menu_path": "",
        "type": "CATA",
        "icon": "setting",
        "children": [
            {
                "menu_name": "字典管理",
                "menu_path": "/dictionary",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "新增字典",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "删除字典",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "编辑字典",
                        "menu_path": "",
                        "type": "BTN"
                    }
                ]
            }, {
                "menu_name": "通知设置",
                "menu_path": "/notice",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "添加通知",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "删除通知",
                        "menu_path": "",
                        "type": "BTN"
                    }, {
                        "menu_name": "编辑通知",
                        "menu_path": "",
                        "type": "BTN"
                    }
                ]
            }
        ]
    }, {
        "menu_name": "报表统计",
        "menu_path": "",
        "type": "CATA",
        "icon": "line-chart",
        "children": [
            {
                "menu_name": "数据报表",
                "menu_path": "/chart",
                "type": "MENU",
                "children": [
                    {
                        "menu_name": "导出数据",
                        "menu_path": "",
                        "type": "BTN",
                    }
                ]
            }, {
                "menu_name": "日志报表",
                "menu_path": "/log",
                "type": "MENU",
            }
        ]
    }
]

role_data = [
    {
        "id": "1",
        "role_code": "ORG",
        "data_code": "ORG",
        "role_name": "机构管理员",
        "creator": "zn",
        "create_time": 1,
        "updator": "zn",
        "update_time": 1,
        "delete": 0,
    }, {
        "id": "2",
        "role_code": "DEPT",
        "data_code": "DEPT",
        "role_name": "部门管理员",
        "creator": "zn",
        "create_time": 1,
        "updator": "zn",
        "update_time": 1,
        "delete": 0,
    }, {
        "id": "3",
        "role_code": "USER",
        "data_code": "USER",
        "role_name": "普通用户",
        "creator": "zn",
        "create_time": 1,
        "updator": "zn",
        "update_time": 1,
        "delete": 0,
    }, {
        "id": "4",
        "role_code": "IMPL",
        "data_code": "IMPL",
        "role_name": "实施人员",
        "creator": "zn",
        "create_time": 1,
        "updator": "zn",
        "update_time": 1,
        "delete": 0,
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
        if not temp.get("id"):
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


def getMenuList():
    result = []
    valid_array = copy.copy(menu_data)
    while True:
        temp_array = []
        for md in valid_array:
            result.append(md.get("menu_name"))
            children = md.get("children")
            if children:
                temp_array.extend(children)

        if not temp_array:
            break
        valid_array = copy.copy(temp_array)
    print(result)


# 机构管理员菜单
role_menu_ORG = [
                '首页',
                '组织管理',
                    '机构管理',
                        '查看机构',
                    '部门管理',
                        '新建同级部门', '新建下级部门', '编辑部门', '删除部门', '添加用户', '删除用户', '编辑用户', '启用',
                '授权管理',
                    '机构授权',
                        '更新授权',
                    '用户授权',
                        '生成激活码', '导出激活码', '修改计算机备注',
                '应用管理',
                    '应用列表',
                        '应用授权',
                '系统管理',
                    '字典管理',
                        '添加字典', '删除字典', '编辑字典',
                '报表统计',
                    '数据报表',
                        '导出数据',
                    '日志报表',
                        '导出日志'
                ]

# 部门管理员菜单
role_menu_DEPT = [
                '首页',
                '组织管理',
                    '部门管理',
                '应用管理',
                '报表统计',
                    '数据报表',
                        '导出数据',
                    '日志报表',
                        '导出日志'
                ]
# 普通用户菜单
role_menu_USER = [
                '首页',
                '报表统计',
                    '数据报表',
                        '导出数据',
                    '日志报表'
                ]
# 实施人员菜单
role_menu_IMPL = [
                '首页',
                '组织管理',
                    '机构管理',
                        '导出机构', '添加机构', '删除机构', '编辑机构', '查看机构',
                    '部门管理',
                        '新建同级部门', '新建下级部门', '编辑部门', '删除部门', '添加用户', '删除用户', '编辑用户', '启用',
                '授权管理',
                    '机构授权',
                        '更新授权',
                '应用管理',
                    '应用列表',
                        '应用授权',
                '系统管理',
                    '字典管理',
                        '添加字典', '删除字典', '编辑字典',
                '报表统计',
                    '数据报表',
                        '导出数据',
                    '日志报表',
                        '导出日志'
                ]


def role_menu_mapping(array, menu, role, role_code):
    result = []
    list_map_role = list(map(lambda x: [x.get("role_code"), x.get("id")], role))
    role_dealt = dict(list_map_role)
    role_id = role_dealt.get(role_code)
    list_map_menu = list(map(lambda x: [x.get("menu_name"), x.get("id")], menu))
    menu_dealt = dict(list_map_menu)
    for element in array:
        snow_id = get_snow_id()
        menu_id = menu_dealt.get(element)
        sql = "insert into sys_role_menu (`id`, `role_id`, `menu_id`) values ('%s', '%s', '%s');" % (
            snow_id, role_id, menu_id)
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

    # 角色列表
    role = []
    recursive(role_data, role)
    # 角色层级
    role_array = list2sql("sys_role", role)
    for ra in role_array:
        print(ra)

    # 角色菜单绑定
    ORG_array = role_menu_mapping(role_menu_ORG, menu, role, 'ORG')
    for a in ORG_array:
        print(a)
    DEPT_array = role_menu_mapping(role_menu_DEPT, menu, role, 'DEPT')
    for a in DEPT_array:
        print(a)
    USER_array = role_menu_mapping(role_menu_USER, menu, role, 'USER')
    for a in USER_array:
        print(a)
    IMPL_array = role_menu_mapping(role_menu_IMPL, menu, role, 'IMPL')
    for a in IMPL_array:
        print(a)

    getMenuList()
