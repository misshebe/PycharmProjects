#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

info = {
    'stu1101':"Tian hai yi",
    'stu1102':"Da qiao wei jiu",
    'stu1103':"Lai ya mei li",
}

print(info)
print(info['stu1101']) # 查 打印key=stu1101的value
info['stu1101']    #除非确定有这个key才能用这种方法 否则报错
print(info.get('stu1108')) #正确的查找姿势 没有返回为空None
print('stu1101' in info) #判断key在不在字典里 在就返回True 否则False  ## info.has_key("stu1103") in py2.x

info ["stu1101"] = "天海翼"  #改 把stu1101的值改为"天海翼"

info["stu1104"] = "天使萌" #增 添加一个stu104 有则修改 无则添加

print(info)

del info["stu1104"] #删 del是python通用的删除方法
info.pop("stu1101") #删 不能留空 报错 留空不是删最后一个的 标准的删除姿势
info.popitem()  #删 随机删一个
print(info)