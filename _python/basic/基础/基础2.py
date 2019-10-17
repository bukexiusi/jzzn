from utils.ZNHelper import *
a = 1
b = 2

def main():
    c = 1
    result = 1 if False else (2 if False else 3)
    browserValues = {
        None: "2"
    }
    result = browserValues.get(str(2))
    result = result if result else (browserValues.get('0') if browserValues.get('0') else browserValues.get(None))
    print(result)

    word = ZNWord()
    word.open("D:/123.doc")
    print(word.content())
    word.quit()


main()