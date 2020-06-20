#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time
import RPi.GPIO as GPIO

'''
当主人回到家里，机器人通过人脸识别发现主人回来了，就启动风扇（或台灯）。
并对主人说：“欢迎您回家，已为您打开风扇（或台灯），祝您生活愉快”
人脸样本采集使用block自带的功能，好像采集后不能关block；
如果样本不能使用block上传就使用API上传一张人脸图片样本，再设置样本标签即名字 LBW
'''


def resful_put(API, param):
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    param = param
    json_data = json.dumps(param)
    response = requests.put(url=motion_url, data=json_data, headers=headers)
    # print (response.content)
    return response.json()


def restful_get(API):
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url=motion_url, headers=headers)
    # print (response.content)
    return response.json()

def restful_get_vision(API,option,type):
    
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    params = {
        "option":"%s" % option,
        "type":"%s" % type
        }
    response = requests.get(url=motion_url, headers=headers,params=params)
    # print (response.content)
    return response.json()

seedata_start = {
    "type": "recognition",
    "operation": "start",
    "option": "face",
    "timestamp": int(time.time())
}

seedata_stop = {
    "type": "recognition",
    "operation": "stop",
    "option": "face",
    "timestamp": int(time.time())
}

ttsdata = {
    "tts": "欢迎您回家已为您打开风扇或台灯祝您生活愉快",
    "interrupt": True,
    "timestamp": int(time.time())
}

resful_put('visions', seedata_start)  # 开始人脸识别，人脸样本若存在就返回string的name,例如是LBW
GPIO.setwarnings(False)#定义GPIO数值
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)

while True:
    response = restful_get_vision('visions','face','recognition')  # 获取人脸识别结果
    try:
        if response['data']['recognition']['name'] == 'LBW':
            resful_put('visions', seedata_stop)  # 停止人脸识别
            GPIO.output(8 , GPIO.HIGH)  # 开启风扇
            time.sleep(1)
            resful_put('voice/tts', ttsdata)
            break
    except:
        print("face error!")
