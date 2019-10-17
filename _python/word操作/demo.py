from utils.ZNHelper import *
from utils.RemoteWord_新 import *

if __name__ == "__main__":
    # aaa = '''[znznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznznzn张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠张楠]'''
    #
    # word = ZNWord("D:\\demo.docx")
    # word.replaceText(aaa, "jz")
    # word.save("D:\\aaa\\demo11.docx")
    input_path = r"D:/aaa/ss/s.s/demo111-1-2-3.docx"
    document_name = re.findall("-([\d]*)\.", input_path)
    print(document_name)

    # word_template = Word()
    # word_template.open_document(r"D:/123.docx")
    # word_template.replace_doc("[案号]", "(2018)闽0203执234号")
    # word_template.save_document(r"D:/789.docx")
    # word_template.doc.Close(0)
    # word_template.quit()

    word = Word("D:/123.doc")
    word.replace_doc("[案号]", "(2018)闽0203执234号")
    word.save_document("D:/456.docx")
    word.quit()


