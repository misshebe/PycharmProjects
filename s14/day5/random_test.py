#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
import random
print(random.random()) #用于生成一个0到1的随机浮点数  0 <= n <1.0
print(random.uniform(2,5)) #和random一样 但可以指定取值区间
print(random.randint(1,7)) #随机生成一个int的随机数 前面和后面都能取到
print(random.randrange(1,3))#随机生成一个范围的整数 前面能取到 后面不能
print(random.choice('devops')) #从字符串中随机选择一个
print(random.choice([2,4,6])) #从列表中随机选择一个 (choice可放入序列:字符串 列表 元组)
print(random.sample('devops',2)) #从字符串中随机选择2个

items=[1,2,3,4,5,6,7,8]
print(items)
random.shuffle(items)  #洗牌功能 打乱有序的
print(items)