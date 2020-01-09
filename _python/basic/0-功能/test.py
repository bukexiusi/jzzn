# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/11 15:17
@Author  : 图南
@Email   : 935281275@qq.com
@File    : test.py
@Description :
'''

<<<<<<< HEAD
print(16384/14)
print(1170*1170*16)
=======
import time

try:
    import dbddd

    print(1)
except:
    print(2)
print(33 * 32 * 31 * 30 * 29 * 28 / 1 / 2 / 3 / 4 / 5 / 6 * 16)
print("翊通执行完毕")

test1 = '2019-8-01'


def time_data1(time_sj):  # 传入单个时间比如'2019-8-01 00:00:00'，类型为str
    data_sj = time.strptime(time_sj, "%Y-%m-%d")  # 定义格式
    time_int = int(time.mktime(data_sj))
    return time_int  # 返回传入时间的时间戳，类型为int


print(time_data1('2020-1-1'))
print(time_data1('2020-1-2'))
print(time_data1('2020-1-3'))
print(time_data1('2020-1-4'))
print(time_data1('2020-1-5'))
print(time_data1('2020-1-6'))

print((time_data1('2020-1-6') - time_data1('2020-1-5'))/24/60/60)


for j in range(1, 6):
    print(j)
>>>>>>> 54705801f52218b236f11a92d403d20145391d07
