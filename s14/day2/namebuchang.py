#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

names = ["Libai","Luna",["daji","buzhihuowu"],"Mozi","Ake"]
print(names[0:-1:2]) #隔一个打印一个 步长切片
print(names[::2]) #0和-1都可以省略  #效果应该和上一个一样 但我这里不是...#
print(names[:]) #打印0到-1 不建议这样写


for i in names:
    print(i)
#打印列表