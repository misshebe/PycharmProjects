#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

names = ['ashe',"fiora","hebe"]

def change_name():
    names[0] = "艾希"
    print("inside func",names)

change_name()
print("outside",names) #就这样被你改变
#实力解说 只有字符串和整数是不能在函数里面改的
#列表 字典 集合 类 这些都是可以在局部里面改全局的  元组本来就不能改