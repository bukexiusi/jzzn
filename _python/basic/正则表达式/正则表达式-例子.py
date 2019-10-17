import re

# ^[1-9][0-9]{0,}$        // 所有的正整数
# ^\-{0,1}[0-9]{1,}$      // 所有的整数
# ^[-]?[0-9]+\.?[0-9]+$   // 所有的浮点数
#                //截取文件名

filePath = "C:/seleniumNode/a.b.txt"
fileName = re.findall(".*/(.*)\.", filePath)[0]
print(fileName)
