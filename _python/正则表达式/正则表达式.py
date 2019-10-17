import re, zlib

# 正则匹配或
aaa = "[a][b][c]"
cc=re.findall(r"(\[a\]|\[b\])", aaa)
print(cc)
a = """ 
[案号]
{[执行主体信息.案号]，[执行主体信息.姓名]，[执行主体信息.性别]}
[案号]
{[执行主体信息.案号]，[执行主体信息.姓名]，[执行主体信息.性别]}
[案号]
{[执行主体信息.案号]，[执行主体信息.姓名]，[执行主体信息.性别]}
[案号]
{[执行主体信息.案号]，[执行主体信息.姓名]，[执行主体信息.性别]}
{[执行主体信息.案号]，[执行主体信息.姓名]，[执行主体信息.性别]}
[aaaaaaaaa]
{[执行主体信息.案号]，[执行主体信息.姓名]，[执行主体信息.性别]}
akdsdfsadf
asdfsdfsdfsdf
sadfasdfsdfsadf
"""

# 正则匹配非*（错）
c = "[a][b][c]"
d = re.findall(r"(?!\[a\])\[(.*?)\]", c) # (?!a) 不包含a
print(d)

# 正则匹配非 第二种形式 (?:\{.*?\}) 不匹配(?:这里的字符串)
g = re.findall(r"\s*(?:\{.*?\})?\s*\[(.*?)\]\s*(?:\{.*?\})?\s*", a)
print("g:", g)

aa = """
[[案号]
[收案日期]
	[执行主体信息.案号]
	{[zn:if 案号=” (2018)闽0203执8231号” [zn:for执行主体信息.案号; end] zn:if 案号=” (2018)闽0203执8232号”	[案号] zn:endif]}
	{[zn:if 案号=” (2018)闽0203执8231号” [zn:for执行主体信息.案号; end] zn:if 案号=” (2018)闽0203执8232号”	[案号] zn:endif]}
	[执行主体信息.案号]
{[zn:for执行主体信息.案号;  zn:endfor]}
[执行主体信息.案号]

"""
# bb=re.findall(r"\[([\s\S]*?)\]", aa)
# bb=re.findall(r"\s*(?:\[zn\:if[\s\S]*?zn\:endif\])?|(?:\[zn\:for[\s\S]*?zn\:endfor\])?\s*\[(.*?)\]", aa)
bb=re.findall(r"\s*(?!\[zn\:if[\s\S]*?zn\:endif\]|\[zn\:for[\s\S]*?zn\:endfor\])?\s*\[(.*?)\]\s*(?!\[zn\:if[\s\S]*?zn\:endif\]|\[zn\:for[\s\S]*?zn\:endfor\])?\s*", aa)
bb = re.findall(r"\s*(?:\{[\s\S]*?\})?\s*\[([\s\S]*?)\]\s*(?:\{[\s\S]*?\})?\s*", aa)

# bb=re.findall(r"\s*(?!\[zn\:for[\s]*?zn\:endfor\])?\s*\[(.*?)\]\s*(?!\[zn\:for[\s]*?zn\:endfor\])?\s*", aa)
# bb = re.findall(r"\[[\s\S]*?\]", aa)
print("-----------------bb--------------------:", bb)
bbb = re.findall(r"\{([\s\S]*?)\}", aa)
print("bbb:", bbb)
print("bbb:", len(bbb))
aaa="abc"
bbb = re.findall("[^ab]+", aaa)
print("bbb", bbb)
# g = re.findall(r"\s*(?:\{.*?\})?\s*\[(.*?)\]\s*(?:\{.*?\})?\s*", a)

aaaa = """
我就去了
"""
bb=re.findall(r"\s*(?!\[zn\:if[\s\S]*?zn\:endif\]|\[zn\:for[\s\S]*?zn\:endfor\])?\s*\[(.*?)\]\s*(?!\[zn\:if[\s\S]*?zn\:endif\]|\[zn\:for[\s\S]*?zn\:endfor\])?\s*", aa)



ah = '''[案号(zn:format re.findall('[(.*?)]'), var)][案号(zn:format re.findall('[(.*?)]'), var)][案号][案号(zn:format (:-1))]'''

ah_re = re.findall('\[.*?\]', ah)
print(ah_re)


ah_re2 = re.findall('\[([\u4e00-\u9fa5\da-zA-Z]*?\(zn:format re\..*?, var\)|.*?)\]', ah)
print(ah_re2)


ah_re2 = '''
         [案号(zn:name)(zn:format re.findall('[(.*?)]',var)[0] zn:endformat)][案号(zn:format re.findall('.*', var) zn:endformat)][执行主体信息.案号][执行主体信息.案号][执行主体信息.案号(zn:format re.findall('[\.\s]*', var) zn:endformat)]
'''
ah_re2 = "[案号(zn:format re.findall(‘d{4}’, var)[0]) zn:endformat)]"
ah_re2 = '[_a_-(zn:format re.findall(‘d{4}’, var)[0]) zn:endformat)]'
re_array = re.findall('\[([\u4e00-\u9fa5\da-zA-Z\.\(\)\:\_\-]*?\(zn\:format .*? zn:endformat\))\]', ah_re2)

var = '有字符'

var = eval('"\\n" + var if var else ""')
print(var)


znzn = '''
福 建 省 罗 源 县 人 民 法 院
协 助 执 行 通 知 书
[案号]
罗源县公安局交警大队车辆管理所：
申请执行人{{zn:for 执行主体信息@@zn:if <法律地位>==“申请人”::<姓名>、 zn:endif@@ zn:endfor}}与被执行人{{zn:for 执行主体信息@@zn:if <法律地位>==“被执行人”::<姓名>、 zn:endif@@ zn:endfor}}[案由]一案，本院作出的[执行依据文号][执行依据种类(zn:format re.findall(‘(民事|行政|刑事)’, var)[0] zn:endformat)][执行依据种类(zn:format re.findall(‘生效(.{3})’, var)[0] zn:endformat)]已经发生法律效力。由于被执行人{{zn:for 执行主体信息@@zn:if <法律地位>==“被执行人”::<姓名>、 zn:endif@@ zn:endfor}}未自动履行，依照《中华人民共和国民事诉讼法》第二百四十二条、《最高人民法院关于适用<中华人民共和国民事诉讼法>的解释》第四百八十七条之规定，请协助执行以下事项：
查封、扣押被执行人[车辆信息.所有人(zn:name)]名下的[车辆信息.具体车辆]，查封期限两年。
查封期间停止办理该车辆转移过户、抵押、租赁等相关手续。
附：[车辆信息.所有人(zn:name)]执行裁定书壹份

拟稿人：
审批人：


[文书生成日期(zn:date 中文日期〇)]


福 建 省 罗 源 县 人 民 法 院
协 助 执 行 通 知 书
[案号]
罗源县公安局交警大队车辆管理所：
申请执行人{{zn:for 执行主体信息@@zn:if <法律地位>==“申请人”::<姓名>、 zn:endif@@ zn:endfor}}与被执行人{{zn:for 执行主体信息@@zn:if <法律地位>==“被执行人”::<姓名>、 zn:endif@@ zn:endfor}}[案由]一案，本院作出的[执行依据文号][执行依据种类(zn:format re.findall(‘(民事|行政|刑事)’, var)[0] zn:endformat)][执行依据种类(zn:format re.findall(‘生效(.{3})’, var)[0] zn:endformat)]已经发生法律效力。由于被执行人{{zn:for 执行主体信息@@zn:if <法律地位>==“被执行人”::<姓名>、 zn:endif@@ zn:endfor}}未自动履行，依照《中华人民共和国民事诉讼法》第二百四十二条、《最高人民法院关于适用<中华人民共和国民事诉讼法>的解释》第四百八十七条之规定，请协助执行以下事项：
查封、扣押被执行人[车辆信息.所有人(zn:name)]名下的[车辆信息.具体车辆]，查封期限两年。
查封期间停止办理该车辆转移过户、抵押、租赁等相关手续。
附：[车辆信息.所有人(zn:name)]执行裁定书壹份

拟稿人：
审批人：


[文书生成日期(zn:date 中文日期〇)]
'''

jzjz = re.findall("\[([\u4e00-\u9fa5\da-zA-Z\.\(\)\:]*?\(zn\:format .*? zn:endformat\)|.*?)\]", znzn)
print(jzjz)