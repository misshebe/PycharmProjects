#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

# lib->aa.py代码如下
# class C:
#     def __init__(self):
#         self.name = 'surface'


# mod = __import__("lib.aa") #导入lib目录下的aa.py
#
# obj = mod.aa.C()
# print(obj.name)


import importlib
aa = importlib.import_module('lib.aa') #官方建议食用
print(aa.C().name)

