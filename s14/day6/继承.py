#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface


#class People: #父类People 经典类写法
class People(object): #新式类写法 区别主要体现在继承上面

    def __init__(self,name,age):  #初始化实例
        self.name = name
        self.age  = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

class Relation(object):

    def make_friends(self,obj):
        print("%s is makeing friends wiht %s"%(self.name,obj.name))#为什么能用obj.name obj传的是w1 w1继承了People.name

class Man(People,Relation):# 子类Man 继承

    def piao(self):        #可以自己写一些新的方法
        print("%s is piaoing ... 20000s ...done."% self.name)

    def sleep(self):   #父类的sleep不会执行 覆盖了
        print("man is sleeping")

    def talk(self):  #重构了父类的方法 为父类增加新功能
        People.talk(self)  #先执行父类的
        print("man is sleeping") #再执行自己的


class Woman(People,Relation): #继承多一个就是多继承了 执行顺序从左到右
    def __init__(self,name,age,money):#为了单独多添加一个参数 重构初始化函数 父类的参数都要全写在上面 再写上自己的
#        People.__init__(self,name,age)  #经典类写法
        super(Woman, self).__init__(name,age) #新式类写法 这个作用和上面一条一毛一样 但比较方便比较骚 多继承的时候好用
        self.money = money
        print("%s 一出生就有%s money"%(self.name,self.money))

    def get_birth(self):
        print("%s is born a bady"% self.name)

m1 = Man("surface",18) #因为Man继承了People 所以要传参数
# m1.eat()
# m1.piao()
# m1.sleep()
# m1.talk()

w1 = Woman("ashe",28,1000) #因为重构了初始化 要传入money的值
# w1.get_birth() #Woman里面不能调用Man里面的方法的

m1.make_friends(w1)

