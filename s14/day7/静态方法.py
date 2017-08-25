#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod #这个是静态方法 和类斩断联系 变成一个普通函数
    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

d = Dog("ShiZiGou")
d.eat("包子")

#静态方法 只是名义上归类管理 实际上在静态方法里访问不了类或实例中的任何属性
#这里运行是会报错的 只是高级语法 高级语法就是不用也能活的很好

