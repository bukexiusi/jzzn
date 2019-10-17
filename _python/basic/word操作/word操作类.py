import os
import win32com.client
import re

# 处理Word文档的类

class RemoteWord:
    def __init__(self, filename=None):
        self.xlApp = win32com.client.DispatchEx('Word.Application')
        self.xlApp.Visible = 0
        self.xlApp.DisplayAlerts = 0  # 后台运行，不显示，不警告
        if filename:
            self.filename = filename
            if os.path.exists(self.filename):
                self.doc = self.xlApp.Documents.Open(filename)
            else:
                self.doc = self.xlApp.Documents.Add()  # 创建新的文档
                self.doc.SaveAs(filename)
        else:
            self.doc = self.xlApp.Documents.Add()
            self.filename = ''

    def add_doc_end(self, string):
        '''在文档末尾添加内容'''
        rangee = self.doc.Range()
        rangee.InsertAfter('\n' + string)

    def add_doc_start(self, string):
        '''在文档开头添加内容'''
        rangee = self.doc.Range(0, 0)
        rangee.InsertBefore(string + '\n')

    def insert_doc(self, insertPos, string):
        '''在文档insertPos位置添加内容'''
        rangee = self.doc.Range(0, insertPos)
        if (insertPos == 0):
            rangee.InsertAfter(string)
        else:
            rangee.InsertAfter('\n' + string)

    def replace_doc(self, string, new_string):
        '''替换文字'''
        self.xlApp.Selection.Find.ClearFormatting()
        self.xlApp.Selection.Find.Replacement.ClearFormatting()
        self.xlApp.Selection.Find.Execute(string, False, False, False, False, False, True, 1, True, new_string, 2)

    def save(self):
        '''保存文档'''
        self.doc.Save()

    def save_as(self, filename):
        '''文档另存为'''
        dir = re.findall(r"(.*)\\", filename)[0]
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.doc.SaveAs(filename)

    def doc_content(self):
        '''文档内容'''
        return str(self.doc.Range())

    def close(self):
        '''保存文件、关闭文件'''
        self.save()
        self.xlApp.Documents.Close()
        self.xlApp.Quit()


if __name__ == '__main__':
    # doc = RemoteWord(r'D:\Data\test\test.docx')  # 初始化一个doc对象
    doc = RemoteWord(r"C:\Users\Administrator\Desktop\打印模板\模板一.docx")  # 初始化一个doc对象
    # 这里演示替换内容，其他功能自己按照上面类的功能按需使用
    # doc.replace_doc('zzzzzzzzzzzzzzzzzzzzzzzzzz', '你猜')  # 替换文本内容
    content = doc.doc_content()
    content_array = re.findall(r"\[(.*?)\]", content)
    print(content)
    doc.close()