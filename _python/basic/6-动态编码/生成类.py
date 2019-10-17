# -*- coding: utf-8 -*-
'''
@Time    : 2019/8/1 14:51
@Author  : 图南
@Email   : 935281275@qq.com
@File    : 生成类.py
@Description :
'''
import importlib
from imp import reload as imp_reload


def create_class_meta(module_name, class_name):
    module_meta = __import__(module_name, globals(), locals(), [class_name])
    imp_reload(module_meta)
    class_meta = getattr(module_meta, class_name)
    return class_meta


# 推荐使用这种，__import__推荐
def create_class_meta2(module_name, class_name):
    module_meta = importlib.import_module(module_name)
    imp_reload(module_meta)  # 类的重载
    class_meta = getattr(module_meta, class_name)
    return class_meta
