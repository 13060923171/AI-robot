#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import RPi.GPIO as GPIO
from time import sleep

#UDP server init
HOST = '192.168.43.46' #change the ip of your rpi3
PORT = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
print('...waiting for yanshee is message')

#RPi GPIO init
#Ignore warning for now
GPIO.setwarnings(False)
#Use physical pin numbering
GPIO.setmode(GPIO.BOARD)
#set pin 12 to be an output pin and set initial value to low (off)
GPIO.setup(12,GPIO.OUT,initial = GPIO.LOW)
while True: #Run forever
    data,address = s.recvfrom(1024)
    print(data,address)
    if data == 'start':
        GPIO.output(12,GPIO.HIGH)#Turn on
        sleep(1)#Sleep for 1 second
        s.sendto('ok turn on fan',address)
        print('turn on fan')
    elif data == 'stop':
        GPIO.output(12,GPIO.LOW)#turn off
        sleep(1)#sleep for 1 second
        s.sendto('ok turn off fan', address)
        print('turn off fan')

