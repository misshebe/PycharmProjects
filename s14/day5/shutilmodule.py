#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import shutil

f1 = open("死亡笔记.txt",encoding="utf-8")

f2 = open("死亡笔记续集.txt","w",encoding="utf-8")

shutil.copyfileobj(f1,f2) #把死亡笔记的内容复制到死亡笔记续集

shutil.copyfile("死亡笔记续集.txt","死亡笔记续续集.txt") #直接把文件1复制到文件2

# e.g
# shutil.copymode(src,dst) #仅copy了权限 own不变
#
# shutil.copystat(src,dst) #copy所有的属性
#
# shutil.copy(src,dst) #copy文件和权限
#
# shutil.copy2(src,dst) #copy文件和状态信息
#
# shutil.copytree(src,dst) #递归copy文件 相当于 cp -r
#
# shutil.rmtree("dirname") #递归删除目录
#
# shutil.move(src,dst) #递归的移动文件

#压缩
#shutil.make_archive("file_name","zip","path") #压缩的文件最好不要包括这个程序

