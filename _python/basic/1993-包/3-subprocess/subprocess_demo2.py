# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/6 20:17
@Author  : 图南
@Email   : 935281275@qq.com
@File    : subprocess_demo2.py
@Description :
'''
import os
import re


def get_mac_and_ip():
    """
    # 获取本机MAC地址和IP地址
    :return: (MAC地址，IP地址)
    """
    # 使用with，不需要显式的写pipe.close()
    with os.popen('ipconfig -all') as pipe:
        str_config = pipe.read()
        # print("完整配置信息：", str_config)
        # 利用正则表达式和re模块检索结果
        mac_re_compile = re.compile(r"物理地址[\. ]+: ([\w-]+)")
        ip_re_compile = re.compile(r"IPv4 地址[\. ]+: ([\.\d]+)")

        mac = mac_re_compile.findall(str_config)[0]  # 找到MAC
        ip = ip_re_compile.findall(str_config)[0]  # 找到IP

        # print("MAC=%s, IP=%s" % (mac, ip))

    return mac, ip


def execute_py():
    """
    # 获取本机MAC地址和IP地址
    :return: (MAC地址，IP地址)
    """
    # 使用with，不需要显式的写pipe.close()
    result_list = []
    with os.popen('python ./demo.py') as pipe:
        count = 0
        while True:
            result_list.append(pipe.readline())
            count += 1
            if count > 100:
                break

    return result_list


if __name__ == "__main__":
    # result = get_mac_and_ip()
    # print("MAC: %s\n IP: %s" % result)
    result = execute_py()
    print(result)
