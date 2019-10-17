# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/4 11:07
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 生成器.py
@Description :
'''

aa = [i for i in range(1, 10)]  # 注意区别
bb = (i for i in range(1, 10))  # 将列表生成试外部的中括号改为小括号，就能将生成式转化为生成器。
next(bb), bb.__next__()         # 生成器的取值方式只能使用next的方法。


def num():
    a, b = 0, 1
    for i in range(10):
        yield b  # 生成关键字yield，有yield的关键字的代码块就是yield的生成器。当运行到yield时代码就会停止，并返回运行结果，当在次运行时依旧是到yield停止，并返回结果。 切记：生成器只能使用next方法。
        a, b = b, a + b
        temp = yield b  # 这里并不是变量的定义，当运行到yield时就会停止，所以当运行到等号右边的时候就会停止运行，当在次使用next的时候，将会把一个None赋值给temp，因为b的值已经在上轮循环中输出。这里可以使用num().send()方法将一个新的值赋值给temp。

'''
注意点一：生成器，yeild代表结束执行，第二次在第一次结束的地方开始执行，第三次执行在第二次结束的地方开始执行
注意点二：调用生成器的方法有两种，如下
第一次      
第二次
第三次
第四次
第五次
第六次
第七次
第八次
第九次
第十次 
'''


# 调用生成器方法一
a = num()
for n in a:
    print(n)

# 调用生成器方法二
b = num()
for m in range(10):
    print(next(b))

c = num()
for l in range(100):
    print(next(c))


