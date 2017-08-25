#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

#data = open("yesterday",encoding="utf-8").read()
#print(data)  # 注意这里没有引号

#读 单纯的读
f = open("yesterday",encoding="utf-8") #默认 模式为读
#文件句柄 就是文件的内存对象 #
#包含文件的文件名 它的字符集 大小 在硬盘上的起始位置 统一封装成一个内存对象 赋给变量f f变量就是这个文件的文件句柄
data = f.read()
print(data)

#写 有则覆盖 无则新建
f = open("yesterday2",'w',encoding="utf-8")

f.write("天王盖地虎\n")
f.write("小鸡炖蘑菇\n")
f.close()

#追加 append 能写但也不能读
f = open("yesterday2",'a',encoding="utf-8")

f.write("日日夜夜\n")
f.write("夜夜日日")
f.close()