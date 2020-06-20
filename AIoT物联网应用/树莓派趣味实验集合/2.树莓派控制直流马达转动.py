import RPi.GPIO as GPIO
from time import sleep

# 一个6V直流电机;一个马达驱动芯片：L293D
'''

GPIO 25–Pin 22 > L293D–Pin 1
GPIO 24–Pin 18 > L293D–Pin 2
GPIO 23–Pin 16 > L293D–Pin 7
GND     –Pin 30 > L293D–Pin 5


'''
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()