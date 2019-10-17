import os, re, time
from utils import DateHelper

def quire_all_file_path_of_dir(dir_path):
    all_file_path = []
    for root, dirs, files in os.walk(dir_path):
        print(root)  # 当前目录路径
        print(files)  # 当前路径下所有非目录子文件
        for file_temp in files:
            if not file_temp.startswith("~$") and not file_temp.endswith(".temp") \
                    and not file_temp.endswith(".tmp"):
                file_temp = file_temp.replace("\\", "/")
                all_file_path.append(root + "/" + file_temp)
    return all_file_path

# 目前只支持两级
def confirm_num_of_document(data, cycle_array):
    num = 1
    key_num_mapping = {}
    cycle_array = list(set(cycle_array)) # 去重，防止一样的替换内容生成双倍的份数
    for cycle_ in cycle_array:
        cycle_num_array = []
        # 截取条件
        cycle_split = cycle_.split("##")
        for cycle in cycle_split:
            cycle_condition_expression = re.findall("\(zn:if (.*?)\)", cycle)
            condition_key_left = None
            if len(cycle_condition_expression) > 0:
                cycle_condition_expression = cycle_condition_expression[0]
                cycle_condition_expression = cycle_condition_expression.replace('“', '"').replace('”', '"')
                # 左key数组
                condition_key_left = re.findall("<(.*?)>", cycle_condition_expression)
            else:
                cycle_condition_expression = None

            # 截取key
            cycle_key = None
            cycle_key_array = re.findall("(.*?)\(", cycle)
            if len(cycle_key_array) > 0:
                cycle_key = cycle_key_array[0]
            else:
                cycle_key = cycle
            cs_a = cycle_key.split(".")
            # 循环层数
            current_level = 0
            total_level = len(cs_a) - 1  # 等级从零开始
            # 循环层数各自对应的循环index记录
            if total_level < 0:
                break
            for i in range(total_level):
                cycle_num_array.append(0)

            w_boolean = True
            while w_boolean:
                if current_level == 0:
                    key = cs_a[current_level]
                    temp = data.get(key)
                    if isinstance(temp, list):
                        current_level = current_level + 1
                        if current_level == total_level:
                            key = cs_a[current_level]
                            before_temp = temp[cycle_num_array[current_level - 1]]
                            if key.startswith("t") and key.endswith("t"):
                                temp = "tt"
                            else:
                                temp = temp[cycle_num_array[current_level - 1]].get(key)
                            # key对应num计算
                            key_num_count(key_num_mapping, cycle_, temp, before_temp, condition_key_left, cycle_condition_expression)
                            # 更改循环下标
                            temp_cycle_num = cycle_num_array[current_level - 1]
                            cycle_num_array[current_level - 1] = temp_cycle_num + 1
                    else:
                        w_boolean = False
                else:
                    # 当前key
                    key = cs_a[current_level]

                    temp = None
                    for cli in range(current_level):
                        if total_level == 1:
                            temp = data.get(cs_a[cli])
                        else:
                            if cli > 0:
                                temp = temp[cycle_num_array[cli - 1]].get(cs_a[cli])
                            else:
                                temp = data.get(cs_a[cli])

                    # if current_level == total_level:
                    temp_index = cycle_num_array[current_level - 1]
                    if temp_index > len(temp) - 1:
                        if current_level == 1:
                            w_boolean = False
                        continue
                    before_temp = temp[temp_index]
                    if key.startswith("t") and key.endswith("t"):
                        temp = "tt"
                    else:
                        temp = temp[temp_index].get(key)
                    # key对应num计算
                    key_num_count(key_num_mapping, cycle_, temp, before_temp, condition_key_left, cycle_condition_expression)
                    # 下标累加
                    temp_cycle_num = cycle_num_array[current_level - 1]
                    cycle_num_array[current_level - 1] = temp_cycle_num + 1
            cycle_num_array = []
    for k, v in key_num_mapping.items():
        if v > num:
            num = v
    return num


def key_num_count(key_num_mapping, key, temp, before_temp, condition_key_left, cycle_condition_expression):
    if not (temp is None):
        if condition_key_left and cycle_condition_expression:
            for ckl in condition_key_left:
                replace_value = '' if before_temp.get(ckl) is None else before_temp.get(ckl)
                cycle_condition_expression = cycle_condition_expression.replace("<" + ckl + ">", '"' + replace_value + '"')
            try:
                if eval(cycle_condition_expression):
                    key_num = key_num_mapping.get(key)
                    if not key_num:
                        key_num = 0
                    key_num_mapping[key] = key_num + 1
            except Exception:
                pass
        else:
            key_num = key_num_mapping.get(key)
            if not key_num:
                key_num = 0
            key_num_mapping[key] = key_num + 1

def birthday_by_id_card(ic_num):
    if len(ic_num) == 18:
        birthday_str = ic_num[6:14]
        month = birthday_str[5:6] if birthday_str[4:6].startswith("0") else birthday_str[4:6]
        day = birthday_str[7:] if birthday_str[6:].startswith("0") else birthday_str[6:]
        return birthday_str[:4] + "年" + month + "月" + day + "日"
    else:
        birthday_str = ic_num[6:12]
        month = birthday_str[3:4] if birthday_str[2:4].startswith("0") else birthday_str[2:4]
        day = birthday_str[5:] if birthday_str[4:].startswith("0") else birthday_str[4:]
        return "19" + birthday_str[:2] + "年" + month + "月" + day + "日"

def check_params(inputValue_global):
    inputValueArray = inputValue_global.split(";")
    if len(inputValueArray) < 4:
        raise Exception("文书生成缺少必要参数")
    else:
        if not inputValueArray[1]:
            raise Exception("文书生成缺少文书模板目录")
        if not inputValueArray[2]:
            raise Exception("文书生成缺少文书生成目录")

    court = inputValueArray[0]
    input_dir_path = inputValueArray[1]
    if input_dir_path:
        if not os.path.exists(input_dir_path):
            raise Exception(input_dir_path + " 文件夹不存在")
    output_dir_path = inputValueArray[2]
    extra_excel_path = inputValueArray[3]
    if extra_excel_path:
        if not os.path.exists(extra_excel_path):
            print(extra_excel_path + " 文件不存在")
    extra_picture_dir_path = ''
    if len(inputValueArray) == 5:
        extra_picture_dir_path = inputValueArray[4]

    return court, input_dir_path, output_dir_path, extra_excel_path, extra_picture_dir_path

def read_excel_to_dict(excelOperation, columnValue, case, sheetName, colunNmae):
    total_excel_dict = excelOperation.excel_to_dict_zn(sheetName, colunNmae)
    if isinstance(total_excel_dict, dict):
        match_excel_dict = total_excel_dict.get(columnValue)
        if isinstance(match_excel_dict, dict):
            for edk, edv in match_excel_dict.items():
                if edv:
                    case[edk] = edv
