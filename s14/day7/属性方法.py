#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
class Dog(object):
    def __init__(self,name):
        self.name = name

    @property  #把一个方法变属性
    def eat(self):
        print("%s is eat %s" %(self.name,self.__food))

    @eat.setter #修改它
    def eat(self,food):
        print("set to food:",food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删除了")

d = Dog("ShiZiGou")
d.eat = "baozi"
d.eat