
# 前四个参数是固定的
def get_execute_params():
    return {
        "p1": "C:/seleniumNode/Python36/pythonw.exe",
        "p2": "C:/upload/runtime_handle.py",
        "p3": "main_client",
        "$this": currentWidget.get('action_code'),
        "p4": param1
    }

# 这个方法是真正在客户端执行的方法入口
def main_client():
    txt_operation() # 在main_client中能调用方法

def txt_operation():
    f = open('E:/test.txt', 'a')
    f.write(param1)
    f.write(param2)
    f.close()