# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/14 16:03
@Author  : 图南
@Email   : 935281275@qq.com
@File    : zn_base.py
@Description :
'''

import sys, os
import win32com.client
from execution import *
from yt.yt_sys import print



def __process_exist(process_name):
    try:
        WMI = win32com.client.GetObject('winmgmts:')
        process_code_cov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)

        if len(process_code_cov) > 0:
            # print(process_name + " exist")
            return True
        else:
            # print(process_name + " is not exist")
            return False
    except Exception as e:
        # print(process_name + "error : ", e)
        raise e


def __kill_process(process_name):
    if __process_exist(process_name):
        # run('taskkill /f /im %s' % process_name)
        os.system('taskkill /f /im %s' % process_name)


def __process_dealt():
    __kill_process('IEDriverServer.exe')
    __kill_process('iexplore.exe')
    # __kill_process('wps.exe')
    # __kill_process('et.exe')
    # __kill_process('WINWORD.EXE')
    # __kill_process('EXCEL.EXE')


if __name__ == "__main__":
    # __process_dealt()
    # func_name = sys.argv[1]
    func_name = "main()"
    try:
        print("翊通rpa执行开始")
        exec(func_name)
    except Exception as e:
        print(e)
    finally:
        print("翊通rpa执行完毕")
