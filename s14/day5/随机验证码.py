#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

import random
checkcode=""
for i in range(4):
    current = random.randrange(0,4)
    if current == i:
        tmp = chr(random.randrange(65,90))
    else:
        tmp = random.randrange(0,9)
    checkcode += str(tmp)
print(checkcode)