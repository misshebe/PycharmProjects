#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

# import shelve,datetime
#
# d = shelve.open('shelve_test') #打开一个文件

# info = {'hebe':18,"job":'it'}
# name = ["ashe","fiora","hebe"]
#
# d["name"] = name #持久化列表
# d["info"] = info #持久化字典
# d["date"] = datetime.datetime.now()
#
# d.close()


import shelve,datetime

d = shelve.open('shelve_test') #打开一个文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
