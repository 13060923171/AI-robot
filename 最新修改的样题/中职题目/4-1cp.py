#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import threading as th
import time
import json
import requests


def restful_get(model, params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type': 'application/json'}
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def restful_put(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type': 'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url, headers=headers, data=data)
    return response.json()


lower_red = np.array([160, 40, 40])
upper_red = np.array([180, 255, 255])
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([125, 255, 255])
lower_green = np.array([30, 100, 100])
upper_green = np.array([80, 255, 255])
x, y, z = 0, 0, 0

camera = PiCamera()
camera.resolution = (450, 250)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size=(450, 250))
timestamp = int(time.time())

left_hand = {
    "operation": "start",
    "motion": {
        "name": "raise",
        "direction": "left",
        "repeat": 1,
        "speed": "slow"
    },
    "timestamp": timestamp
}

right_hand = {
    "operation": "start",
    "motion": {
        "name": "raise",
        "direction": "right",
        "repeat": 1,
        "speed": "slow"
    },
    "timestamp": timestamp
}

yellow_led = {
    "type": "button",
    "color": "yellow",
    "mode": "on"
}

green_led = {
    "type": "button",
    "color": "green",
    "mode": "on"
}

reset_data = {
    "operation": "start",
    "motion": {
        "name": "reset",
        "repeat": 1
    },
    "timestamp": int(time.time())
}


def camera_thread():
    global x, y, z
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        cnts = cv2.findContours(mask.copy(), 0L, 2L)[0]  # mask.copy() maybe  equal mask
        if len(cnts) > 0:
            circle = max(cnts, key=cv2.contourArea)
            ((x,y), z) = cv2.minEnclosingCircle(circle)
            x = int(x)
            y = int(y)
            z = int(z)
            print '(x,y):(%d,%d)' % (x,y),'radius:',z
        if z > 15:
            cv2.circle(image, (x, y), z, (0, 255, 0), 5)
        cv2.imshow('color_ball', image)
        rawCapture.truncate(0)  # 清除流以准备下一帧
        print 'press key num:',cv2.waitKey(1) & 0xFF
        if cv2.waitKey(1) & 0xFF == ord("q"):# 相当于time.sleep(1ms)，任意键退出
            camera.close()
            break
    cv2.destroyAllWindows()


def track_thread():
    global x, y, z
    while 1:
        if z > 20:
            if x < 150:
                restful_put('motions', left_hand)
                restful_put('devices/led', yellow_led)
                time.sleep(2)
            else:
                restful_put('motions', right_hand)
                restful_put('devices/led', green_led)
                time.sleep(2)


if __name__ == '__main__':
    #camera.close()
    restful_put('motions',reset_data)
    
    restful_put('motions', reset_data)
    t1 = th.Thread(target=camera_thread, args=())
    t2 = th.Thread(target=track_thread, args=())

    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()

    t1.join()
    t2.join()

