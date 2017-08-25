#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

'''
def test1():
    print('in the test1') #没写return 默认返回None

def test2():
    print('in the test2')
    return 0              #写了0 就是返回0

def test3():
    print('in the test3')
    return 1,'hello',['surface','magua'],{'name':'luna'}  #全部返回为一个元组

x=test1()
y=test2()
z=test3()

print(x)
print(y)
print(z)
'''

# **kwargs:把N个关键字参数 转换成字典的方式
def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test2(name='surface',age=8,sex='F')
test2(**{'name':'surface','age':8,'sex':'F'})