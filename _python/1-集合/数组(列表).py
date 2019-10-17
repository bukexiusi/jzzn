from functools import reduce

'''排序'''
myList = ['青海省','内蒙古自治区','西藏自治区','新疆维吾尔自治区','广西壮族自治区']
myList1 = sorted(myList, key=lambda i: len(i), reverse=True)
print(myList1)

myList = ['青海省','内蒙古自治区','西藏自治区','新疆维吾尔自治区','广西壮族自治区']
myList.sort(key=lambda i: len(i), reverse=True)
print(myList)

'''元素所在索引'''
elementArray = [1, "2", "3"]
print(elementArray.index("3"))
print("")

'''无序排序'''
columnValue = "213的"
columnValues = ["123", "213的", "23333"]
aDealt = sorted(enumerate(columnValues), key=lambda x: columnValue in x, reverse=True)
print(aDealt)

l = [1, 2, 3]
for index, val in enumerate(l):
    print ('index is %d, val is %d' % (index,val))
# 打印数组
print(*l, sep="\n")

'''去重(按照原有顺序)'''
reduceOrder = ['zn:for 当事人列表@@zn:if <法律地位>==”申请执行人”and <类型>==”自然人”::\\t申请执行人：<姓名>，<性别>，<证件号码(zn:func WordHelper.birthday_by_id_card)>出生，<民族>，住<地址>，公民身份号码<证件号码>。\\r##<法律地位>==”申请执行人”and <类型>==”法人”::\\t申请执行人：<姓名>，住所地<地址>，统一社会信用代码<单位机构代码>。\\r \\t法定代表人：<法定代表人姓名>。\\r zn:endif@@ zn:endfor', 'zn:for 当事人列表@@zn:if <法律地位>==”被执行人”and <类型>==”自然人”::\\t被执行人：<姓名>，<性别>，<证件号码(zn:func WordHelper.birthday_by_id_card)>出生，<民族>，住<地址>，公民身份号码<证件号码>。\\r##<法律地位>==”被执行人”and <类型>==”法人”::\\t被执行人：<姓名>，住所地<地址>，统一社会信用代码<单位机构代码>。\\r \\t法定代表人：<法定代表人姓名>。\\r zn:endif@@ zn:endfor', 'zn:for 当事人列表@@zn:if <法律地位>==”申请执行人”::<姓名>， zn:endif@@ zn:endfor', 'zn:for 当事人列表@@zn:if <法律地位>==”被执行人”::<姓名>， zn:endif@@ zn:endfor']

'''数组合并'''
array1 = [1]
array2 = [2]
array2.extend(array1)

'''数组元素对（位置不同）'''
z1 = ["1", "2"]
z2 = ["2", "1"]
zz2 = set(z1) & set(z2)
print("----------------------------------------------------------------")
print(len(zz2))

'''数组中字典去重'''
arr = [
    {'text': 'wuyuan','value': 1},
    {'text': '默认','value': 2},
    {'text': '默认','value': 2},
    {'text':  'wyy', 'value': 4}
]
f = lambda x, y: x if y in x else x + [y]
arr = reduce(f, [[], ] + arr)
print(arr)


'''逆序输出与删除元素'''
reversed_ = [1, 2, 3, 4, 5]

for i in reversed(reversed_):
    if i == 3:
        reversed_.remove(i)
print(reversed_)
