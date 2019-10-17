import json

def main():
    case_code = document_data.get("案号")
    a = "\\"
    a_action_code='''
def a():
    case_code = param1
    b = param2
    c = ""
    f = open('E:/test.txt', 'a')
    f.write(case_code)
    f.write(str(b))
    f.write("翊通")
    f.write(c)
    f.close()
    '''
    path = '/session/' + self_._driver.session_id + '/exeCmd'
    url = '%s%s' % (self_._driver.command_executor._url, path)
    data = {
        "p1": "C:/seleniumNode/Python36/pythonw.exe",
        "p2": "C:\\upload\\runtime_handle.py",
        "p3": "a",
        "$this": a_action_code,
        "p4": case_code,
        "p5": "C:\\a.txt"
    }
    data_str = json.dumps(data)
    result = self_._driver.command_executor._request('POST', url, body=data_str.encode("utf-8"))
    if result.get('status') == 55 or result.get('status') == 500:
        raise Exception(result.get('value'))

    return case_code



def a():
    case_code = param1
    b = param2
    c = "\\\\"
    f = open('E:/test.txt', 'a')
    f.write(case_code)
    f.write(str(b))
    f.write("翊通")
    f.write(c)
    f.close()
    os.system('explorer.exe ' + output_dir_path.replace("/", "\\\\"))

\ -> 服务端正常变量 \\
     客户端         \\\\
     服务端中'''''' \\\\\\\\