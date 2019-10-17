import os

def quire_all_file_path_of_dir(dir_path):
    all_file_path = []
    for root, dirs, files in os.walk(dir_path):
        print(root)  # 当前目录路径
        print(files)  # 当前路径下所有非目录子文件
        for file_temp in files:
            if not file_temp.startswith("~$") and not file_temp.endswith(".temp"):
                all_file_path.append(root + "/" + file_temp)
    return all_file_path