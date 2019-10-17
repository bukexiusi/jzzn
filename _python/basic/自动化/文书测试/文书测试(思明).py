from utils.RemoteExcel import *
from utils.RemoteWord_新 import *
from utils import WordHelper, DateHelper
import time

def data_format():
    # 数据处理
    name_temp_count = 0
    name_temp_count2 = 0
    name_temp_count3 = 0
    name_temp_a = False
    name_temp_b = False
    name_temp_c = False
    name_temp_d = False
    name_temp_e = False
    name_temp_f = False

    # 称呼单复数特殊处理
    for litigant in litigants:
        if litigant.get("类型") == "自然人":
            name_temp_count = name_temp_count + 1
            name_temp_a = True
            if litigant.get("法律地位") == "申请人":
                name_temp_count2 = name_temp_count2 + 1
                name_temp_c = True
            if litigant.get("法律地位") == "被执行人":
                name_temp_count3 = name_temp_count3 + 1
                name_temp_e = True
        else:
            name_temp_count = name_temp_count + 1
            name_temp_b = True
            if litigant.get("法律地位") == "申请人":
                name_temp_count2 = name_temp_count2 + 1
                name_temp_d = True
            if litigant.get("法律地位") == "被执行人":
                name_temp_count3 = name_temp_count3 + 1
                name_temp_f = True

    if name_temp_count == 1:
        if name_temp_a:
            case["称呼单复数"] = "你"
        if name_temp_b:
            case["称呼单复数"] = "你单位"
    else:
        case["称呼单复数"] = "你们"
    # 申请人称呼单复数
    if name_temp_count2 == 1:
        if name_temp_c:
            case["申请人称呼单复数"] = "你"
        if name_temp_d:
            case["申请人称呼单复数"] = "你单位"
    else:
        case["申请人称呼单复数"] = "你们"
    # 被执行人称呼单复数
    if name_temp_count3 == 1:
        if name_temp_e:
            case["被执行人称呼单复数"] = "你"
        if name_temp_f:
            case["被执行人称呼单复数"] = "你单位"
    else:
        case["被执行人称呼单复数"] = "你们"

    # 文书生成日期
    current_time_array = time.localtime(time.time())
    current_time_str = time.strftime("%Y-%m-%d %H:%M:%S", current_time_array)
    case["文书生成日期"] = current_time_str


def document_create():

    court = "厦门市思明区人民法院"
    input_dir_path = "D:/chunsun/案件模板"
    output_dir_path = "D:/chunsun/生成模板"
    extra_picture_dir_path = ""

    word = None
    word_template = None
    try:
        # 案号处理
        case_code = case.get("案号")
        case_code = case_code.replace("(", "（").replace(")", "）")
        case["案号"] = case_code
        pre_case_code = case.get("执行依据文号")
        pre_case_code = pre_case_code.replace("(", "（").replace(")", "）")
        case["执行依据文号"] = pre_case_code
        # 截取序号
        if excelOperation:
            # 思明补充信息
            case_num = case.get("案号")
            if case_num:
                case_num = re.findall(r".*[\u4e00-\u9fa5](.*)号", case_num)
                if len(case_num) > 0:
                    case_num = case_num[0]
                    excel_dict = excelOperation.excel_to_dict_siming_zn(case_num)
                    for edk, edv in excel_dict.items():
                        if edv:
                            case[edk] = edv
            # 思明书记员信息
            clerk = case.get("书记员")
            if clerk:
                WordHelper.read_excel_to_dict(excelOperation, clerk, case, "承办人员信息", "对应书记员")

        # 有选择文书则按照选择文书生成结果，无选择文书则全部生成
        input_path_array = WordHelper.quire_all_file_path_of_dir(input_dir_path)
        document_select = case.get("选择文书")
        for input_path in input_path_array:
            execute_document = True
            input_path = input_path.replace("%20", " ")  # 有环境会将空格转义成%20
            input_path = input_path.replace("\\\\", "/")
            # input_path = input_path.replace("\\", "/")

            if document_select:
                execute_document = False
                fileName = re.findall(".*/(.*)\.", input_path)[0]
                if document_select == fileName:
                    execute_document = True
                elif document_select.startswith(fileName):
                    if fileName + "|" in document_select:
                        execute_document = True
                else:
                    if "|" + fileName in document_select:
                        execute_document = True

            if not execute_document:
                continue
            # 打开模板
            word_template = Word()
            word_template.open_document(input_path)

            word_content = word_template.read_document_text()
            if word_template:
                word_template.close_document()
            if word_content:
                copy_re_array = re.findall(
                    r"\[([\u4e00-\u9fa5\da-zA-Z\.\(\)\:]*?\(zn\:format .*? zn:endformat\)|.*?)\]", word_content)
            else:
                continue

            '''确定模板复制份数'''
            copy_re_array_match = []
            for cra in copy_re_array:
                if "." in cra:
                    copy_re_array_match.append(cra)
            copy_num = WordHelper.confirm_num_of_document(case, copy_re_array_match)
            copy_document_name_array = []
            copy_document_name_array2 = []

            sub_case_message = re.findall("(\d{4}).*?(\d+)号", case.get("案号"))
            if len(sub_case_message) == 0:
                raise Exception("案号格式错误")
            document_name = re.findall(".*/(.*?)\.", input_path)
            if len(document_name) == 0:
                raise Exception(input_path + "文件路径出错")
            document_name = document_name[0]
            multi_dir = input_path.replace(input_dir_path + "/", "")
            if court == "厦门市思明区人民法院":
                if copy_num == 1:
                    if "/" in multi_dir:
                        sub_multi_dir, sub_multi_document_name = re.findall("(.*)/(.*)", multi_dir)[0]
                        # multi_dir2
                        # multi_dir3 文书分类
                        multi_dir2 = sub_multi_dir + "/" + sub_multi_document_name
                        multi_dir3 = sub_multi_dir + "/" + case.get("案号") + "-" + sub_multi_document_name
                    else:
                        multi_dir2 = multi_dir
                        multi_dir3 = case.get("案号") + "-" + multi_dir
                    refactoring = output_dir_path + "/" + case.get("案号") + "/" + multi_dir2
                    copy_document_name_array.append(refactoring)
                    refactoring2 = output_dir_path + "/文书分类/" + document_name + "/" + multi_dir3
                    copy_document_name_array2.append(refactoring2)
                else:
                    for cni in range(copy_num):
                        if "/" in multi_dir:
                            sub_multi_dir, sub_multi_document_name = re.findall("(.*)/(.*)", multi_dir)[0]
                            sub_file_name, sub_suffix = re.findall("(.*)\.(.*)", sub_multi_document_name)[0]
                            multi_dir2 = sub_multi_dir + "/" + sub_file_name + "-" + str(
                                cni) + "." + sub_suffix
                            multi_dir3 = sub_multi_dir + "/" + case.get("案号") + "-" + sub_file_name + "-" + str(
                                cni) + "." + sub_suffix
                        else:
                            sub_file_name, sub_suffix = re.findall("(.*)\.(.*)", multi_dir)[0]
                            multi_dir2 = sub_file_name + "-" + str(cni) + "." + sub_suffix
                            multi_dir3 = case.get("案号") + "-" + sub_file_name + "-" + str(cni) + "." + sub_suffix
                        refactoring = output_dir_path + "/" + case.get("案号") + "/" + multi_dir2
                        copy_document_name_array.append(refactoring)
                        refactoring2 = output_dir_path + "/文书分类/" + document_name + "/" + multi_dir3
                        copy_document_name_array2.append(refactoring2)
            else:
                if copy_num == 1:
                    refactoring = output_dir_path + "/" + case.get("案号") + input_path.replace(input_dir_path, "")
                    copy_document_name_array.append(refactoring)
                else:
                    for cni in range(copy_num):
                        cutout = re.findall(".*/(.*)(\..*)", input_path)
                        if len(cutout) == 0:
                            raise Exception(word.get_file_path() + "非法文件名")
                        output_sub_path_name, output_suffix = cutout[0]
                        refactoring = output_dir_path + "/" + case.get(
                            "案号") + "/" + output_sub_path_name + "-" + str(cni) + output_suffix
                        copy_document_name_array.append(refactoring)

            '''匹配单个'''
            re_array = re.findall('\[([\u4e00-\u9fa5\da-zA-Z\.\(\)\:]*?\(zn\:format .*? zn:endformat\)|.*?)\]',
                                  word_content)
            re_array = set(re_array)
            '''匹配循环'''
            re_array2 = re.findall(r"\{\{([\s\S]*?)\}\}", word_content)
            '''复制模板并替换'''
            True_copy_index = 0
            for copy_index in range(copy_num):
                word = Word()
                word.open_document(input_path)
                new_path = copy_document_name_array[copy_index]  # 用于生成多分文档时自定义文件名
                new_path2 = None
                if len(copy_document_name_array2):
                    new_path2 = copy_document_name_array2[copy_index]
                for re_element in re_array:
                    re_result = None
                    re_element_temp = re.findall('(.*?)\(zn\:', re_element)
                    if len(re_element_temp) == 0:
                        re_element_temp = re_element
                    else:
                        re_element_temp = re_element_temp[0]

                    re_split = re_element_temp.split(".")
                    vfk = None
                    if len(re_split) == 1:
                        re_result = value_format(re_element, case, word, input_path, extra_picture_dir_path)
                        vfk = re_element
                    else:
                        replace_content = re_element.split("##")
                        max_data_num = 0
                        while True:
                            while_tag = False  # 循环取值标记
                            exit_tag = False  # 取不到值退出循环标记
                            mdata_key_temp = None
                            mdata_key_temp_parent = None
                            for rci in replace_content:
                                '''
                                执行主体信息.姓名(zn:if <法律地位>==”被执行人” and <类型>==”自然人”)
                                '''
                                mdata_key_temp_parent = re.findall("(.*?)\.", rci)  # 执行主体信息
                                if len(mdata_key_temp_parent) > 0:
                                    mdata_key_temp_parent = mdata_key_temp_parent[0]
                                    mdata_sub_list = case.get(mdata_key_temp_parent)
                                    if not mdata_sub_list:
                                        exit_tag = True
                                        continue
                                    exit_tag = False
                                    max_data_num = len(mdata_sub_list)

                                logic_expression = re.findall("\(zn:if (.*?)\)", rci)
                                if len(logic_expression) > 0:
                                    logic_expression = logic_expression[0]
                                    logic_expression = logic_expression.replace('“', '"').replace('”', '"')
                                else:
                                    logic_expression = None

                                if logic_expression:
                                    mdata_key_temp = re.findall("\.(.*?)\(", rci)  # 姓名
                                    if len(mdata_key_temp) > 0:
                                        mdata_key_temp = mdata_key_temp[0]
                                    logic_expression_t1 = logic_expression
                                    condition_key_left = re.findall("<(.*?)>", logic_expression)
                                    for ckli in condition_key_left:
                                        replace_temp = case.get(mdata_key_temp_parent)[True_copy_index].get(ckli)
                                        replace_temp = '' if replace_temp is None else replace_temp
                                        logic_expression_t1 = logic_expression_t1.replace("<" + ckli + ">", '"' +
                                                                                          replace_temp + '"')
                                    try:
                                        logic_expression_boolean = eval(logic_expression_t1)
                                    except Exception as e:
                                        raise Exception(input_path + "中" + logic_expression_t1 + "表达式出错")
                                    if logic_expression_boolean:
                                        while_tag = True
                                        break
                                else:
                                    mdata_key_temp = rci.split(".")
                                    if len(mdata_key_temp) > 1:
                                        mdata_key_temp = mdata_key_temp[1]
                                    while_tag = True
                                    break

                            if exit_tag:
                                break

                            if while_tag:
                                parent_data = case.get(mdata_key_temp_parent)
                                if not parent_data:
                                    while_tag = False
                                    True_copy_index = True_copy_index + 1
                                    if max_data_num == True_copy_index:
                                        break
                                    continue
                                re_result = value_format(mdata_key_temp, parent_data[True_copy_index], word,
                                                         input_path, extra_picture_dir_path)
                                vfk = mdata_key_temp
                                break
                            else:
                                True_copy_index = True_copy_index + 1
                                if max_data_num == True_copy_index:
                                    break

                    if re_result != vfk:
                        if not (re_result is None):
                            if not isinstance(re_result, str):
                                re_result = str(re_result)
                            word.replace_doc("[" + re_element + "]", re_result)
                    if re_result:
                        if "(zn:name)" in re_element:
                            cutout = re.findall("(.*)(\..*)", new_path)
                            if len(cutout) == 0:
                                raise Exception(new_path + "非法文件名")
                            word_path, word_suffix = cutout[0]
                            if copy_num == 1:
                                new_path = word_path + "-" + re_result + word_suffix
                            else:
                                new_path = re.sub('-[\d]*\.', "-" + re_result + ".", new_path)

                            if new_path2:
                                cutout = re.findall("(.*)(\..*)", new_path2)
                                if len(cutout) == 0:
                                    raise Exception(new_path2 + "非法文件名")
                                word_path, word_suffix = cutout[0]
                                if copy_num == 1:
                                    new_path2 = word_path + "-" + re_result + word_suffix
                                else:
                                    new_path2 = re.sub('-[\d]*\.', "-" + re_result + ".", new_path2)

                for re_element2 in re_array2:
                    format_content = []
                    temp_re_element2 = re_element2
                    if "zn:format" in re_element2:
                        format_content = re.findall("zn:format .*? zn:endformat", re_element2)
                        if len(format_content) == 0:
                            raise Exception(re_element2 + "处zn:format格式错误")
                        temp_re_element2 = re.sub("zn:format .*? zn:endformat", "{zn}", re_element2)
                    for_content_re = re.findall(r"zn:for (.*?) zn:endfor", temp_re_element2)
                    if len(for_content_re) < 1:
                        raise Exception(
                            input_path + "中" + re_element2 + "处配置错误，可能导致的原因是zn:for(空格)内容(空格)zn:endfor前后缺少必要的空格")
                    for_content_re = for_content_re[0]
                    for fc in format_content:
                        for_content_re = re.sub("{zn}", fc, for_content_re, 1)
                    for_content = for_content_re.split("@@")
                    if len(for_content) < 2:
                        raise Exception(input_path + "中" + for_content_re + "处配置错误，可能导致的原因是缺少必要的两组@@")
                    sub = case.get(for_content[0])
                    if not sub:
                        continue
                    re_result2 = ""
                    if for_content[1].startswith("zn:if"):
                        zn1 = re.findall(r"zn:if (.*?) zn:endif", for_content[1])
                        if len(zn1) < 1:
                            raise Exception(input_path + "中" + for_content[
                                1] + "处配置错误，可能导致的原因是zn:if(空格)内容(空格)zn:endif前后缺少必要的空格")
                        zn1 = zn1[0].split("##")
                        # 遍历条件
                        for di in sub:
                            for zn2 in zn1:
                                zn3 = zn2.split("::")
                                if len(zn3) < 2:
                                    raise Exception(input_path + "中" + zn2 + "处配置错误，可能导致的原因是缺少::")
                                condition = zn3[0].replace("“", "'").replace("”", "'")
                                expression = zn3[1]
                                condition_re = re.findall("<(.*?)>", condition)
                                for condition_re_key in condition_re:
                                    condition_left = di.get(condition_re_key)
                                    condition_left = '' if condition_left is None else condition_left
                                    condition = condition.replace("<" + condition_re_key + ">",
                                                                  "'" + condition_left + "'")

                                try:
                                    condition_boolean = eval(condition)
                                except Exception as e:
                                    raise Exception(input_path + "中" + condition + "表达式出错")
                                if condition_boolean:
                                    content_array = re.findall("<(.*?)>", expression)
                                    content_array = list(set(content_array))  # 数组去重
                                    for cai in content_array:
                                        ev = value_format(cai, di, word, input_path, extra_picture_dir_path)
                                        if not (ev is None):
                                            if ev != cai:
                                                expression = expression.replace("<" + cai + ">", ev)
                                    re_result2 = re_result2 + expression
                                    break
                    else:
                        for di in sub:
                            content = for_content[1]
                            content_array = re.findall("<(.*?)>", content)
                            content_array = list(set(content_array))  # 数组去重
                            for cai in content_array:
                                ev = value_format(cai, di, word, input_path, extra_picture_dir_path)
                                if not (ev is None):
                                    if ev != cai:
                                        content = content.replace("<" + cai + ">", ev)
                            re_result2 = re_result2 + content
                    re_result2 = re_result2.replace("\\n", "\r")
                    re_result2 = re_result2.replace("\\r", "\r")
                    re_result2 = re_result2.replace("\\t", "\t")
                    re_result2 = re_result2.replace("<p> ", '^p')
                    re_result2 = re_result2.replace("<p>", '^p')
                    if re_result2[-2:] == '^p':
                        re_result2 = re_result2[:-2] + for_content[2]
                    else:
                        re_result2 = re_result2[:-1] + for_content[2]
                    if re_result2:
                        word.replace_doc("{{" + re_element2 + "}}", re_result2)
                True_copy_index = True_copy_index + 1
                new_path = re.sub("\[.*?\]", "", new_path)
                word.save_document(new_path)
                if new_path2:
                    new_path2 = re.sub("\[.*?\]", "", new_path2)
                    word.save_document(new_path2)
                word.close_document()
    except Exception as e:
        if word:
            word.close_document()
        raise e
    finally:
        if word:
            word.quit()


def value_format(mdata_key, mdata, word, input_path, extra_picture_dir_path):
    mdata_key_temp = re.findall("([\u4e00-\u9fa5\da-zA-Z\-\_]*?)\(zn\:", mdata_key)
    if len(mdata_key_temp) > 0:
        mdata_key_true = mdata_key_temp[0]
        var = mdata.get(mdata_key_true)
        if not var:
            return var

        if "(zn:date " in mdata_key:
            try:
                time.strptime(var, "%Y-%m-%d %H:%M:%S")
            except Exception:
                try:
                    time.strptime(var, "%Y-%m-%d")
                    var = var + " 00:00:00"
                except Exception:
                    try:
                        time.strptime(var, "%y-%m-%d")
                        var = "20" + var + " 00:00:00"
                    except Exception:
                        pass
            mdata_key_format = re.findall("\(zn:date (.*?)\)", mdata_key)
            if len(mdata_key_format) < 1:
                raise Exception(input_path + "中" + mdata_key + "处可能缺少必要空格")
            mdata_key_format = mdata_key_format[0]
            if mdata_key_format == "中文日期零":
                var = DateHelper.chinese_date(var)
            elif mdata_key_format == "中文日期〇":
                var = DateHelper.chinese_date2(var)
            else:
                time_str = var
                try:
                    if time_str:
                        time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                        var = time.strftime(mdata_key_format, time_array).format(y='年', m='月',
                                                                                 d='日')
                    else:
                        var = ""
                except ValueError as e:
                    time_array = time.strptime(time_str, "%Y-%m-%d")
                    var = time.strftime(mdata_key_format, time_array).format(y='年', m='月',
                                                                             d='日')
                except Exception as e:
                    var = mdata.get(mdata_key)
            # 去掉月份前面0，日期前面0（南安需求），同时也会出去时分秒前面零
            re_var = re.findall("\d+", var)
            if len(re_var) > 0:
                var = re.sub("\d+", "{zn}", var)
                for rv in re_var:
                    if rv.startswith("0"):
                        rv = rv[1:]
                    var = re.sub("{zn}", rv, var, 1)

        if "(zn:format " in mdata_key:
            if not ("zn:endformat" in mdata_key):
                raise Exception(input_path + "中" + mdata_key + "处可能缺少zn:endformat")
            mdata_key_format = re.findall("\(zn:format (.*) zn:endformat\)", mdata_key)
            if len(mdata_key_format) < 1:
                raise Exception(input_path + "中" + mdata_key + "缺少必要空格")
            mdata_key_format = mdata_key_format[0]
            mdata_key_format = mdata_key_format.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
            var = eval(mdata_key_format)

        if "(zn:func " in mdata_key:
            ''' mdata_key ->  '''
            mdata_key_format = re.findall("\(zn:func (.*)\)", mdata_key)
            if len(mdata_key_format) < 1:
                raise Exception(input_path + "中" + mdata_key + "缺少必要空格")
            var = eval(mdata_key_format[0] + '("' + var + '")')

        if "(zn:picture)" in mdata_key:
            if extra_picture_dir_path:
                if extra_picture_dir_path.endswith("/"):
                    picture_path = extra_picture_dir_path + var + ".bmp"
                else:
                    picture_path = extra_picture_dir_path + "/" + var + ".bmp"
                word.replace_picture("[" + mdata_key + "]", picture_path)
            return mdata_key

        if "(zn:name)" in mdata_key:  # 不做格式上的处理
            pass
    else:
        if mdata_key.startswith("t") and mdata_key.endswith("t"):
            var = mdata_key[1:-1]
        else:
            var = mdata.get(mdata_key)
        if var is None:
            var = mdata_key
    return var


if __name__ == "__main__":
    excelOperation = Excel("D:/列表导出.xls")
    case_excel = excelOperation.excel_to_dict_result_zn("案件列表", "案号", "(2019)闽0203执3578号")
    litigant_excel = excelOperation.excel_to_dict_result_zn("当事人列表", "案号", "(2019)闽0203执3578号")
    global case
    global litigants
    case = case_excel
    litigants = litigant_excel
    case["当事人列表"] = litigant_excel

    '''数据处理'''
    data_format()
    '''文书生成'''
    document_create()

    # self.word.Selection.Find.Execute(
    #     oldStr, # findText
    #     False,  # matchCase
    #     False,  # matchWholeWord
    #     False,  # matchWildcards
    #     False,  # matchSoundsLike
    #     False,  # matchAllWordForms
    #     True,   # forward
    #     1,      # wrap
    #     True,   # format
    #     newStr, # replaceWith
    #     2)      # replace
    #             # matchKashida
    #             # matchDiacritics
    #             # matchAlefHamza
    #             # mathcControl