'''begin：word操作'''
import win32clipboard, math, win32con
from win32com import client
from ctypes import windll


class ZNWord():

    '''初始化'''
    def __init__(self, path=None, visible=0):
        self.word = client.DispatchEx('Word.Application')  # 使用独立的进程
        self.word.Visible = visible  # 0为不显示；1为显示word界面
        self.word.DisplayAlerts = 0  # 0为警告不显示:1为警告显示
        self.doc = None  # 文档
        self.fullPath = None  # 文件路径
        self.oldStrNotReplace = []  # 解决文书分段替换所设置的数组
        if path:
            self.open(path)

    '''打开word'''
    def open(self, path, Encoding='gbk'):
        path = path.replace("\\", "/")
        self.fullPath = path
        try:
            self.doc = self.word.Documents.Open(FileName=path, Encoding=Encoding)
        except Exception:
            # 处理win10下 D:/1.docx -> D:\\\\//1.docx 问题(博文电脑)
            try:
                path = path.replace("/", "\\")
                self.doc = self.word.Documents.Open(FileName=path, Encoding=Encoding)
            except Exception as e_inner:
                raise e_inner

    '''重命名'''
    def rename(self, newPath):
        os.rename(self.fullPath, newPath)

    '''word全内容'''
    def content(self):
        return self.doc.Range().text

    '''替换文字'''
    def replaceText(self, oldStr, newStr, clearStyle=False):
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
            self.word.Selection.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, newStr, 1)
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

    '''替换图片'''
    def replacePic(self, oldStr, newPicPaht):  # 只支持.bmp文件
        aString = windll.user32.LoadImageW(0, newPicPaht, win32con.IMAGE_BITMAP,
                                           0,
                                           0, win32con.LR_LOADFROMFILE)
        if aString != 0:  # 由于图片编码问题  图片载入失败的话  aString 就等于0
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
            win32clipboard.CloseClipboard()
        self.word.Selection.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, '^c', 2)

    '''保存'''
    def save(self, savePath=None):
        self.__oldStrNotReplaceDealt()
        if savePath:  # 若path为''，保存word在原路径
            '''文档另存为'''
            savePath = savePath.replace("\\", "/")
            dir = re.findall(r"(.*)/", savePath)[0]
            if not os.path.exists(dir):
                os.makedirs(dir)
            self.doc.SaveAs(savePath)
        else:
            self.doc.Save()

    '''关闭文档'''
    def close(self, save=False):
        if save:
            self.__oldStrNotReplaceDealt()
            self.doc.Close(-1)
        else:
            self.doc.Close(0)

    '''特殊处理'''
    def __oldStrNotReplaceDealt(self):
        needReplace = self.oldStrNotReplace
        if len(needReplace):
            needReplace.sort(key=lambda i: len(i), reverse=True)
            for oldStr in needReplace:
                self.replaceText(oldStr, "")
            self.oldStrNotReplace = []

    '''终止进程'''
    def quit(self):
        self.word.Quit()

    # 读取document文档
    # def paragraphs(self):
    #     docValue = []
    #     for i in range(len(self.doc.Paragraphs)):  # 遍历段落
    #         para = self.doc.Paragraphs[i]
    #         docValue.append(para.Range.text)  # 带有/r
    #     return docValue


'''end：word操作'''