import json


# 前四个参数是固定的
def get_execute_params():
    return {
        "p1": "C:/seleniumNode/Python36/pythonw.exe",
        "p2": "C:/upload/runtime_handle.py",
        "p3": "a",
        "$this": currentWidget.get('action_code'),
        "p4": json.dumps(self_._taskExecution._batchParam), # 批参数
        "p5": json.dumps(collect_data),                    # 采集数据
        "p6": self_._taskExecution._task.get("task_name"), 
        "p7": document_data                    # 列表数据
    }

# 这个方法是真正在客户端执行的方法入口
def a():
    batch = param1 # 批变量
    collect_data = param2 # 采集数据
    task_name = param3
    list_data = param4
    txt_operation(batch, collect_data, task_name, list_data) # 在main_client中能调用方法

def txt_operation(batch, collect_data, task_name, list_data):
    f = open('E:/test.txt', 'a')
    case_code = list_data.get("案号")
    case_code2 = collect_data.get("案件信息")[0].get("案号")
    f.write(case_code)
    f.write(case_code2)
    f.close()