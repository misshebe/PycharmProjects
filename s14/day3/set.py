#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

list_1 = [1,2,3,4,5,6,7,8,9]  #列表
list_1 = set(list_1)          #列表转集合
print(list_1,type(list_1))    #打印集合及其数据类型

list_2 = set([2,4,6,8,10])
print(list_1,list_2)          #打印两个集合

print(list_1.intersection(list_2)) #取这两个集合的交集
print(list_1.union(list_2))        #取这两个集合的并集 合并在一起并去重
print(list_1.difference(list_2))   #差集 in list_1 but not in list_2
print(list_2.difference(list_1))   #差集 in list_2 but not in list_1

list_3 = set([1,3,5])
print(list_3.issubset(list_1))     #判断list_3是不是list1的子集 子集有的 父集全有
print(list_1.issuperset(list_3))   #判断list_1是不是list_3的父集
print(list_1.symmetric_difference(list_2))  #对称差集 把两个集合都没有的 集合在一起 即把重复的去掉
print(list_1,list_2)

list_4 = set([2,4,6])              #list_4和list_3命中无交集
print(list_3.isdisjoint(list_4))   #判断两个集合有没有交集 没有则返回True

print("----------------------------")

print(list_1,list_2)
print(list_1 & list_2)  #交集
print(list_1 | list_2)  #并集 合并去重
print(list_1 - list_2)  #差集 在list_1中 但不在list2中 注意顺序
print(list_1 ^ list_2)  #对称差集 项在list_1中或者list_2中 但不会同时出现在二者中


print("=============================")

list_1.add(250)                 #集合中没有插入 只有添加
list_1.update([233,666,520])    #添加多项
print(list_1.remove(250))       #删除一项 天生去重 不会出现两个一样的数据
print(len(list_1))              #set的长度 一个数据为1
print(list_1.pop())             #随机删一个 并且返回删除的项
print(list_1.discard(999))      #删除一个不存在的项 不会报错 返回值都是None remove就会报错
print(list_1)