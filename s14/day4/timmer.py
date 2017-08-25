#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import time

def timmer(func):  #定义装饰器
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper  #注意这里没有括号 有会报错 TypeError: 'NoneType' object is not callable

@timmer             #放在要装饰的函数前面 调用装饰器
def test1():
    time.sleep(3)
    print("in the test1!")

test1()