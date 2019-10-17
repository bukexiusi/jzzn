from openpyxl import load_workbook

class read():

    def readxlsx(self, filename, Now=0):
        workbook = load_workbook(filename)
        sheets = workbook.get_sheet_names()  # 从名称获取sheet
        booksheet = workbook.get_sheet_by_name(sheets[0])

        rows = booksheet.rows

        z = next(rows)
        # rows = booksheet.rows
        columns = booksheet.columns
        x = []
        p = []
        for i in rows:
            y = {}
            p.append(i[Now].value)
            y = dict([(k.value, j.value) for k, j in zip(z, i)])
            # print(y)
            x.append(y)
        workbook.close()
        return x, z, p

    def xlsx_dict(self, filename):
        x, z, p = self.readxlsx(filename, 0)
        return x
    def xlsx_dict1(self, filename):
        x, z, p = self.readxlsx(filename, 0)
        y = []
        for i, j in zip(x, p):
            y.append({j: i})
        return y
