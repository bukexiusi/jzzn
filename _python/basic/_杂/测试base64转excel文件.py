import base64
import os
import pandas
import time
table_file = '''
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
'''
start = time.time()
file_stream = base64.b64decode(str(table_file))
# 写入文件
with open(r'C:\workPath\a.xlsx', 'wb') as f:
    f.write(file_stream)
    filename = f.name
result = []
xls = pandas.ExcelFile(filename)
for exchange in xls.sheet_names:
    sheet = pandas.read_excel(xls, sheet_name=exchange, dtype=str)
    mapping = sheet.to_dict(orient='records')
    dictionary = {
        "data": mapping,
        "column_heads": sheet.columns.values.tolist()
    }
    result.append(dictionary)

end = time.time()
print(end - start)
