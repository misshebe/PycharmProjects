#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
#自定义异常
class SurfaceError(Exception):
    def __init__(self,msg):
        self.message = msg

try:
    raise SurfaceError("柯南保佑") #触发异常
except SurfaceError as e:
    print(e)