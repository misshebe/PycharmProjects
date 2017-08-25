#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import json
f = open("test.txt","r")

data = json.loads(f.read())

print(data['age'])
#反序列化用loads 把硬盘的数据读到内存