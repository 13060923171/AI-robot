#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

from socket import *

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from time import sleep # Import the sleep function from the time module

 

#UDP server init

HOST = '10.10.64.207'#chang the IP of your Rpi3

PORT = 9999

s = socket(AF_INET,SOCK_DGRAM) 

s.bind((HOST,PORT))

print '...waiting for Yanshee\'s message..'

 

#RPI GPIO init

# Ignore warning for now

GPIO.setwarnings(False)

# Use physical pin numbering

GPIO.setmode(GPIO.BOARD)

# Set pin 12 to be an output pin and set initial value to low (off)

GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

 

while True: # Run forever

    data,address = s.recvfrom(1024)

    print data,address

    if data == "start" :

        GPIO.output(12, GPIO.HIGH) # Turn on

        sleep(1) # Sleep for 1 second

        s.sendto("OK Turn on Fan",address)

        print 'Turn on Fan'

    elif data == "stop" :

        GPIO.output(12, GPIO.LOW) # Turn off

        sleep(1) # Sleep for 1 second

        s.sendto("OK Turn off Fan",address)

        print 'Turn off Fan'