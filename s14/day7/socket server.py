#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
#服务端

import socket
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听的端口
server.listen() #监听

print("我要开始等电话了")
while True:
    # conn 就是客户端连过来而在服务端为其生成的一个连接实例
    conn, addr = server.accept()  # 等待 等电话打进来 #阻塞
    print(conn, addr)
    print("电话来了")

    while True:
        data = conn.recv(1024)#官方建议最大不超过8192 #recv默认是阻塞的
        if not data:break #客户端已断开 conn.recv收到的就都是空数据
        print("recv:",data)
        conn.send(data.upper()) #把数据变成大写发回去

server.close()