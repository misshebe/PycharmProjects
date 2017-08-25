#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

print( all([0,-5,20]) ) #如果列表里面的可迭代对象所有的元素都为真的话 返回Ture 非0就是真 负数也为真
print( any([0,-5,20]) ) #任意一个为真 就返回Ture
print( any([]) )        #列表为空 则为False
print(bin(250))         #把数字转换成二进制
print(chr(97))          #返回数字的ASCII码的对应表
print(ord('a'))         #返回字符 与上面对应
print(globals())        #打印当前程序所有的key和value
print(hex(10))          #把数字转换成16进制
print(oct(8))           #转换成8进制
print(pow(2,8))         # x的y次方

a = {6:2,8:0,1:3,-6:6,99:66,2:50}
print( sorted(a.items()))  #按key排序
print( sorted(a.items(),key=lambda x:x[1])) #按value排序 x表示所有元素

b = [1,2,3,4,5,6]
c = ['a','b','c','d']
for i in zip(b,c):      #zip中文拉链
    print(i)            #会按最少的项一一对应  (1, 'a') (2, 'b') ...

#import module          #这里的模块名是没有引号的
#__import__('str_module_name') #只知道模块名的字符串可以用这种方法导入 听说还很有用 注意这里有引号的
