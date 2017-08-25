#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import hashlib
m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"World")       #这里是加密Hello+world
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"HelloWorld") #验证了上面
print(m2.hexdigest())

c2 = hashlib.md5()
c2.update("为了宇宙的和平".encode(encoding="utf-8"))  #使用中文要encode
print(c2.hexdigest())

s2 = hashlib.sha1()       #还有sha256 sha512 用法一毛一样
s2.update(b"HelloWorld")  #变长只是它的表现形式 重点是它里面的算法不一样
print(s2.hexdigest())


#python有一个hmac模块 他内部对我们创建key和内容进行处理然后加密
import hmac
h = hmac.new(b"666","瓜皮".encode(encoding='utf-8'))
print(h.hexdigest())  #hexdigest是十六进制加密 取值0-f
