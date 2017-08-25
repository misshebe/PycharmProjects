#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import json
info={
    'name':'surface',
    'age':22
}

f = open("test.txt","w")
#print(json.dumps(info))
f.write( json.dumps(info))
f.close()
#序列化用dumps 把内存的数据存在硬盘上