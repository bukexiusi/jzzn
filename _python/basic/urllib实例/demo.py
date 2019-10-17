import urllib.request
import sys
import io

'''
编码名称	用途
utf8	所有语言
gbk	简体中文
gb2312	简体中文
gb18030	简体中文
big5	繁体中文
big5hkscs	繁体中文
'''

'''
urllib第一问
'''
#改变标准输出的
response = urllib.request.urlopen('http://www.baidu.com')
tag = "2"
if tag == "1":
    print(response.read().decode('utf-8'))
    '''
    print()函数的局限就是Python默认编码的局限，因为系统是win7的，python的默认编码不是'utf-8',改一下python的默认编码成'utf-8'就行了
    '''
elif tag == "2":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    print(response.read().decode('utf-8'))
    '''
    中文乱码，cmd不能很好的支持utf-8
    '''
elif tag == "3":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    print(response.read().decode('utf-8'))
    '''
    正常输出
    '''