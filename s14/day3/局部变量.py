#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

school = "oldboy"  #全局变量在此
def change_name(name):
    global school  #反客为主 局部变量在全局生效要先声明
    school = "Qing Shan"
    print("before change",name)
    name = "ZhaoRiTian"
    print("after change",name)

name = "zhaoritian"
change_name(name)
print(name)
print("school:",school) #Qing Shan
#不要在复杂的程序 用函数改全局变量 会被开除哦