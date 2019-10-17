import re, math, json, os, time
from functools import reduce

s_str = "a.b"
a_aray = s_str.split(".")
print("a_aray:", a_aray)

a = 10
b = 3
print(a/b) # 结果3.333
print(a//b) # 结果3，永远是整数

# 字符串跨行
s4 = '''Hello,
jz、
zn
a '''
print(s4)

# list 可变
family = ['jz', 'zn', 'jj']
# family[0]
# family[1]
# family[2]
# family[-1]
# family[-2]
# family[-3]
family.append("jj2") # 追加末尾元素
family.insert(1, "jj3") # 插入指定位置
family.pop() # 删除末尾元素
family.pop(1) # 删除指定位置元素

# tuple 元组（指向不可变，若tuple中含有list，则tuple中的list可变，但一直指向该list）
family_ = ('jz', 'zn', 'jj')

# 条件语句
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 循环语句
names = ['jz', 'zn', 'jj']
for name in names:
    print("for in 循环（字符串）>>> " + name)

sum = 0
for x in [1, 2, 3, 4, 5]:
    sum += x
print("for in 循环（数字）>>> " + str(sum))

sum = 0
for x in range(1000): # 生成1-999
    sum += x
print("for in 循环（数字）>>> " + str(sum))

sum = 0
x = 0
while x < 1000:
    sum += x
    x = x + 1
print("while循环（数字）>>> " + str(sum))

# dict(key - value)
familyDict = {
    'father': 'jz',
    'mother': 'zn'
}
familyDict['father'] = '江臻'
print("dict示例 >>> familyDict.get(\"daughter\")会报错！")
print("dict示例 >>> familyDict[\"daughter\"]会报错！")
print("dict示例 >>> " + familyDict.get("daughter", '你猜'))
if not ('daughter' in familyDict):
    familyDict['daughter'] = '江江'
print("dict示例 >>> " + familyDict['daughter'])

set_v = set([1, 2, 3])

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)

array = ["1", "2"]
print(array)
print(len(array))

array11 = []
array22 = ["1", "3"]
array33 = ["1", "2"]
array11.append(array22)
array11.append(array33)
print(array11)

dic = {'剧情': 11, '犯罪': 10, '动作': 8, '爱情': 3, '喜剧': 2, '冒险': 2, '悬疑': 2, '惊悚': 2, '奇幻': 1}
keys = list(dic.keys())
values = list(dic.values())
print(keys)
print(keys.__len__())
print(values)

aaaa = "\"d\""
print(re.findall(r'"(.*?)"', aaaa))


print(6%4)
print(6//4) # 向下取整数

abc = "(2018)闽0203执8231号"
abcd = re.findall(r".*[\u4e00-\u9fa5](.*)号", abc)
print(abcd)

current_xpath = "../"
if (not current_xpath.startswith("./")) and (not current_xpath.startswith('../')):
    print("1111")
if current_xpath.startswith('../'):
    current_xpath = "%s%s" %("/",current_xpath)
print("current_xpath", current_xpath)

zn = '''1:[案号]2:[法官]   3:[执行主体信息.案号]
{zn:for 执行主体信息@@<案号>,<姓名>；@@ zn:endfor}{zn:for 执行主体信息@@zn:if <类型>==自然人::<案号>,<姓名>。\\n##<类型>==法人::<案号>,<姓名>,<法定代表人姓名>。\\n zn:endif@@ zn:endfor}第一个问题，数据格式自定义
[正确案由]
[简案号]
[全案号]
[车辆信息.姓名]
'''

copy_re_array = re.findall(r"\[(.*?)\]", zn)
copy_re_array2 = []
print(copy_re_array)

for zn in copy_re_array:
    if "." in zn:
        copy_re_array2.append(zn)

print(copy_re_array2)

jzzn = "\\test.ad.docx"
jzzn2 = re.findall("(.*)\.", jzzn)
jzzn3 = re.findall(".*\.(.*)", jzzn)
print(jzzn2)
print(jzzn3)

jzzzn = '(2018)闽0203执8231号,福建金海峡融资担保有限公司(郭文彤),郭文彤。\n    (2018)闽0203执8231号,厦门奥大进出口有限公司(陈碧霞),陈碧霞。\n(2018)闽0203执8231号,陈碧霞。\n(2018)闽0203执8231号,林生仁。\n(2018)闽0203执8231号,陈嫩花。\\n'
print(jzzzn.endswith("\\n"))

cycle = "执行主体信息.姓名(zn:if)"
cycle_key = re.findall("(.*?)\(", cycle)
print(cycle_key)

abcd = '<法律地位>==被执行人 or <类型>==自然人'
abcd_ = re.findall("(==.*? |==.*?$)", abcd)
for a in abcd_:
    a_ = a.replace("==", "").replace(" ", "")
    abcd_[abcd_.index(a)] = a_
print(abcd_)

logic = re.findall("(\S*)", abcd)
logic_expression = ""
logic_index = 0
for li in logic:
    if li:
        if 'and' in li or 'not' in li or 'or' in li:
            logic_expression = logic_expression + li + " "
        else:
            logic_expression = logic_expression + "logic" + str(logic_index) + " "
            logic_index = logic_index + 1
print(logic_expression)

abcd = '"被执行人"=="被执行人" or "自然人"=="自然人"'
print("znzn", eval(abcd))

inputValue = "asddsafsdff"
document_param_array = re.findall("\${(.*?)}", inputValue)
print(document_param_array)
print(len(document_param_array))

eryuan = 6
eryuan = 123 if eryuan < 5 else 10
print(eryuan)

splitStr = "a;b;c;"
splitArray = splitStr.split(";")
print(len(splitArray))


print(math.ceil(float(401)/200))

url = "D:/文件夹1-/文书-1.docx"
re_result = "张三"
new_path = re.sub('-([^/]*?)\.', "-" + re_result + ".", url)
print(new_path)

print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
array_zn = [1, 2, 3 , 4, 5]
for i in range(3, len(array_zn) + 1):
    print(i)

zn1 = "zn"
zn1 = json.dumps(zn1)
zn1 = json.loads(zn1)
print(zn1)

zznn = 'zn'
zznn2 = eval('zznn')
print(zznn2)

va = ""
va_ = " "
print(len(re.findall("\s", va)))


# s = '''
# D:/wenshu/\xe4\xb8\x80\xe9\x94\xae\xe7\x94\x9f\xe6\x88\x90\xe6\xa8\xa1\xe6\x9d\xbf/\xe6\x89\xa7\xe8\xa1\x8c\xe8\xa3\x81\xe5\xae\x9a\xe4\xb9\xa6(\xe5\x88\xa4\xe5\x86\xb3).docx\xe4\xb8\xadzn:if<\xe6\xb3\x95\xe5\xbe\x8b\xe5\x9c\xb0\xe4\xbd\x8d>==\xe2\x80\x9d\xe7\x94\xb3\xe8\xaf\xb7\xe4\xba\xba\xe2\x80\x9dand<\xe7\xb1\xbb\xe5\x9e\x8b>==\xe2\x80\x9d\xe8\x87\xaa\xe7\x84\xb6\xe4\xba\xba\xe2\x80\x9d::\\t\xe7\x94\xb3\xe8\xaf\xb7\xe6\x89\xa7\xe8\xa1\x8c\xe4\xba\xba\xef\xbc\x9a<\xe5\xa7\x93\xe5\x90\x8d>\xef\xbc\x8c<\xe6\x80\xa7\xe5\x88\xab>\xef\xbc\x8c<\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f(zn:date%Y{y}%m{m}%d{d})\xe5\x87\xba\xe7\x94\x9f\xef\xbc\x8c<\xe6\xb0\x91\xe6\x97\x8f>\xef\xbc\x8c\xe4\xbd\x8f<\xe5\x9c\xb0\xe5\x9d\x80>\xef\xbc\x8c\xe5\x85\xac\xe6\xb0\x91\xe8\xba\xab\xe4\xbb\xbd\xe5\x8f\xb7\xe7\xa0\x81<\xe8\xaf\x81\xe4\xbb\xb6\xe5\x8f\xb7\xe7\xa0\x81>\xe3\x80\x82\\r##<\xe6\xb3\x95\xe5\xbe\x8b\xe5\x9c\xb0\xe4\xbd\x8d>==\xe2\x80\x9d\xe7\x94\xb3\xe8\xaf\xb7\xe4\xba\xba\xe2\x80\x9dand<\xe7\xb1\xbb\xe5\x9e\x8b>==\xe2\x80\x9d\xe6\xb3\x95\xe4\xba\xba\xe2\x80\x9d::\\t\xe7\x94\xb3\xe8\xaf\xb7\xe6\x89\xa7\xe8\xa1\x8c\xe4\xba\xba\xef\xbc\x9a<\xe5\xa7\x93\xe5\x90\x8d>\xef\xbc\x8c\xe4\xbd\x8f\xe6\x89\x80\xe5\x9c\xb0<\xe5\x9c\xb0\xe5\x9d\x80>\xef\xbc\x8c\xe7\xbb\x9f\xe4\xb8\x80\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xbf\xa1\xe7\x94\xa8\xe4\xbb\xa3\xe7\xa0\x81<\xe5\x8d\x95\xe4\xbd\x8d\xe6\x9c\xba\xe6\x9e\x84\xe4\xbb\xa3\xe7\xa0\x81>\xe3\x80\x82\\r \\t\xe6\xb3\x95\xe5\xae\x9a\xe4\xbb\xa3\xe8\xa1\xa8\xe4\xba\xba\xef\xbc\x9a<\xe6\xb3\x95\xe5\xae\x9a\xe4\xbb\xa3\xe8\xa1\xa8\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d>\xe3\x80\x82\\r zn:endif\xe5\xa4\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\x94\x99\xe8\xaf\xaf\xef\xbc\x8c\xe5\x8f\xaf\xe8\x83\xbd\xe5\xaf\xbc\xe8\x87\xb4\xe7\x9a\x84\xe5\x8e\x9f\xe5\x9b\xa0\xe6\x98\xafzn:if(\xe7\xa9\xba\xe6\xa0\xbc)\xe5\x86\x85\xe5\xae\xb9(\xe7\xa9\xba\xe6\xa0\xbc)zn:endif\xe5\x89\x8d\xe5\x90\x8e\xe7\xbc\xba\xe5\xb0\x91\xe5\xbf\x85\xe8\xa6\x81\xe7\x9a\x84\xe7\xa9\xba\xe6\xa0\xbc\r
# '''
# s = '''\xe7\xad\x89\xe5\xbe\x85\xe6\x96\xb0\xe7\xaa\x97\xe5\x8f\xa3\xe6\x89\x93\xe5\xbc\x80'''
s = '''PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'D:\\\\ChunSun\\\\Server\\\\clever-spiders4\\\\clever-spiders\\\\log\\\\log.2019-05-22' -> 'D:\\\\ChunSun\\\\Server\\\\clever-spiders4\\\\clever-spiders\\\\log\\\\log.2019-05-22.2019-05-22'\r, referer: http://150.101.192.4:8090/'''
s = '''\xe5\x8f\xa6\xe4\xb8\x80\xe4\xb8\xaa\xe7\xa8\x8b\xe5\xba\x8f\xe6\xad\xa3\xe5\x9c\xa8\xe4\xbd\xbf\xe7\x94\xa8\xe6\xad\xa4\xe6\x96\x87\xe4\xbb\xb6\xef\xbc\x8c\xe8\xbf\x9b\xe7\xa8\x8b\xe6\x97\xa0\xe6\xb3\x95\xe8\xae\xbf\xe9\x97\xae\xe3\x80\x82'''
# s = '''\xe5\xbd\x93\xe5\x89\x8d\xe6\xad\xa5\xe9\xaa\xa4\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a \xe6\x80\xbb\xe5\xaf\xb9\xe6\x80\xbb\xe6\x9f\xa5\xe8\xaf\xa2\xe7\x99\xbb\xe5\xbd\x95\xe6\xad\xa5\xe9\xaa\xa4'''
ss = s.encode('raw_unicode_escape')
print("znn", ss)  # 结果：b'\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
sss = ss.decode()
print(sss)

dict_test = {'0': 'zn'}
print("dict_test", dict_test.get('0'))

if {}:
    print("zn", "jz")
else:
    print("jz", "zn")
str_test = ""
array_test = str_test.split(";")
if "0" in array_test:
    print("1123123123123")

avdf = ["1", "2", "3"]
print(avdf.index("2"))
action_code = '''
from service.varmanagement import var_service
from service.varmanagement import zn_service

def main():
    pass

'''
replace_content = re.findall("from service\..*?service", action_code)
print(replace_content)

a = [1, 2, 3, 4, 5, 6]
# for i in a[-1:-7:-1]:
#     print(i)

# 左闭右开的原则
#  1   2   3   4   5   6  1  2  3  4  5  6
# -6  -5  -4  -3  -2  -1  0  1  2  3  4  5

for i in range(5, -1, -1):
    print(a[i])

# input_dir_path = "D:\\svn"
# if not os.path.exists(input_dir_path):
#     print(input_dir_path + " 文件夹不存在")
# else:
#     print("1111111111")
#
# output_dir_path = "D:\\chunsun\\生成模板\\"
# os.system('explorer.exe ' + output_dir_path)



aaa= '''zn:for 当事人列表@@zn:if <法律地位>==”申请人” and <类型>==”自然人”::    申请执行人：<姓名>，<性别(zn:format var[:-1] zn:endformat)>，<证件号码(zn:func birthday_by_id_card)>出生，<民族>，住<地址>，公民身份号码<证件号码>。\r##<法律地位>==”申请人” and <类型>==”法人”::    申请执行人：<姓名>，住所地<地址>，统一社会信用代码<单位机构代码>。\r法定代表人：<法定代表人姓名>。\r zn:endif@@ zn:endfor'''
for_content_re = re.findall(r"zn:for (.*?) zn:endfor", aaa)
print(for_content_re)


new_path2 = 'D:/chunsun/生成模板/文书分类/执行裁定书[我就去了]/（9102）闽0203执3469号-执行裁定书[我就去了].docx'
new_path2 = re.sub("\[.*?\]", "", new_path2)
print(new_path2)


msg = "中文"
print(msg.encode('utf-8'))

s1='\u70ed\u95e8\u94ed\u6587\u63a8\u8350'
s1='\u8BA4\u8BC1\u4FE1\u606F\u5B58\u653E\u5730\u5740'
print("112233")
print('s1=',s1)

s2='\\u70ed\\u95e8\\u94ed\\u6587\\u63a8\\u8350'
print('s2=',s2)

s3=s2.encode('utf-8').decode('unicode_escape')
print('s3=',s3)

jj = "中文"
zz = jj.encode("utf-8")
print(zz)


su = u'a汉字b'
sl = su.encode('gbk').decode('latin1')
print(s1)
# su_g2l = su.encode('gbk').decode('latin1')
# su_glg = su.encode('gbk').decode('latin1').encode('latin1').decode('gbk')
# su_g2u = su.encode('gbk').decode('utf8', 'replace')
# su_gug = su.encode('gbk').decode('utf8', 'replace').encode('utf8').decode('gbk')
# su_u2l = su.encode('utf8').decode('latin1')
# su_u2g = su.encode('utf8').decode('gbk')
# print(s1)
# print(su_g2l)
# print(su_glg)
# print(su_g2u)
# print(su_gug)
# print(su_u2l)
# print(su_u2g)

msg = "中文"
msgb = msg.encode("utf-8")
print(msgb)
for i in msgb:
    print(i)

print(bytes([228, 184, 173, 230, 150, 135]))
print(str(bytes([228, 184, 173, 230, 150, 135]).decode("utf8")))


'''
import re
write = re.findall("\((.*)\)", ${案号})[0]

import re
write = re.findall("\d([\u4e00-\u9fa5]+)\d", ${案号})[0]

import re
write = re.findall("(\d+)号", ${案号})[0]
'''
case_code = "(2019)闽0203执119号"
print(re.findall("\((.*)\)", case_code)[0])
print(re.findall("\d([\u4e00-\u9fa5]+)\d", case_code)[0])
print(re.findall("(\d+)号", case_code)[0])
'''
(2019)闽0203执119号
(2019)闽0203执210号
'''

print(time.time())

a = 119
b = 210
c = 522
d = 711

print(a+b+c+d)
print(a+b)
print(c+d)
print(c+d-(a+b))

param_column_name = "add_start"
print(re.findall("(.*)_(.*)", param_column_name)[0])

a = {"a": "a"}
b = a
b["a"] = "b"
print(a.get("a"))


arr=[{'text':'wuyuan','value':1},{'text':'默认','value':2},{'text':'默认','value':2},
{'text':'wyy','value':4}]
f = lambda x,y:x if y in x else x + [y]
arr = reduce(f, [[], ] + arr)
print(arr)



