#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

names = ["Libai","Luna","Mozi","Ake"]
names.remove("Mozi")
print(names)


names = ["Libai","Luna","Mozi","Ake"]
del names[2]
print(names)


names = ["Libai","Luna","Mozi","Ake"]
names.pop()   #默认删除最后一个
names.pop(2)  #效果等同 del name[2]
print(names)

print(names.count("Luna"))#统计列表中Luna的个数
#names.clear()  #清空列表
names.reverse() #反转列表中的顺序
names.sort()   #排序  特殊符号>数字>大写字母>小写字母(按ascii码排序规则)

names2 = [1,2,3,4]
names.extend(names2) #把name2合并到name1中 name2的内容不会删除
del names2 #删除变量 删除列表2
print(names)