#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

msg="你吞吞吐吐 我一脸懵逼"
print(msg)

print(msg.encode())#python3默认为utf-8 可以留空 但不建议 转换为bytes
print(msg.encode().decode())#python3默认为utf-8 可以留空 但不建议 转换为string

print(msg.encode(encoding="utf-8"))#转换为bytes类型(比特)
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))#转换为string类型


