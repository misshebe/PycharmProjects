#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

with open("yesterday","r",encoding="utf-8") as f,\
      open("yesterday.bak","r",encoding="utf-8") as f2:
    for line in f:
        print(line.strip())
