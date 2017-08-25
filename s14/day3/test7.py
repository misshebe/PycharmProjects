#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
'''
def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('surface',age=18,sex='m')#第一个位置参数必须指定 kwarges必须要用key的方式添加
'''

'''
def test4(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test4('surface',sex='m',game='LOL',age=3)
test4('surface',6,sex='m',game='LOL') #能使用位置参数传参
'''
'''
def test5(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test5('surface',age=81,sex='m',game='LOL')
'''

def test6(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("DEMAXIYA")

def logger(source):
    print("from %s" % source)

test6('surface',age=81,sex='m',game='LOL')
#在一个函数里面引用另一个函数