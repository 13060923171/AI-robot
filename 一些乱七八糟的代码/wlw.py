#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import picamera
import cv2
import numpy
import time
import RPi.GPIO as GPIO
import RobotApi as api

#init robot api
api.ubtRobotInitalize()
ret = api.ubtRobotConnect("SDK","1","127.0.0.1")

#GPIO setting for fan control
GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BOARD)#use physical pin numbering
#Set pin 16 to be an ouput pin and set initial value to high
GPIO.setup(16,GPIO.OUT,inital = GPIO.LOW)

#get the picture and found face
while True:
    #create a memory stream so photos does not need to be saved in a file
    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
            camera.resolution = (320,240)
            camera.capture(stream,format= 'jpeg')
    #convert the picture into a numpy array
    buff= numpy.fromstring(stream.getvalue(),dtype=numpy.uint8)
    #Now creates an OpenCV image
    image = cv2.imdecode(buff,1)
    #Load a cascade file for detecting faces
    face_cascade= cv2.CascadeClassifier('/usr/share/opencv/haarrcascades/haarcascade_frontalface_alt.xml')
    #convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    print('Found'+str(len(faces))+'face(s)')
    #draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    #Save the result image
    cv2.imwrite('result.jpg',image)
    isInterrputed =1
    #if found face turn on the fan
    if len(faces) > 0:
        GPIO.output(16,GPIO.HIGH)#Turn on

        api.ubtStartRobotAction('reset',1)
    else:
        GPIO.output(16,GPIO.LOW)
    time.sleep(2)
#--------------------Disconnect-----------------------
api.ubtRobotDisconnect('SDK','1','127.0.0.1')
api.ubtRobotDeinitialize()