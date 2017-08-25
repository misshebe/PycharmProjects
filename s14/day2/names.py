#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

names = ["Libai","Luna","Mozi","Ake"]
print(names)
print(names[0])#打印列表的第一个
print(names[0],names[2])#打印第一个和第三个
print(names[1:3])#打印第二个和第三个(顾头不顾尾)
print(names[0:4])#打印全部
print(names[:4])#前面是0的话 可以省略

print(names[-1])#打印最后一个
print(names[-3:-1])#打印第二个和第三个 注意:切片永远是从左往右的
print(names[-2:])#打印倒数第二个到最后一个

print(names.index("Luna"))#查找列表中Luna的下标
print(names[names.index("Luna")])#这多此一举 但好像有什么用
