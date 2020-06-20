#!/usr/bin/env python

#coding=utf-8

from picamera.array import PiRGBArray
from picamera import PiCamera
from functools import partial
import cv2
import os
import time
import threading
import numpy as np
import multiprocessing as mp
from socket import *
import RobotApi as api # 调用最新的机器人API

'''

 攻击方机器人通过颜色识别出红色机器人的位置包括左右位置和远近位置，然后作出相应的攻击策略，左边时左边出拳、右边时右边出拳。
 离得很近的时候出双拳并连续攻击，并配合多种语音互动效果，完成人类对打竞技PK的模拟过程。

'''
##############################

#Brief : Competitive robot demo 

#Version : "V1.0"

#Author :"Sanson"

#Date : "2018/08/21"

##############################

 

resX = 500

resY = 300

 

# Define HSV thresholds for various colors

lower_red = np.array([160, 40, 40])

upper_red = np.array([179, 255, 255])

lower_green = np.array([30, 100, 100])

upper_green = np.array([80, 255, 255])

lower_blue = np.array([100, 100, 100])

upper_blue = np.array([125, 255, 255])

lower_yellow = np.array([20, 30, 30])

upper_yellow = np.array([70, 255, 255])

 

 

xdeg = 90

tts_flag = 0

 

HOST = '127.0.0.1'

PORT = 20001

ADDR = (HOST, PORT)

 

udpCliSock = socket(AF_INET, SOCK_DGRAM)

# Setup the camera

camera = PiCamera()

camera.resolution = (resX, resY)

camera.framerate = 30

 

# Use this as our output

rawCapture = PiRGBArray(camera, size=(resX, resY))

 

def headangle(angle, ADDR):

    data = str("{\"cmd\":\"servo\",\"type\":\"write\",\"time\":10,\"angle\":\"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

    angle_hex = str(hex(angle))

    end = str("\"}")

    if(angle<16):

        hexdate=(data+"0"+angle_hex[-1]+end)

        udpCliSock.sendto(hexdate ,ADDR)

    else:

        udpCliSock.sendto(data + angle_hex[2] + angle_hex[3] + end ,ADDR)

def get_circles(img):

    x = 0

    y = 0

    radius = 0

    blurred = cv2.GaussianBlur(img, (11, 11), 0) # 高斯滤波

    # Convert color space to HSV

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) # BGR转HSV

    # Two value processing of pictures

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Corrosion operation

    mask = cv2.erode(mask, None, iterations=2)

    # Corrosion and expansion before filtering

    mask = cv2.dilate(mask, None, iterations=2)

    # Looking for outlines in figures

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # if have

    if len(cnts) > 0:

        # find the max outline

        c = max(cnts, key=cv2.contourArea)

        # Use the smallest circumscribed circle to draw the largest outline

        ((x, y), radius) = cv2.minEnclosingCircle(c)

 

    return int(x),int(y),int(radius),img

 

def draw_frame(img,x,y,z):

    global xdeg

    if(z > 15):

        cv2.circle(img,(x,y),z,(255,0,0),5)

        #cv2.rectangle(img,(i[0]-i[2],i[1]-i[2]),(i[0]+i[2],i[1]+i[2]),(255,255,0),5)

        print("circle_center is : ",x,y)

        print("radius is : ",z)

        #if(x < 250):

         #    xdeg -= 5

            #headangle(xdeg, ADDR)         

        #if(x > 250):

         #    xdeg += 5

            #headangle(xdeg, ADDR)

        #if(xdeg > 150):

         #    xdeg = 150

        #if(xdeg < 30):

         #    xdeg = 30

    cv2.imshow('Color_tracking', img)

 

def walk_track(x,y,z):

    global tts_flag

    if z > 20 :

         if(x < 150):

             api.ubtSetRobotMotion("walk", "left", 3,1)

             api.ubtStartRobotAction("reset",1)

         if(x > 350):

             api.ubtSetRobotMotion("walk", "right", 3,1)

             api.ubtStartRobotAction("reset",1)

         if x > 150 and x < 350:

             if tts_flag == 0:

                  api.ubtSetRobotMotion("wave", "both", 4,2)

                  api.ubtSetRobotMotion("raise", "both", 4,2)

                 api.ubtVoiceTTS(0, " hello guy,  I have found you wait me,I'll hit you!!")

                 tts_flag = 1

             if z > 20 and z < 120 :

                 api.ubtSetRobotMotion("walk", "front", 4,1)

                 api.ubtStartRobotAction("reset",1)

             if z > 120 :

                 if tts_flag == 1 :

                     api.ubtVoiceTTS(0, "HI HI guy ,I come here! I catch you!")

                     tts_flag = 2

                 if x < 250 :

                     api.ubtStartRobotAction("Left hits forward", 1)

                     if z > 140 :

                         #api.ubtStartRobotAction("Shoot left", 1)

                          api.ubtStartRobotAction("Hit left", 1)

                     if z > 180 :

                          api.ubtSetRobotMotion("stretch", "both", 4,2)

                 if x > 250 :

                     api.ubtStartRobotAction("Right hits forward", 1)

                     if z > 140 :

                         api.ubtStartRobotAction("Hit right", 1)

                     if z > 180 :

                          api.ubtSetRobotMotion("stretch", "both", 4,2)

             if z > 200 :

                 api.ubtSetRobotMotion("walk", "back", 2,2)

                 api.ubtStartRobotAction("reset",1)

 

if __name__ == '__main__':

   

    pool = mp.Pool(processes=4) # 进程池，4

    fcount = 0

 

    api.ubtRobotInitialize()

    api.ubtRobotConnect("sdk","1","127.0.0.1")

    #init head pose

    headangle(90, ADDR)

    print("Color_tracking start...:")

    api.ubtStartRobotAction("reset",1)

 

    camera.capture(rawCapture, format="bgr")

 

    r1 = pool.apply_async(get_circles, [rawCapture.array])

    r2 = pool.apply_async(get_circles, [rawCapture.array])

    r3 = pool.apply_async(get_circles, [rawCapture.array])

    r4 = pool.apply_async(get_circles, [rawCapture.array])

 

    x1,y1,z1, i1 = r1.get()

    x2,y2,z2, i2 = r2.get()

    x3,y3,z3, i3 = r3.get()

    x4,y4,z4, i4 = r4.get()

 

    rawCapture.truncate(0)

 

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array

 

        if fcount == 1:

            r1 = pool.apply_async(get_circles, [image])

            x2,y2,z2, i2 = r2.get()

            draw_frame(i2, x2,y2,z2)

 

        elif fcount == 2:

            r2 = pool.apply_async(get_circles, [image])

            x3,y3,z3, i3 = r3.get()

            draw_frame(i3, x3,y3,z3)

 

        elif fcount == 3:

            r3 = pool.apply_async(get_circles, [image])

            x4,y4,z4, i4 = r4.get()

            draw_frame(i4, x4,y4,z4)

             walk_track(x4,y4,z4)

 

        elif fcount == 4:

            r4 = pool.apply_async(get_circles, [image])

            x1,y1,z1, i1 = r1.get()

            draw_frame(i1, x1,y1,z1)

 

            fcount = 0

        fcount += 1

 

        rawCapture.truncate(0)

 

        key = cv2.waitKey(1) & 0xFF 

        # press 'q' to exit

        if key == ord('q'): 

            break

    # When everything done, release the capture

    camera.release()

    cv2.destroyAllWindows()