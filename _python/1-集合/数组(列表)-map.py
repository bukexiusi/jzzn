'''
@Time    : 2019/7/28 11:40
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-zip.py
@Description :
'''

a = [1, 2, 3]
c = list(map(lambda x: x * 10, a))
print(c)

a = [1, 2, 3]
b = [4, 5, 6]
c = list(map(lambda x, y: x * 10 + y, a, b))
print(c)

#  若a和b长度不一致，取最短
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = list(map(lambda x, y: x * 10 + y, a, b))
print(c)

# 循环取字典中某值组成新数组
aa = [
    {"id": 1, "name": "张三"},
    {"id": 2, "name": "李四"},
    {"id": 3, "name": "王五"}
]
aa1 = [
    {"id": 1, "name": "张三"},
    {"id": 2, "name": "李四"},
    {"id": 3, "name": "王五"}
]
bb = list(map(lambda x: x.get("name"), aa))
print(bb)

bb1 = list(map(lambda x, y: x.get("name") + y.get("name"), aa, aa1))
print(bb1)

row_data = [{"数据表名": "zn_business_table_0", "id": 1}, {"数据表名": "zn_business_table_0"}]
field_data = [{"执行说明": "执行成功"}, {"执行说明": "执行失败"}]
dealt = list(map(lambda x, y: []+x if x.get("id") else 0, row_data, field_data))
print(dealt)

