import re

def birthday_by_identity_card(ic_num):
    if len(ic_num) == 18:
        birthday_str = ic_num[6:14]
        return birthday_str[:4] + "年" + birthday_str[4:6] + "月" + birthday_str[6:] + "日"
    else:
        birthday_str = ic_num[6:12]
        return "19" + birthday_str[:2] + "年" + birthday_str[2:4] + "月" + birthday_str[4:] + "日"


if __name__ == "__main__":
    aaa = re.findall("\d{4}([\u4e00-\u9fa5]*)\d", '(2019)闽0211执3号')[0]

    a = "a,b,c"

    b = eval("a[:-1]")
    print(b)

    c = eval("a.split(',')")
    print(c)

    aa = "35082319930711001X"
    bb = "XXXXXX630815XXX"

    cc = eval("birthday_by_identity_card(bb)")
    print(cc)
