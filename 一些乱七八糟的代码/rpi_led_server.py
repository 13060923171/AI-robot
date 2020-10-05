#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import RPi.GPIO as GPIO #import Raspberry Pi gpio library
from time import sleep # import the sleep function from the time module

#UDP server init
HOST = '10.10.64.207' #change the ip of your rpi3
PORT = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
print('...waiting for Yanshee message..')

#PRI GPIO init
#Ignore warning for now
GPIO.setwarnings(False)
#Use physical pin numbering
GPIO.setmode(GPIO.BOARD)
#set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)

while True: # run forever
    data,address = s.recvfrom(1024)
    print(data,address)
    if data == 'start':
        GPIO.output(8,GPIO.HIGH)#Turn off
        sleep(1) #Sleep for 1 second
        s.sendto('ok turn on led',address)
        print('turn on led')
    elif data == 'stop':
        GPIO.output(8,GPIO.LOW) #Turn off
        sleep(1) #Sleep for 1 second
        s.sendto('ok turn off led',address)
        print('turn off led')
    elif data == 'flash':
        print('flash led')
        s.sendto('ok flash led already',address)
        for i in range(3):
            GPIO.output(8,GPIO.LOW)
            sleep(0.5) #sleep for 0.5 second
            GPIO.output(8,GPIO.HIGH)

