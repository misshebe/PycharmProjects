#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

import time
def bar():             #你是主角
    time.sleep(3)
    print('in the bar')

def test(func):         #这与装饰器 装饰bar
    start_time=time.time()
    func()         #run bar
    stop_time=time.time()
    print("the func run time is %s" %(stop_time-start_time))

test(bar)  #这里把bar传入到test这个函数中运行 这里改变了调用方式了 不能修改调用方式的

bar()      #原生调用方式
# print(bar)
# func=bar
# print("bar",bar)
# print("func",func)
# func()