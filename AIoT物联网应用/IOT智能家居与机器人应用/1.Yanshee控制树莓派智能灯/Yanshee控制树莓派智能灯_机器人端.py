#!/usr/bin/env python
# -*- coding: utf-8 -*- 
  
from socket import *
import RobotApi

# 本案例试图通过Yanshee的远程控制指令来完成对树莓派智能灯的开灯、关灯和闪灯等行为
# 机器人端 代码
# 我们分别从终端输入 start 、 stop 、 flash来完成智能灯的开始、停止、闪烁三种状态的控制，并通过Yanshee读出当前指令的内容。然后输入exit退出。

HOST='10.10.64.207'  
PORT=9999  
 
#-------robot init---------
RobotApi.ubtRobotInitialize()
ret=RobotApi.ubtRobotConnect("sdk","1", "127.0.0.1")
if (0 != ret):
    print ("Error --> ubtRobotConnect return value: %d" % ret)
    exit(1)
 
#-----udp client init----------
s = socket(AF_INET,SOCK_DGRAM)  
s.connect((HOST,PORT))
 
while True:  
    message = raw_input('send message:>>')
    if message == "exit" :
        break
    s.sendall(message)  
    data = s.recv(1024)  
    print data
    if message == "start":
        RobotApi.ubtVoiceTTS(1,"打开智能灯")
    if message == "stop":
        RobotApi.ubtVoiceTTS(1,"关闭智能灯")
    if message == "flash":
        RobotApi.ubtVoiceTTS(1,"闪烁智能灯")
 
s.close()
#----------------------- block program end ----------------------                                                                                                                                 
RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                            
RobotApi.ubtRobotDeinitialize()
exit()