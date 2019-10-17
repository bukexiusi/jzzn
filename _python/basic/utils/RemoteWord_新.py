import win32clipboard, math, win32con
from win32com import client
from ctypes import windll
import re, os, shutil


# 使用win32com扩展包，只对windows平台有效
class Word:
    # 初始化word
    def __init__(self, Visible=0, DisplayAlerts=0, newProcess=False):
        if newProcess:
            self.word = client.DispatchEx('Word.Application')  # 使用独立的进程
        else:
            self.word = client.Dispatch('Word.Application')
        self.word.Visible = Visible  # 0为不显示；1为显示word界面
        self.word.DisplayAlerts = DisplayAlerts  # 0为警告不显示:1为警告显示
        self.doc = None  # 文档
        self.filePath = None  # 文件路径
        self.oldStrNotReplace = [] # 解决文书分段替换所设置的数组

    # 获取文件路径
    def get_file_path(self):
        return self.filePath

    # 文件重命名
    def rename_document(self, newPath):
        shutil.move(self.filePath, newPath)

    # 打开FileName word 文件 todo 无法与在线文档一起使用
    def open_document(self, FileName, Encoding='gbk'):
        self.filePath = FileName
        self.doc = None
        try:
            self.doc = self.word.Documents.Open(FileName=FileName, Encoding=Encoding)
        except Exception as e:
            '''处理win10下 D:/1.docx -> D:\\\\//1.docx 问题(博文电脑)'''
            try:
                FileName = FileName.replace("/", "\\")
                self.filePath = FileName
                self.doc = self.word.Documents.Open(FileName=FileName, Encoding=Encoding)
            except Exception as e_inner:
                raise e_inner

    def switch_document(self, index):
        self.doc = self.word.Documents[index]

    # 在文档末尾添加内容
    def add_doc_end(self, string):
        rangee = self.doc.Range()
        rangee.InsertAfter('\n' + string)

    # 在文档开头添加内容
    def add_doc_start(self, string):
        rangee = self.doc.Range(0, 0)
        rangee.InsertBefore(string + '\n')

    # 在文档insertPos位置添加内容
    def insert_doc(self, insertPos, string):
        rangee = self.doc.Range(0, insertPos)
        if (insertPos == 0):
            rangee.InsertAfter(string)
        else:
            rangee.InsertAfter('\n' + string)

    # 替换文字
    def replace_doc(self, oldStr, newStr, clearStyle=False):
        if clearStyle:
            self.word.Selection.Find.ClearFormatting()
            self.word.Selection.Find.Replacement.ClearFormatting()
        '''处理win10 8g内存下 大约250字符以上字符参量过长问题'''
        str_limit = 125
        oldStrLen = len(oldStr)
        if oldStrLen > str_limit:
            count = math.ceil(oldStrLen / str_limit)
            for i in range(count):
                start = str_limit * i
                end = str_limit * (i + 1)
                if i == 0:
                    self.word.Selection.Find.Execute(oldStr[start:end], False, False, False, False, False, True, 1,
                                                     True, "[zn]", 2)
                else:
                    # self.word.Selection.Find.Execute(oldStr[start:end], False, False, False, False, False, True, 1,
                    #                                  True, "", 2)
                    self.oldStrNotReplace.append(oldStr[start:end])

            oldStr = "[zn]"
        newStr = '' if newStr is None else newStr
        newStrLen = len(newStr)
        if newStrLen < str_limit:
            self.word.Selection.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, newStr, 2)
        else:
            count = math.ceil(newStrLen / str_limit)
            tempStr = ''
            for j in range(count):
                tempStr = tempStr + "[z" + str(j) + "n]"
            self.word.Selection.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, tempStr, 2)
            for i in range(count):
                start = str_limit * i
                end = str_limit * (i + 1)
                self.word.Selection.Find.Execute("[z" + str(i) + "n]", False, False, False, False, False, True, 1, True,
                                                 newStr[start:end], 2)

    # 替换图片
    def replace_picture(self, oldStr, newPicPaht):  # 只支持.bmp文件
        aString = windll.user32.LoadImageW(0, newPicPaht, win32con.IMAGE_BITMAP,
                                           0,
                                           0, win32con.LR_LOADFROMFILE)
        if aString != 0:  # 由于图片编码问题  图片载入失败的话  aString 就等于0
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
            win32clipboard.CloseClipboard()
        self.word.Selection.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, '^c', 2)

    # 保存word
    def save_document(self, savePath=None):
        self.old_str_not_replace_dealt()
        if savePath:  # 若path为''，保存word在原路径
            # self.doc.SaveAs(savePath)
            '''文档另存为'''
            dir = re.findall(r"(.*)/", savePath)[0]
            if not os.path.exists(dir):
                os.makedirs(dir)
            self.doc.SaveAs(savePath)
        else:
            self.doc.Save()

    # 关闭打开的word文档
    def close_document(self):
        self.doc.Close(0)

    # 关闭打开的word文档
    def save_and_close_document(self):
        self.old_str_not_replace_dealt()
        self.doc.Close(-1)

    # 部分替换处理
    def old_str_not_replace_dealt(self):
        if len(self.oldStrNotReplace):
            needReplace = self.oldStrNotReplace
            needReplace.sort(key=lambda i: len(i), reverse=True)
            for oldStr in needReplace:
                self.replace_doc(oldStr, "")

    def quit(self):
        self.word.Quit()

    # 获取word的text
    def read_document_text(self):
        return self.doc.Range().Text

    # 读取document文档
    def read_document(self):
        docValue = []
        for i in range(len(self.doc.Paragraphs)):  # 遍历段落
            para = self.doc.Paragraphs[i]
            docValue.append(para.Range.text)  # 带有/r
        return docValue

    def delete_paragraph(self, endIndex, startIndex):
        for i in range(endIndex, startIndex, -1):
            del self.doc.Paragraphs[i]

    def word_copy_to_clipboard(self):  # 获取word的text
        try:
            self.doc.Content.Copy()
            return True
        except:
            self.doc[0].Content.Copy()
            return True

if __name__ == "__main__":
    word = Word()
    word.open_document("D:\\11.docx")
    word.replace_doc('add','add^padd')