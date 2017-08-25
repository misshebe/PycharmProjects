#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()

foo()
# 函数嵌套的定义是在一个函数的函数体内
# 用def去声明一个新的函数 而不是去调用一个函数
# This is 函数嵌套