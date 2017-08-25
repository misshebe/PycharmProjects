#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
f = open("yesterday",'r+',encoding="utf-8") #文件句柄 读写 (常用)
f = open("yesterday",'w+',encoding="utf-8") #文件句柄 写读
f = open("yesterday",'a+',encoding="utf-8") #文件句柄 追加读写

f = open("yesterday",'rb',encoding="utf-8") #文件句柄 二进制文件 用途:1.网络传输 2.二进制文件 视频
f = open("yesterday",'wb',encoding="utf-8") #文件句柄 写
f.write("hello binary\n".encode())          #文件是以二进制编码的 看起来没什么两样
f.close()