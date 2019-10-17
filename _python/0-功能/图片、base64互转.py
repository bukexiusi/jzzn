# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/24 22:23
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 图片、base64互转.py
@Description :
'''

import base64


def pic2str(path):
    with open(path,'rb') as f:
        ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
        return ls_f


def str2pic(str_, to_path="zn.jpg"):
    img_data = base64.b64decode(str_)
    with open(to_path, 'wb') as f:
        f.write(img_data)


if __name__ == "__main__":
    print(str(pic2str(r"E:\杂乱图片\3487622762d0f703b8e99eb000fa513d2797c593.jpg")))
