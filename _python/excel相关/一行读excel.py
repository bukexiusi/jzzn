# -*- coding: utf-8 -*-
'''
@Time    : 2019/6/26 18:33
@Author  : 图南
@Email   : 935281275@qq.com
@File    : demo.py
@Description :
'''

import pandas

# 读数据(excel -> dict)
excel = pandas.read_excel("D:\\数据表-表结构.xlsx", sheet_name=2)
dictionary = excel.to_dict(orient='records')
print(dictionary)
print("----------------------------------------------------------------------------------------------------------------")

# 存数据(list -> excel)
df1 = pandas.DataFrame(columns=["案号", "年份", "执字", "序号", "天才"])
df1.to_excel("output.xlsx", index=False)
# excel = pandas.read_excel("output.xlsx")
# dictionary = excel.to_dict(orient='records')
# print(dictionary)

# 生成多分sheet
with pandas.ExcelWriter('output2.xlsx') as writer:
    df1 = pandas.DataFrame(columns=["案号", "年份", "执字", "序号", "天才"])
    df1.to_excel(writer, sheet_name='Sheet_name_1', index=False)
    df2 = pandas.DataFrame(columns=["案号", "年份", "执字", "序号", "天才2"])
    df2.to_excel(writer, sheet_name='Sheet_name_2', index=False)

# 将Excel文件读取成 ExcelFile 格式
xls = pandas.ExcelFile("D:\\数据表-表结构.xlsx")
exchanges = xls.sheet_names
for exchange in exchanges:
    sheet = pandas.read_excel(xls, sheet_name=exchange)
    column_heads = sheet.columns.values.tolist()  # 获取列名
    dictionary = sheet.to_dict(orient='records')
    print(dictionary)
