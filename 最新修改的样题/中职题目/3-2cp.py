#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import openadk
import time
import requests
import json
#from __future__ import print_function

'''
当机器人发现手动安装在身上的触摸传感器被触摸的时候，
机器人说：很高兴认识你人类朋友。并作举左手示意动作
0 （未触摸）
1 （触摸btn1）
2 （触摸btn2）
3 （触摸两边）
'''

movedata = {
    "operation": "start",
    "motion": {
        "name": "raise",
        "direction": "left",
        "repeat": 3,
        "speed": "normal"
    },
    "timestamp": int(time.time())
}

ttsdata = {
    "interrupt": True,
    "timestamp": 1551838515,
    "tts": "很高兴认识你人类朋友"
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


# 这里不知道要不要使用while循环，
while True:
    time.sleep(1)
    # 获取所有传感器的列表。在调用传感器模块是用于刷新传感器
    # rbsen_response = restful_get('sensors/list') # 传回传感器id和槽位，如果需要传参就要获取id和slot槽位
    # print(rbsen_response)
    print('touch me !')
    # response = rbsen.get_sensors_touch(id=id,slot=slot) # 传感器id、slot两个参数可以不填，不知道会不会自动检测。
    response = restful_get('sensors/touch')  # 传感器id、slot两个参数可以不填，不知道会不会自动检测。
    touch_value = response['data']['touch'][0]['value']  # 返回表示触摸状态值
    if touch_value >= 1:
        resful_put('voice/tts', ttsdata)
        time.sleep(1)
        resful_put('motions', movedata)
        break
