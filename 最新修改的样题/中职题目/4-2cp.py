#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 树莓派摄像头库获取视频流
from picamera.array import PiRGBArray
from picamera import PiCamera
import requests
import json
import time
import cv2
import threading

'''
通过物体识别的程序，当机器人发现宠物猫图片的时候用TTS提醒小朋友：
“发现宠物猫”并向前走两步之后挥手，同时闪烁胸前红灯实现和小朋友互动
这道题视频里面用到了模型caffe框架的moblenet，但是我这里尝试使用它的API看看能不能用物体识别识别出猫；
可以使用opencv自带的猫脸级联分类器。
'''
# 初始化摄像头，设置分辨率和帧率
camera = PiCamera()
camera.resolution = (450, 250)
camera.framerate = 30
# 将摄像头的视频流转换为数组
rawCapture = PiRGBArray(camera, size=(450, 250))
timestamp = int(time.time())

ttsdata = {
    "tts": "发现宠物猫",
    "interrupt": True,
    "timestamp": timestamp
}

handdata = {
    "operation": "start",
    "motion": {
        "name": "come on",
        "direction": "forward",
        "repeat": 1,
        "speed": "normal"
    },
    "timestamp": timestamp
}

leddata = {
    "type": "button",
    "color": "red",
    "mode": "on"
}

walkdata = {
    "operation": "start",
    "motion": {
        "name": "walk",
        "direction": "forward",
        "repeat": 2,
        "speed": "normal"
    },
    "timestamp": timestamp
}

reset_data = {
    "operation": "start",
    "motion": {
        "name": "reset",
        "repeat": 1
    },
    "timestamp": int(time.time())
}

def restful_put(model,data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type':'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url,headers=headers,data=data)
    return response.json()


def restful_get(model,params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type':'application/json'}
    response = requests.get(url=url,headers=headers,params=params)
    return response.json()

def FindCat():
    detector = cv2.CascadeClassifier("/home/pi/Desktop/opencv/haarcascade_frontalcatface.xml")

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # image 为每一帧用于检测猫脸
        image = frame.array
        grayimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # 检测detectMultiScale参数：图像；每次检测完后图像缩放比例，最少检测到4次才算成功；目标最小尺寸；
        rects = detector.detectMultiScale(grayimage, scaleFactor=1.0,minNeighbors=2,minSize=(10,10))

        #cv2.imshow('find_cat', image)
        # cv2.imshow('find_cat', rects)
        for (x,y,w,h) in rects:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(image,"Found face",(x,y-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
            if len(rects)>0:
                restful_put('voice/tts',ttsdata)
                time.sleep(1)
                restful_put('motions',walkdata)
                time.sleep(1)
                restful_put('motions',handdata)
                time.sleep(1)
                restful_put('devices/led',leddata)
                break

        #show frame
        cv2.imshow("find_cat",image)
        # 按'q'健退出循环
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break
        #wait for next frame
        rawCapture.truncate(0)
    # When everything done, release the capture
    camera.close()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    FindCat()
    a = restful_put('motions',reset_data)
    print a
    print "exit all task."
