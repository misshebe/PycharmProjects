#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface


'''
print(f.tell()) #打印当前文件句柄的指针指向的位置
#print(f.read(5))
print(f.readline()) #读取文件中的第一行
print(f.readline())
print(f.readline())
print(f.tell()) #打印当前的位置
f.seek(0)       #回到起始位置
print(f.readline()) #重新读一行 这行是起始行
print(f.tell())
'''
f = open("yesterday",'r',encoding="utf-8")
print(f.encoding) #打印文件的编码
print(f.fileno()) #返回一个整型的文件描述符 可用于底层操作系统的 I/O 操作
print(f.flush())  #把内存中的数据强制写入到硬盘中 默认是缓冲区满了才写入的

f = open("test",'a',encoding="utf-8")
f.seek(10)      #没用 不管用
f.truncate(20)  #一定会从开头截断20个字符 20后面的都删除