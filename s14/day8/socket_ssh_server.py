#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
#server
import socket,os
server = socket.socket()
server.bind(('localhost',6969))

server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行执行",data)
        cmd_res = os.popen(data.decode()).read()#接收字符串 执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has nno output..."

        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #先发大小给客户端
        client_ack = conn.recv(1024)  #等待客户端确认 解决粘包问题
        print("ack form client:",client_ack)
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()