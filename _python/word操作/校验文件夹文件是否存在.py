import os, re
from word操作.word操作类 import *
print(os.path.exists("D:\\案件模板\\"))
print(os.path.exists("D:\\案件模板\\文件一.py"))

file_name = "D:\\案件模板\\ddd\\dddd.fff\\文件一.py"
print(re.findall(r"(.*)\\", file_name))

word = RemoteWord("D:\\案件模板\\模版一.docx")
word.close()