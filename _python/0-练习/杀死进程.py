# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/15 10:57
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 杀死进程.py
@Description : 判断进程是否存在和杀进程
'''

from subprocess import run
import win32com.client


def processExist(processName):
    try:
        WMI = win32com.client.GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % processName)

        if len(processCodeCov) > 0:
            print(processName + " exist")
            return True
        else:
            print(processName + " is not exist")
            return False
    except Exception as e:
        print(processName + "error : ", e)
        raise e


def killProcess(processName):
    if processExist(processName):
        run('taskkill /f /im %s' % processName)


def processDealt():
    killProcess('IEDriverServer.exe')
    killProcess('iexplore.exe')
    killProcess('wps.exe')
    killProcess('WINWORD.EXE')
    killProcess('EXCEL.EXE')


if __name__ == "__main__":
    processDealt()
