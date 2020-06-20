#!/usr/bin/env python

# -*- coding: utf-8 -*-
# 流程说明：机器人循环说出八条命令、让Yanshee2机器人依次执行。每条指令之间间隔两秒，一套动作执行完一遍之后延时三秒。


from socket import *
import RobotApi

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

environment_sensor = RobotApi.UBTEDU_ROBOTENV_SENSOR_T()

flag = 1

while True:

    time.sleep(2)

   

    if flag == 1 :

        RobotApi.ubtVoiceTTS(1,"向前走")

        message = "forward"

        flag = 2

    elif flag == 2 :

        RobotApi.ubtVoiceTTS(1,"向后走")

        message = "backward"

        flag = 3

    elif flag == 3 :

        RobotApi.ubtVoiceTTS(1,"向左走")

        message = "left"

        flag = 4

    elif flag == 4 :

        RobotApi.ubtVoiceTTS(1,"向右走")

        message = "right"

        flag = 5

    elif flag == 5 :

        RobotApi.ubtVoiceTTS(1,"鞠躬")

        message = "bow"

        flag = 6

    elif flag == 6 :

        RobotApi.ubtVoiceTTS(1,"举左手")

        message = "raise"

        flag = 7

    elif flag == 7 :

        RobotApi.ubtVoiceTTS(1,"你是谁")

        message = "say"

        flag = 8

    elif flag == 8 :

        RobotApi.ubtVoiceTTS(1,"停止")

        message = "stop"

        flag = 1

        time.sleep(3)

 

    s.sendall(message) 

    data = s.recv(1024) 

    print data

 

s.close()

#----------------------- block program end ----------------------                                                                                                                                

RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                            

RobotApi.ubtRobotDeinitialize()

exit()