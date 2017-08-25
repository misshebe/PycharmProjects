#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

def add(a,b,f):
    return f(a)+f(b)
res = add(3,-6,abs) #把abs这个函数当作位置变量传到f的位置
print(res)          #abs的作用就是把负数变成正数
#这tm就是高阶函数