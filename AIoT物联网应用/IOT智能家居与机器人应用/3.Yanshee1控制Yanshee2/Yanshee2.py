#!/usr/bin/env python

# -*- coding: utf-8 -*-

 
# 流程说明：当Yanshee2机器人接收到远端发来的控制命令之后，做相应的动作和语音行为等。
from socket import *
from time import sleep # Import the sleep function from the time module
import RobotApi

#UDP server init

HOST = '10.10.64.207'#chang the IP of your Rpi3

PORT = 9999

s = socket(AF_INET,SOCK_DGRAM) 

s.bind((HOST,PORT))

print '...waiting for Yanshee1\'s action command..'

 

#-------robot init---------

RobotApi.ubtRobotInitialize()

ret=RobotApi.ubtRobotConnect("sdk","1", "127.0.0.1")

if (0 != ret):

    print ("Error --> ubtRobotConnect return value: %d" % ret)

    exit(1)

 

while True: # Run forever

    data,address = s.recvfrom(1024)

    print data,address

    if data == "forward" :

        RobotApi.ubtSetRobotMotion("walk", "front", 4,1)

        RobotApi.ubtStartRobotAction("reset",1)

        print 'Robot move forward'

    elif data == "backward" :

        RobotApi.ubtSetRobotMotion("walk", "back", 2,1)

        RobotApi.ubtStartRobotAction("reset",1)

        print 'Robot move backward'

    elif data == "left" :

        RobotApi.ubtSetRobotMotion("walk", "left", 3,1)

        RobotApi.ubtStartRobotAction("reset",1)

        print 'Robot move left'

    elif data == "right" :

        RobotApi.ubtSetRobotMotion("walk", "right", 3,1)

        RobotApi.ubtStartRobotAction("reset",1)

        print 'Robot move right'

    elif data == "bow" :

        RobotApi.ubtSetRobotMotion("bow", "", 1, 1)

        print 'Robot do bow motion'

    elif data == "raise" :

        api.ubtSetRobotMotion("raise", "left", 4,1)

        print 'Robot raise left hand'

    elif data == "say" :

        RobotApi.ubtVoiceTTS(1,"你好，我是一个智能教学机器人")

        print 'Robot start to say something'

    elif data == "stop" :

        RobotApi.ubtStopRobotAction()

        print 'Robot stop motion'

 

#----------------------- block program end ----------------------                                                                                                                                 

RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                           

RobotApi.ubtRobotDeinitialize()

exit()