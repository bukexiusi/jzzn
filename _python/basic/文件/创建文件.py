def main_client():
    # 创建空文件
    try:
        f = open('C:/test.txt', 'w')
        f.write("1111")
    except Exception as e:
        pass
    finally:
        f.close()
    #
    # 创建空文件二
    with open("C:/test.py", 'w') as f:
        f.write("zn")


if __name__ == '__main__':
    main_client()
