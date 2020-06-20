#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import RobotApi
'''
流程说明：我们通过Yanshee读取环境温度值，当发现温度高于23摄氏度时说：“室温过高，准备打开风扇降温”，
同时发送UDP控制消息start给树莓派智能风扇设备服务器端。当读取环境温度值低于23°时说：“室温正常，准备关闭风扇”，
同时发送UDP控制消息stop给智能风扇服务器端完成关闭风扇动作。
'''

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

while True:

    time.sleep(2)

    ret = RobotApi.ubtReadSensorValue("environment",environment_sensor ,12)

    if ret !=0:

        print("Can not read Sensor value. Error code: %d"% (ret)) 

    else:

        print("Read Environment Sensor tempValue: %d "% (environment_sensor.iTempValue))

    temp = environment_sensor.iTempValue

    if temp > 23 :

        RobotApi.ubtVoiceTTS(1,"室温过高，准备打开风扇降温")

        message = "start"

    elif tmep < 23 :

        RobotApi.ubtVoiceTTS(1,"室温正常，准备关闭风扇")

        message = "stop"

    s.sendall(message) 

    data = s.recv(1024) 

    print data

 

s.close()

#----------------------- block program end ----------------------                                                                                                                                 

RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                           

RobotApi.ubtRobotDeinitialize()

exit()