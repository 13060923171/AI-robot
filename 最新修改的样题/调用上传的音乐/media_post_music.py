#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time


def resful_put(API, param):
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    param = param
    json_data = json.dumps(param)
    response = requests.put(url=motion_url, data=json_data, headers=headers)
    # print (response.content)
    return response.json()


def resful_post(API, param):
    timestamp = int(time.time())
    url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    param = param
    json_data = json.dumps(param)
    response = requests.post(url=url, data=json_data, headers=headers)
    # print (response.content)
    return response.json()


def restful_get(API):
    timestamp = int(time.time())
    motion_url = "http://127.0.0.1:9090/v1/{0}".format(API)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url=motion_url, headers=headers)
    # print (response.content)
    return response.json()


post_tts = {
    'file': 'ys.mp3'
}

put_tts = {
    "operation": "start",
    "name": "ys.mp3"
}
if __name__ == '__main__':
    # 上传音频
    #resful_post('Desktop/ys',post_tts)
    # 播放音乐
    a = resful_put('media/music',put_tts)
    print a

