#!/usr/bin/python

# -*- coding: utf-8 -*-

# 我们使用Python语言来控制机器人做举左手动作
# GET用来获取资源，POST用来新建资源（也可以用于更新资源），PUT用来更新资源，DELETE用来删除资源。
'''
总结一下什么是RESTful架构：

（1）每一个URI代表一种资源；

（2）客户端和服务器之间，传递这种资源的某种表现层；

（3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。
'''

import requests

import json

import time

 

def set_motion():

    timestamp = int(time.time()) # 时间整数

    motion_url = "http://10.10.64.77:9090/v1/motions" #请求url

    headers={'Content-Type':'application/json'} # 请求头
    # 参数
    param={

        "operation": "start",

        "motion": {

        "name": "raise",

        "direction": "left",

        "repeat": 1,

        "speed": "normal"

        },

        "timestamp": timestamp

    }

    json_data = json.dumps(param) # 将参数转换为json格式

    response=requests.put(url=motion_url,data=json_data, headers=headers) # put更新资源,传入请求url，json请求参数，请求头

    print (response.content) # 打印响应文本

if __name__ == '__main__':

    set_motion()