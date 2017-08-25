#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

def test1():
    print('in the test1')
    return 0
    print("打印不到我")

x=test1() #把return的返回值赋值给x
print(x)