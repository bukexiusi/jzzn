# -*- coding: utf-8 -*-
'''
@Time    : 2019/10/17 10:32
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数据权限.py
@Description :
'''

import pymysql
import pandas


auth_interface_en_cn = {
    "com.yidao.clever.idao.SysOrgDetailMapper.list": "机构列表",
    "com.yidao.clever.idao.SysDeptMapper.listOrderByLvl": "部门树",
    "com.yidao.clever.idao.SysUserMapper.list": "用户列表",
    "com.yidao.clever.idao.CsOrgAuthorMapper.list": "机构权限列表",
    "com.yidao.clever.idao.CsClientAuthorMapper.list": "客户端权限列表",
    "com.yidao.clever.idao.CsAppMapper.list": "应用列表",
    "com.yidao.clever.idao.SysRoleMapper.list": "角色列表"
}


def get_db_data():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='cs_siming',
        charset='utf8'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cursor.execute('select * from sys_role_data_authority')
        result = cursor.fetchall()
        print(result)
        return result
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    db_data = get_db_data()
