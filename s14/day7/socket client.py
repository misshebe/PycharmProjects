#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
#客户端
import socket

client = socket.socket() #声明socket类型 同时生成socket连接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    # client.send(b"Hello Surface!") #python3只能收发byte了 不能字符串
    client.send(msg.encode("utf-8"))
    data = client.recv(1024) #收多少 默认单位字节
    # print("recf:",data)
    print("recf:",data.decode())

client.close()