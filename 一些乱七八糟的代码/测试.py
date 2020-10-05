#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time


def resful_put(API, param):
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    param = param
    json_data = json.dumps(param)
    response = requests.put(url=motion_url, data=json_data, headers=headers)
    return response.json()


def resful_post(API, param):
    url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    param = param
    json_data = json.dumps(param)
    response = requests.post(url=url, data=json_data, headers=headers)
    return response.json()

put_walk = {
    "motion": {
        "direction": "forward",
        "name": "walk",
        "repeat": 5,
        "speed": "fast"
    },
    "operation": "start",
    "timestamp": int(time.time())
}
put_come_on = {
    "motion": {
        "direction": "left",
        "name": "come on",
        "repeat": 2,
        "speed": "normal"
    },
    "operation": "start",
    "timestamp": int(time.time())
}
put_bow = {
    "motion": {
        "name": "bow",
        "repeat": 1,
        "speed": "very slow"
    },
    "operation": "start",
    "timestamp": int(time.time())
}
put_stop = {
    "motion": {
        "name": "stop",
        "repeat": 1,
        "speed": "normal"
    },
    "operation": "start",
    "timestamp": int(time.time())
}

post_tts = {
    'file': '3.mp3'
}

put_tts = {
    "operation": "start",
    "name": "fuqing.m4a"
}
if __name__ == '__main__':
    # 上传音频

#   resful_post('media/music', post_tts)
    resful_put('motions',put_walk)
    time.sleep(9)
    resful_put('motions',put_come_on)
    time.sleep(5)
    # 播放音乐
    resful_put('media/music', put_tts)
    resful_put('motions',put_bow)
    time.sleep(5)
    resful_put('motions',put_stop)
