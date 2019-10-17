# -*- coding: utf-8 -*-
'''
@Time    : 2019/7/28 10:55
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 打印十万内素数.py
@Description :
'''

result = []
for i in range(2, 100001):
    is_prime = True
    for j in range(2, i):
        if j * j > i:
            break
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result.append(i)

print(result)
print(len(result))
