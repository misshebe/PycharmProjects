#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

names = ["Libai","Luna","Mozi","Ake"]
names.append("zhugeliang")#把zhugeliang追加到列表中
names.insert(1,"boluo")#把buluo插入到luna的位置 下标定位 不能批量插入 只能一个一个插

print(names)
print(names.index("Luna"))#查找列表中Luna的下标