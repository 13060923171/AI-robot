#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import RobotApi
import time

HOST = '192.168.43.46' #change the ip of your rpi3
PORT = 9999

#----------robot init---------------
RobotApi.ubtRobotInitialize()
ret = RobotApi.ubtRobotConnect('sdk','1','127.0.0.1')
if (0!=ret):
    print('Error -->ubtRobotConnect return value: %d'%ret)
    exit(1)

#-------udp client init------------
s = socket(AF_INET,SOCK_DGRAM)
s.connect((HOST,PORT))
environment_sensor= RobotApi.UBTEDU_ROBOTENV_SENSOR_T()
while True:
    time.sleep(2)
    ret = RobotApi.ubtReadSensorValue('environment',environment_sensor, 12)
    if ret !=0:
        print('can not read sensor value. error code :%d'%(ret))
    else:
        print('read enviroment sensor temvalue :%d'%(environment_sensor.iTempValue))
    temp = environment_sensor.iTempValue
    if temp >23:
        RobotApi.ubtVoiceTTS(1,'室温过高，准备打开风扇减温')
        message = 'start'
    elif temp < 23:
        RobotApi.ubtVoiceTTS(1,'室温正常，准备关闭风扇')
        message = 'stop'
s.sendall(message)
data = s.recv(1024)
print(data)
s.close()
#--------------------block program end-----------------------
RobotApi.ubtRobotDisconnect('sdk','1','127.0.0.1')
RobotApi.ubtRobotDeinitialize()
exit()
