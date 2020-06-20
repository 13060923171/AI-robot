#!/usr/bin/env python

# -*- coding: utf-8 -*-

# 本案例试图通过Yanshee的远程控制指令来完成对树莓派智能灯的开灯、关灯和闪灯等行为
# 树莓派智能灯端 代码
# 我们分别从终端输入 start 、 stop 、 flash来完成智能灯的开始、停止、闪烁三种状态的控制，并通过Yanshee读出当前指令的内容。然后输入exit退出。

from socket import *

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from time import sleep # Import the sleep function from the time module

 

#UDP server init

HOST = '10.10.64.207'#chang the IP of your Rpi3

PORT = 9999

s = socket(AF_INET,SOCK_DGRAM) 

s.bind((HOST,PORT))

print '...waiting for Yanshee message..'

 

#RPI GPIO init

# Ignore warning for now

GPIO.setwarnings(False)

# Use physical pin numbering

GPIO.setmode(GPIO.BOARD)

# Set pin 8 to be an output pin and set initial value to low (off)

GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

 

while True: # Run forever

    data,address = s.recvfrom(1024)

    print data,address

    if data == "start" :

        GPIO.output(8, GPIO.HIGH) # Turn on#

        sleep(1) # Sleep for 1 second

        s.sendto("OK Turn on LED",address)

        print 'Turn on LED'

    elif data == "stop" :

        GPIO.output(8, GPIO.LOW) # Turn off

        sleep(1) # Sleep for 1 second

        s.sendto("OK Turn off LED",address)

        print 'Turn off LED'

    elif data == "flash" :

        print 'Flash LED'

        s.sendto("OK Flash LED already",address)

    for i in range (3):

        GPIO.output(8, GPIO.LOW)

        sleep(0.5) # Sleep for 0.5 second

        GPIO.output(8, GPIO.HIGH)