# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 11:40
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 数组(列表)-zip.py
@Description :
'''

a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
c = zip(a, b)
print(type(c))
print(c)

'''zip后，以下三句只能执行一句，暂时理解为只能进行一次list操作'''
# print(list(c))

# for c_e in c:
#     print(c_e)

# for a_e, b_e in c:
#     print(a_e)
#     print(b_e)
