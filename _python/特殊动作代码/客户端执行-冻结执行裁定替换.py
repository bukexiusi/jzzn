import pythoncom
import sys
import xlrd
import os
import re
import docx
import json
import math
from openpyxl import load_workbook
from win32com import client
from win32com import client
import re,os
from utils.RemoteWord import Word

def get_execute_params():
  return {"p1":"python","p2":"C:/upload/runtime_handle.py","p3":"wenshutihuan","$this":currentWidget.get('action_code'),"p4":inputValue}


#思明冻结文书替换
def wenshutihuan():
    path = param1
    path = path.replace("\\\\", "/")
    path = path.replace("\u202a", "")
    path = path.replace("\u202A", "")
    word = Word(newProcess=True)  # 在线文档无法和本地文档处于同一个进程中
    word.open_document(path)
    value1s = word.read_document()
    word.close_document()
    word.quit()

    start1 = 3 # 起始替换段落
    end1 = -1 # 截止替换段落
    for index in range(len(value1s)):
        value1 = value1s[index]
        if '裁定如下' in value1:
            end1 = index
            break
    start2 = 3 # 起始段落
    end2 = -1 # 截止段落
    word = Word()
    word.switch_document(0)
    value2s = word.read_document()
    for index in range(len(value2s)):
        value2 = value2s[index]
        if '裁定如下' in value2:
            end2 = index
            break

    # 将原段落全部清空
    for index in range(end2-1, start2 - 1, -1):
        text = word.doc.Paragraphs[index].Range.text
        raise Exception(text)
        if text == '\r':
            continue
        # word.replace_doc(text, '') # 最后一段无法直接替换空值
        word.doc.Paragraphs[index].Range.text = ''

    idx = start2
    for index in range(start1, end1 + 1):
        value1 = value1s[index]
        if index == end1:
            text = word.doc.Paragraphs[idx + 1].Range.text
            word.replace_doc(text[:-1], value1[:-1])
        else:
            word.doc.Paragraphs[idx].Range.InsertAfter(value1)
        idx = idx + 1

    # 替换本裁定
    word.replace_doc('本裁定', '本裁定立即执行')
