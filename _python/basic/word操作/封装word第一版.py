'''begin��word����'''
import win32clipboard, math, win32con
from win32com import client
from ctypes import windll


class ZNWord():

    '''��ʼ��'''
    def __init__(self, path=None, visible=0):
        self.word = client.DispatchEx('Word.Application')  # ʹ�ö����Ľ���
        self.word.Visible = visible  # 0Ϊ����ʾ��1Ϊ��ʾword����
        self.word.DisplayAlerts = 0  # 0Ϊ���治��ʾ:1Ϊ������ʾ
        self.doc = None  # �ĵ�
        self.fullPath = None  # �ļ�·��
        self.oldStrNotReplace = []  # �������ֶ��滻�����õ�����
        if path:
            self.open(path)

    '''��word'''
    def open(self, path, Encoding='gbk'):
        path = path.replace("\\", "/")
        self.fullPath = path
        try:
            self.doc = self.word.Documents.Open(FileName=path, Encoding=Encoding)
        except Exception:
            # ����win10�� D:/1.docx -> D:\\\\//1.docx ����(���ĵ���)
            try:
                path = path.replace("/", "\\")
                self.doc = self.word.Documents.Open(FileName=path, Encoding=Encoding)
            except Exception as e_inner:
                raise e_inner

    '''������'''
    def rename(self, newPath):
        os.rename(self.fullPath, newPath)

    '''wordȫ����'''
    def content(self):
        return self.doc.Range().text

    '''�滻����'''
    def replaceText(self, oldStr, newStr, clearStyle=False):
        if clearStyle:
            self.word.Selection.Find.ClearFormatting()
            self.word.Selection.Find.Replacement.ClearFormatting()
        '''����win10 8g�ڴ��� ��Լ250�ַ������ַ�������������'''
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

    '''�滻ͼƬ'''
    def replacePic(self, oldStr, newPicPaht):  # ֻ֧��.bmp�ļ�
        aString = windll.user32.LoadImageW(0, newPicPaht, win32con.IMAGE_BITMAP,
                                           0,
                                           0, win32con.LR_LOADFROMFILE)
        if aString != 0:  # ����ͼƬ��������  ͼƬ����ʧ�ܵĻ�  aString �͵���0
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
            win32clipboard.CloseClipboard()
        self.word.Selection.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, '^c', 2)

    '''����'''
    def save(self, savePath=None):
        self.__oldStrNotReplaceDealt()
        if savePath:  # ��pathΪ''������word��ԭ·��
            '''�ĵ����Ϊ'''
            savePath = savePath.replace("\\", "/")
            dir = re.findall(r"(.*)/", savePath)[0]
            if not os.path.exists(dir):
                os.makedirs(dir)
            self.doc.SaveAs(savePath)
        else:
            self.doc.Save()

    '''�ر��ĵ�'''
    def close(self, save=False):
        if save:
            self.__oldStrNotReplaceDealt()
            self.doc.Close(-1)
        else:
            self.doc.Close(0)

    '''���⴦��'''
    def __oldStrNotReplaceDealt(self):
        needReplace = self.oldStrNotReplace
        if len(needReplace):
            needReplace.sort(key=lambda i: len(i), reverse=True)
            for oldStr in needReplace:
                self.replaceText(oldStr, "")
            self.oldStrNotReplace = []

    '''��ֹ����'''
    def quit(self):
        self.word.Quit()

    # ��ȡdocument�ĵ�
    # def paragraphs(self):
    #     docValue = []
    #     for i in range(len(self.doc.Paragraphs)):  # ��������
    #         para = self.doc.Paragraphs[i]
    #         docValue.append(para.Range.text)  # ����/r
    #     return docValue


'''end��word����'''