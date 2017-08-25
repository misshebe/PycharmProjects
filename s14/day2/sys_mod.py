#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
'''
import sys
print(sys.argv[2])#这里在命令行才能操作
'''

import os
cmd_res = os.popen("dir").read()#不加read不会显示在屏幕上
print("-->",cmd_res)

os.mkdir("shagua")#新建一个目录
