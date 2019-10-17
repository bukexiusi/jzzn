# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/6 20:10
@Author  : 图南
@Email   : 935281275@qq.com
@File    : subprocess_demo.py
@Description :
'''


import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print('hello world')")
obj.stdin.write("\n")
obj.stdin.write("print('hello python')\n")
obj.stdin.write("print(1+3)")
content = '''
print(1)
print(2)
print(3)
'''
obj.stdin.write(content)
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)  # 程序没有异常，只输出空行
