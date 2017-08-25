#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import copy
names = ["Libai","Luna",["daji","buzhihuowu"],"Mozi","Ake"]
name2 = copy.deepcopy(names)  #复制一份列表 深复制
print(names)
print(name2)

names[1] = "露娜"
names[2][0] = "妲己"

print(names) #names的"Luna"变成"露娜"  子集中的"daji"变成"妲己"
print(name2) #names的变化和name2无关 是完全独立的两个列表

print(names[0:-1:2])

for i in names:
    print(i)


