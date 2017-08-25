#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface


'''
for i in range(5):
    print(f.readline())
#取文件前五行的内容
'''

#print(f.readlines())  #这是一个列表 每行一个元素

'''
for index,line in enumerate(f.readlines()):
    if index == 9:
        print('--------华丽的分割线-------')
        continue
    print(line.strip()) #strip 把空格和换行去掉
#显示出第九行的内容
#readlines适合读小文件
'''

f = open("yesterday",'r',encoding="utf-8")

count = 0
for line in f:
    if count == 9:
        print('-------------华丽的分割线-------------')
        count += 1
        continue
    print(line.strip())
    count += 1
    #高效的循环方式 每次只往内存中读入一行