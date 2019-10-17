import re
from word操作.word整合类 import Word

def createDocument():
    dict_obj = {
        "案号": "(2018)闽0203执8231号",
        "法官": "张三",
        "执行主体信息": [
            {
                "案号": "(2018)闽0203执8231号",
                "姓名": "李四",
                "类型": "自然人"
            },{
                "案号": "(2018)闽0203执8231号",
                "姓名": "王五",
                "类型": "自然人"
            },{
                "案号": "(2018)闽0203执8231号",
                "单位名称": "北京软星科技有限公司",
                "法人代表": "赵六",
                "类型": "法人"
            }
        ]
    }
    word = None
    try:
        # 打开模板
        word = Word()
        word.open_document(r"G:\test.docx")
        refactoring = r"G:\test1.docx"
        word.save_document(refactoring)
        word.close_document()
        # 复制模板
        word = Word()
        word.open_document(refactoring)
        content = word.read_document_text()
        # 匹配单个
        re_array = re.findall(r"\[(.*?)\]", content)
        for re_element in re_array:
            re_result = None
            re_split = re_element.split(".")
            re_array_continue = False
            for rs in re_split:
                re_result = dict_obj.get(rs)
                if isinstance(re_result, str):
                    break
                elif isinstance(re_result, list):
                    re_result = re_result[0].get(rs)
                else:
                    re_array_continue = True
            if re_array_continue:
                continue
            word.replace_doc("[" + re_element + "]", re_result)
        # 匹配循环
        re_array2 = re.findall(r"\{([\s\S]*?)\}", content)
        for re_element2 in re_array2:
            ci1 = re.findall(r"zn:for (.*?) zn:endfor", re_element2)
            ci2 = ci1[0].split("@@")
            sub = dict_obj.get(ci2[0])
            if "zn:" in ci2[1]:
                re_result2 = ""
                zn1 = re.findall(r"zn:if (.*?) zn:endif", ci2[1])[0].split("##")
                # 遍历条件
                meet_boolean = False
                for di in sub:
                    for zn2 in zn1:
                        zn3 = zn2.split("::")
                        condition = zn3[0]
                        expression = zn3[1]
                        condition_left = re.findall(r"<(.*?)>", condition.split("==")[0])[0]
                        condition_right = condition.split("==")[1]
                        condition_symbol = "=="
                        condition_boolean = False
                        if condition_symbol == "==":
                            condition_boolean = di.get(condition_left) == condition_right
                        if condition_boolean:
                            content_array = re.findall("<(.*?)>", expression)
                            content_array = list(set(content_array))  # 数组去重
                            replace_boolean = True
                            for cai in content_array:
                                if cai in di.keys():
                                    expression = expression.replace("<" + cai + ">", di.get(cai))
                                else:
                                    replace_boolean = False
                            if replace_boolean:
                                re_result2 = re_result2 + expression
                            break
                re_result2 = re_result2[:-1] + "。"
                word.replace_doc("{" + re_element2 + "}", re_result2)
            else:

                re_result2 = ""
                for di in sub:
                    content = ci2[1]
                    content_array = re.findall("<(.*?)>", content)
                    content_array = list(set(content_array))  # 数组去重
                    replace_boolean = True
                    for cai in content_array:
                        if cai in di.keys():
                            content = content.replace("<" + cai + ">", di.get(cai))
                        else:
                            replace_boolean = False
                    if replace_boolean:
                        re_result2 = re_result2 + content
                re_result2 = re_result2[:-1] + "。"
                word.replace_doc("{" + re_element2 + "}", re_result2)
        word.save_document()
    except Exception as e:
        print(str(e))
    finally:
        word.close_document()




if __name__ == "__main__":
    createDocument()
