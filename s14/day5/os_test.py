#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

import os
# os.chdir("c:\\Users") #切换目录     cd 第一个\是转义符 233
# os.chdir(r"c:\Users\surface") #切换目录 推荐食用
# print(os.getcwd()) #获取当前的目录  pwd
# os.curdir #返回当前目录
# os.pardir #获取当前目录的父目录
#os.mkdir(r"C:\a\b\c") #递归创建目录 mkdir -p
#os.removedirs(r"C:\a\b\c") #若目录为空 则删除 并递归到上一级目录 如若也为空 则删除 依次类推
#os.mkdir(r"C:\a") #创建单个目录
#os.rmdir(r"C:\a\b\c") #只会删除最后c这个目录
#os.rename("oldname","newname") #重命名
# print(os.listdir('.')) #列出当前目录的文件  ls
# print(os.listdir('..')) #列出上一级的目录文件
# print(os.listdir("E:\\")) #列出E盘的文件
# print(os.listdir(r'E:')) #列出E盘的文件
# print(os.stat("随机验证码.py")) #获取文件/目录 信息
# print(os.sep)  #输出当前操作系统特定的路径分隔符
#print(os.linesep) #输出当面平台使用的行终止符 win"\r\n" linux"\n"
# print(os.environ) #查看当前系统上的环境变量
# print(os.pathsep) #查看当前系统path的分隔符 分割文件路径的字符串
# print(os.name)  #输出字符串指示当前使用的苹果 win=nt linux=posix
# print(os.system("ipconfig")) #运行系统命令 #linux os.system("ls")
# print(os.path.abspath(__file__)) #获取绝对路径
# print(os.path.dirname(r'c:\a\b\c\d.txt')) #返回目录名
# print(os.path.basename(r'c:\a\b\c\d.txt')) #返回文件名
# print(os.path.split(r"C:\a\b\c\d.txt")) #将path分割成目录和文件名二元组返回
# print(os.path.exists(r'd:')) #判断一个路径是否存在
# print(os.path.exists(r'd:\unexists.txt')) #判断一个文件是否存在
# print(os.path.isabs(r'c:\a\b\c\d.txt')) #判断这个路径是不是绝对路径
# print(os.path.isfile(r'c:\cang.avi')) #判断一个文件是否存在
# print(os.path.isdir(r'c:\windows')) #判断一个目录是否存在
# print(os.path.join(r'c;',r'\d',r'jin.avi')) #将多个路径组合后返回 第一个绝对路径之前的参数将被忽略
# print(os.path.join('/','etc','passwd')) #返回'/etc/passwd'
# print(os.path.getatime(r'c:\remixos_install.log')) #获取一个文件的最后存取 时间戳
# print(os.path.getmtime(r'c:\remixos_install.log')) #获取一个文件的最后修改时间