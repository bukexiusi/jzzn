import re

dict_obj = {
    "案号": "(2018)闽0203执8231号",
    "法官": "张三",
    "执行主体信息": [
        {
            "案号": "(2018)闽0203执8231号",
            "姓名": "李四"
        }, {
            "案号": "(2018)闽0203执8231号",
            "姓名": "王五"
        }, {
            "案号": "(2018)闽0203执8231号",
            "单位名称": "北京软星科技有限公司",
            "法人代表": "赵六"
        }
    ],
    "车辆信息": [
        {
            "姓名": "哼哼",
            "车辆信息": "aaa"
        }
    ]

}
a = """
1:[案号]
[执行主体信息.案号3]
2:[法官]
	3:[执行主体信息.案号]
{zn:for 执行主体信息@@zn:if <类型>==自然人::<案号>,<姓名>；##<类型>==法人::<案号>,<单位名称>,<法人代表>； zn:endif@@ zn:endfor}
第一个问题，数据格式自定义
第二个问题，一份模板根据当事人数量生成文书（通知书）
第三个问题，有些数据来自法官自己编写，不来源于数据？？？
第四个问题，指定生成文书
{zn:for 执行主体信息@@<案号>,<姓名>；@@ zn:endfor}
[执行主体信息.案号2]
"""
# {zn:for 执行主体信息|zn:if <案号>="闽" <案号> zn:endif； zn:endfor}
b = re.findall(r"\[(.*?)\]", a)
print(b)
print(len(b))

c = re.findall(r"\{([\s\S]*?)\}", a)
print(c)
print(len(c))

for ci in c:
    ci1 = re.findall(r"zn:for (.*?) zn:endfor", ci)
    ci2 = ci1[0].split("@@")
    if "zn:" in ci2[1]:
        pass
    else:
        sub = dict_obj.get(ci2[0])
        result = ""
        for di in sub:
            content = ci2[1]
            content_array = re.findall("<(.*?)>", content)
            content_array = list(set(content_array)) # 数组去重
            for cai in content_array:
                if di.get(cai):
                    content =  content.replace("<" + cai + ">", di.get(cai))
            result = result + content
            print(result)
        result = result[:-1] + "。"
        print(a.replace("{" + ci + "}", result))

print(re.findall(r"\[.*\..*\]", a))
import re
write = re.findall("(\d+)号", ${案号})[0]