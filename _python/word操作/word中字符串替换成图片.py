from utils.RemoteWord import *

word = Word()
word.open_document(r"D:/执行裁定书（罚金）.doc")
word.replace_picture("[承办人(zn:picture)]", "D:/曾国量.bmp")
word.replace_picture("[书记员(zn:picture)]", "D:/曾国量.bmp")
word.save_document("D:/123.doc")
word.doc.Close(0)

