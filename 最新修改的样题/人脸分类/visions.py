#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time




def resful_put(API,param):
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers={'Content-Type':'application/json'}
    param= param
    json_data = json.dumps(param)
    response=requests.put(url=motion_url,data=json_data, headers=headers)
    #print (response.content)
    return  response.json()


def restful_get(API):
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers={'Content-Type':'application/json'}
    response=requests.get(url=motion_url,headers=headers)
    #print (response.content)
    return  response.json()


# option :  face(age、gender、age_group（小孩，老人？）、quantity、expression、recognition)
#           object(recognition) 物体识别
#           color(color_detect) 颜色识别
def restful_get_visions(API, option, type):
    timestamp = int(time.time())
    params= {
        'option':'%s' % option,
        'type':'%s' % type
    }
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(params=params,url=motion_url, headers=headers)
    # print (response.content)
    return response.json()

# type:
# face(tracking,age、gender、age_group（小朋友？，老人？）、quantity、expression、recognition)
# object(recognition) 物体识别
# color(color_detect) 颜色识别
# 组合和get一致。
seedata_start = {
    "type": "recognition",
    "operation": "start",
    "option": "object",
    "timestamp": int(time.time())
}

seedata_stop = {
    "type": "recognition",
    "operation": "stop",
    "option": "object",
    "timestamp": int(time.time())
}

resful_put('visions', seedata_start)  # 开始人脸识别，人脸样本若存在就返回string的name,例如是LBW

time.sleep(5)
response = restful_get_visions\
        ('visions', option='object', type='recognition')  # 获取人脸识别结果

print response
resful_put('visions', seedata_stop)
'''
while True:
    response = restful_get_visions\
        ('visions', option='face', type='recognition')  # 获取人脸识别结果

    # 判断条件 analysis(age、group、gender、expression) recognition(name)、quantity
    # color(name)
    if response['data']['recognition']['name'] == 'LBW':
        resful_put('visions', seedata_stop)  # 停止人脸识别
        time.sleep(1)
        break
'''
