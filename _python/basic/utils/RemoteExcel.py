from openpyxl import load_workbook
import xlrd, copy


class Excel():

    def __init__(self, path):
        self.work_excel = xlrd.open_workbook(path)
        self.temp = {}

    def readxlsx(self, filename, Now=0):
        workbook = load_workbook(filename)
        sheets = workbook.get_sheet_names()  # 从名称获取sheet
        booksheet = workbook.get_sheet_by_name(sheets[0])
        rows = booksheet.rows
        z = next(rows)
        x = []
        p = []
        for i in rows:
            p.append(i[Now].value)
            y = dict([(k.value, j.value) for k, j in zip(z, i)])
            x.append(y)
        workbook.close()
        return x, z, p

    def xlsx_dict(self, filename):
        x, z, p = self.readxlsx(filename, 0)
        return x

    def xlsx_dict_sort(self, filename):
        x, z, p = self.readxlsx(filename, 0)
        y = []
        for i, j in zip(x, p):
            y.append({j: i})
        return y

    def excel_to_dict(self):
        count = len(self.work_excel.sheets())  # sheet数量
        result_array = []
        for ci in range(count):
            sheet_array = []
            for row in self.acquire_excel(self.work_excel, ci):
                sheet_array.append(row)
            result_array.append(sheet_array)
        return result_array

    def acquire_excel(self, excel, sheetnum):
        table = excel.sheets()[sheetnum]
        nor = table.nrows
        nol = table.ncols
        dict = {}
        for i in range(1, nor):
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)
                dict[title] = value
            yield dict

    def excel_to_dict_zn(self, sheet_name, key_colum_name):
        sheets = self.work_excel.sheets()
        i = -1
        for i in range(len(sheets)):
            if sheets[i].name == sheet_name:
                break
        if i > -1:
            table = sheets[i]
            result_dict = {}
            for row in self.acquire_excel_zn(table):
                rowCopy = copy.deepcopy(row)
                key = rowCopy.get(key_colum_name)
                value = result_dict.get(key)
                temp = None
                if value:
                    if isinstance(value, dict):
                        temp = [value]
                        temp.append(rowCopy)
                    else:
                        temp = value
                        temp.append(rowCopy)
                else:
                    temp = rowCopy
                result_dict[key] = temp

            return result_dict
        else:
            raise Exception("所选择的excel无sheet")

    def acquire_excel_zn(self, table):
        nor = table.nrows
        nol = table.ncols
        dict = {}
        for i in range(1, nor):
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)
                dict[title] = value
            yield dict

    def excel_to_dict_result_zn(self, sheet_name, colum_name, colum_value):
        sheets = self.work_excel.sheets()
        i = -1
        for i in range(len(sheets)):
            if sheets[i].name == sheet_name:
                break
        if i > -1:
            sheet = sheets[i]
            result_dict = self.temp.get(sheet.name)
            if not result_dict:
                result_dict = {
                    "index": 1,
                    "mapping": {}
                }
                self.temp[sheet.name] = result_dict

            mapping = result_dict.get("mapping")
            cache = mapping.get(colum_value)
            if cache:
                return cache
            start_index = result_dict.get("index")

            nor = sheet.nrows
            nol = sheet.ncols
            # 确定字段列数
            colum_name_order = 0
            for j in range(nol):
                title = sheet.cell_value(0, j)
                if title == colum_name:
                    colum_name_order = j
                    break

            match_tag = False
            mismatch_tag = False
            for i in range(start_index, nor):
                #
                excel_colum_value = sheet.cell_value(i, colum_name_order)
                if excel_colum_value == colum_value:
                    match_tag = True
                if match_tag:
                    if excel_colum_value != colum_value:
                        mismatch_tag = True
                if match_tag and mismatch_tag:
                    result_dict["index"] = i
                    break
                # 存值
                dictionary = {}
                for j in range(nol):
                    title = sheet.cell_value(0, j)
                    value = sheet.cell_value(i, j)
                    dictionary[title] = value
                cache = mapping.get(excel_colum_value)
                if cache:
                    if isinstance(cache, dict):
                        cache_temp = [cache]
                        cache_temp.append(dictionary)
                    else:
                        cache_temp = cache
                        cache_temp.append(dictionary)
                else:
                    cache_temp = dictionary
                mapping[excel_colum_value] = cache_temp

            return mapping.get(colum_value)
        else:
            raise Exception("所选择的excel无sheet")

    def acquire_excel_result_zn(self, sheet, colum_name, colum_value, row_index):

        cache = self.temp.get(sheet.name)  # 案件列表: {}
        if not cache:
            cache = {}
        result = cache.get(colum_value)  # {value: colum}
        if result:
            return result

        nor = sheet.nrows
        nol = sheet.ncols
        match_tag = False
        mismatch_tag = False
        for i in range(row_index, nor):
            dictionary = {}
            for j in range(nol):
                title = sheet.cell_value(0, j)
                value = sheet.cell_value(i, j)
                dictionary[title] = value
            '''
            {
                "案件列表": {
                    "(2019)闽0203执1号": {},
                    "(2019)闽0203执2号": {}
                },
                "执行主体列表": {

                }
            }
            '''
            result_value = cache.get(colum_value)
            result_value_temp = None
            if result_value:
                if isinstance(result_value, dict):
                    result_temp = [result_value]
                    result_temp.append(dictionary)
                else:
                    result_temp = result_value
                    result_temp.append(dictionary)
            else:
                result_temp = dictionary

            cache[dictionary.get(colum_name)] = result_temp

            if dictionary.get(colum_name) == colum_value:
                match_tag = True
            if match_tag:
                if dictionary.get(colum_name) != colum_value:
                    mismatch_tag = True
            if match_tag and mismatch_tag:
                break

        return cache.get(colum_value)

    '''
    思明写死代码 二分法查询案号
    '''

    def excel_to_dict_siming_zn(self, case_num):
        table = self.work_excel.sheets()[0]
        nor = table.nrows
        nol = table.ncols

        result_num = None
        # 起点
        start_num = 0
        # 终点
        end_num = nor
        # 当前案号
        current_num = nor // 2
        cycle_boolean = True
        cycle_num = 0
        while cycle_boolean and cycle_num < 30:
            if current_num == 0:
                '''防止取到标题'''
                break
            value = table.cell_value(current_num, 0)
            if value:
                if int(case_num) == int(value):
                    cycle_boolean = False
                    result_num = current_num
                else:
                    if int(case_num) > int(value):
                        ''' 落在右区间 '''
                        start_num = current_num
                    else:
                        ''' 落在左区间 '''
                        end_num = current_num
                    current_num = (start_num + end_num) // 2
            else:
                end_num = current_num
                current_num = current_num // 2
            cycle_num = cycle_num + 1

        result_dict = {}
        if result_num:
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(current_num, j)
                if isinstance(value, float):
                    value = int(value)
                result_dict[title] = value
        return result_dict