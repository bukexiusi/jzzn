def main():
    var = "python"
    return var

def get_execute_params():
    return {
        "p1": "C:/seleniumNode/Python36/pythonw.exe",
        "p2": "C:/upload/runtime_handle.py",
        "p3": "txt_operation",
        "$this": currentWidget.get('action_code'),
    }

def txt_operation():
    f = open('E:/test.txt', 'a')
    f.write('the second writing...')
    f.close()



def main():
    zn_dict = {}
    zn_dict["zn"] = "jz"
    set_value(zn_dict)
    for k, v in zn_dict.items():
        print(k, v)

def set_value(dictionary_obj):
    dictionary_obj["jz"] = "zn"

if __name__ == "__main__":
    main()