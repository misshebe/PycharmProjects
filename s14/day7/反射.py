#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

def bulk(self):
    print("%s is yelling..."%self.name)

class Cat(object):
    def __init__(self,name):
        self.name = name

    # def eat(self):
    #     print("%s is eating..."%self.name)

    def eat(self,food):
        print("%s is eating..."%self.name,food)

c = Cat("Ake")
choice = input(">>:").strip()

# print(hasattr(c,choice)) #判断有没有一个属性 有就返回True
#
# print(getattr(c,choice)) #找到它的内存对象
#
# getattr(c,choice)() #加上括号 调用它

if hasattr(c,choice):
#    delattr(c,choice)  #删除一个属性
    func = getattr(c,choice)
    func("YingZheng")
else:
    setattr(c,choice,bulk) #动态的把一个外面的方法装配到类里面
    c.talk(c)


#反射
#hasattr(obj,name_str) 判断一个对象obj里是否有对应的name_str字符串的方法
#getattr(obj,name_str) 根据字符串去获取obj对象里的对应的方法的内存地址
#setattr(obj,'y',z) 相当于 x.y = v''
#delattr(obj,name_str) 删除一个属性