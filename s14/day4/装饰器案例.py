#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

import time

def timer(func):    #timer(test1)  func=test1 | test2
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)                     #run test1
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco

# def timer():
#     def deco():
#         pass
#嵌套函数

@timer           #test1=timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timer
def test2(name,age):  #参数在函数括号里面定义的
    time.sleep(2)
    print("in test2",name,age)   #各种各样的需求

test1()
test2('suface',18)

# print(timer(test1))  #打印出了deco的内存地址 deco的房间
# m=timer(test1)       #给deco的房间一个门牌号
# m()                  #执行函数体里的代码
#以上三个步骤可以在函数前使用 @装饰器 一步完成