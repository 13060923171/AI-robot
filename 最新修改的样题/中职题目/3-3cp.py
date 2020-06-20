#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time

'''
测试机器人摔倒后爬起的动作；
首先查询所有舵机的角度值；主要查看腿部舵机角度
通过改变机器人腿部舵机角度让机器人站起来；
'''

ttsdata = {
    "tts": "哎呀不小心摔倒了没有人看到吧",
    "interrupt": True,
    "timestamp": int(time.time())
}
# 向后倒，向前爬起；如果向前倒，向后爬起name为GetupRear；还有一个reset动作不知道是什么
getup_data = {
    "operation": "start",
    "motion": {
        "name": "GetupFront",
        "repeat": 1
    },
    "timestamp": int(time.time())
}


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


while 1:
    angles = restful_get('servos/angles')
    print(angles)
    response = restful_get('sensors/gyro')
    print(response['data']['gyro'][0]['euler-x'])  # 查询欧拉角x
    eulerX = response['data']['gyro'][0]['euler-x']  # 欧拉X角
    if eulerX >= 140:
        resful_put('voice/tts', ttsdata)
        time.sleep(1)
        resful_put('motions', getup_data)
        break
