#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera.array import PiRGBArray
from picamera import PiCamera

import cv2
import os
import time
import threading
import numpy as np
import multiprocessing as mp
import RobotApi

resX = 450
resY = 250

#Setup the camera
camera = PiCamera()
camera.resolution = (resX,resY)
camera.framerate =30

#Use this as our output
rawCapture = PiRGBArray(camera,size=(resX,resY))

RobotApi.ubtRobotInitialize()
RobotApi.ubtRobotConnect('SDK','1','127.0.0.1')

def find_cat():
    res = os.popen('./MobileNetSSDNS image/test.jpg')
    res = res.read()
    for line in res.splitlines():
        #print line
        result = line.split(':')[-1:]
        if result[0] == 'cat':
            print('ok i find cat')
            RobotApi.ubtSetRobotMotion('walk','front',2,1)
            RobotApi.ubtStartRobotAction('reset',1)
        else:
            print('Dont find Cat......')
def camera_thread():
    print('camera_thread run')
    for frame in camera.capture_continuous(rawCapture,format='bgr',use_port=True):
        img = frame.array
        cv2.imwrite('image/test.jpg',img)
        cv2.imshow('Find_cat',img)
        rawCapture.truncate(0)
        key = cv2.waitKey(1) & 0XFF
        if key == ord('q'):
            break
    # when everything done, release the capture
    cv2.destroyAllWindows()

def find_thread():
    print('find_thread run')
    while True:
        find_cat()
        time.sleep(2)

if __name__ == '__main__':
    RobotApi.ubtStartRobotAction('reset',1)
    threads = []
    t1 = threading.Thread(target=camera_thread(),args=())
    threads.append(t1)
    t2 = threading.Thread(target=find_thread(),args=())
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()