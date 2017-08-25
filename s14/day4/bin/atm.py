#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

import os
print(__file__) #打印当前的路径 这是相对路径 它看起来是绝对路径 因为是在pycharm里面执行 linux就能看出是相对路径了
print(os.path.abspath(__file__)) #这tm才是绝对路径 通过相对路径自动返回绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #返回目录名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #返回上一级

BASE_DIR=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys
sys.path.append(BASE_DIR) #添加环境变量
#import conf,core #没有返回错误就ok了 conf和core有波浪线是因为动态加载的 不是错误

from conf import conf
from core import main

main.login()