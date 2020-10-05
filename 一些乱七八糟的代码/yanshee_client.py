#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import RobotApi

HOST = '10.10.64.207'
PORT = 9999

RobotApi.ubtRobotInitialize()
ret = RobotApi.ubtRobotConnect('sdk','1','127.0.0.1')
if (0!=ret):
    print('Return value: %d'%ret)
    exit(1)

s = socket(AF_INET,SOCK_DGRAM)
s.connect((HOST,PORT))

while True:
    message = raw_input('send message:>>')
    if message == 'exit':
        break
    s.sendall(message)
    data = s.recv(1024)
    print(data)
    if message == 'start':
        RobotApi.ubtVoiceTTS(1,'打开智能灯')
    if message == 'stop':
        RobotApi.ubtVoiceTTS(1,'关闭智能灯')
    if message =='flash':
        RobotApi.ubtVoiceTTS(1,'闪烁智能灯')
s.close()
RobotApi.ubtRobotDisconnect('sdk','1','127.0.0.1')
RobotApi.ubtRobotDeinitialize()
exit()