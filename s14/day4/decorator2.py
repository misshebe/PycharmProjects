#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test(func):
    print(func)
    return func

t=test(bar)
print(t)  #有返回内存地址就能加()运行
t()

bar=test(bar) #变通一下就实现了 不修改调用方式
bar()