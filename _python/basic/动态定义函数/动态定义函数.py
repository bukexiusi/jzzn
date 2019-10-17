import re

if __name__ == "__main__":
    action_code ='''
    def add_demo2():
        \treturn 1
    def main():
        \treturn a + b + add_demo2()
    '''
    print(re.findall("(.*?)d", action_code))
    # 获取参数
    con = {'a': 1, 'b': 2, 'collect_data':'1', 'document_data':'1'}  # 设置全局变量
    exec(action_code.replace(re.findall("(.*?)d", action_code)[0], ""), con)
    params = con["main"]()  # json格式数据
    print(params)