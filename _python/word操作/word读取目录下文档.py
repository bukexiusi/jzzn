import os
from word操作.word操作类 import *

input_path = "D:\\案件模板" # 文件夹目录
output_path = "D:\\生成文档"
files= os.listdir(input_path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     print(file)
print(s) #打印结果

print("------------------------------------------我是分界线------------------------------------------")

for root, dirs, files in os.walk(input_path):
    print("-------------------------------------------------")
    print(root) #当前目录路径
    print(dirs) #当前路径下所有子目录
    print(files) #当前路径下所有非目录子文件
    print("-------------------------------------------------")

print("------------------------------------------我是分界线------------------------------------------")

all_file_path = []
for root, dirs, files in os.walk(input_path):
    print("-------------------------------------------------")
    print(root) #当前目录路径
    print(files) #当前路径下所有非目录子文件
    for file_temp in files:
        if not file_temp.startswith("~$"):
            all_file_path.append(root + "\\" + file_temp)
    print("-------------------------------------------------")

print(all_file_path)
print(all_file_path.__len__())

for file_path in all_file_path:
    refactoring = output_path + file_path.replace(input_path, "")
    word = None
    try:
        word = RemoteWord(file_path)
        word.save_as(refactoring)
    except Exception as e:
        pass
    finally:
        word.close()
print(all_file_path)
