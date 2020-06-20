#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import *
import json
import requests
import time
import RPi.GPIO as GPIO

app = Flask(__name__)

put_bow = {
    "operation": "start",
    "motion": {
        "name": "bow",
        "repeat": 1,
        "speed": "very slow"
    },
    "timestamp": int(time.time())
}

reset_data = {
    "operation": "start",
    "motion": {
        "name": "reset",
        "repeat": 1
    },
    "timestamp": int(time.time())
}

ttsdata2 = {
      "tts": "主人再见",
      "interrupt": True,
      "timestamp": int(time.time())
}

post_streams = {
    "resolution" : "640x480"
}

def restful_get(model,params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url=url, headers=headers,params=params)
    return response.json()

def restful_put(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url, data=data, headers=headers)
    return response.json()

def restful_delete(model,params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url=url, headers=headers,params=params)
    return response.json()

def restful_post(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()

wenshidu = restful_get('sensors/environment')
ttsdata1 = {
      "tts": "欢迎回家已为您打开台灯祝您生活愉快,当前温度={0}度".format(wenshidu["data"]["environment"][0]["temperature"]),
      "interrupt": True,
      "timestamp": int(time.time())
}

GPIO.setwarnings(False)#定义GPIO数值
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if request.form.get('submit_button') == 'go home':
            restful_delete('visions/streams')
            print '关闭视频流成功'
            restful_put('motions',put_bow)
            time.sleep(5)
            restful_put('motions',reset_data)
            time.sleep(2)
            restful_put('voice/tts',ttsdata1)
            time.sleep(1)
            GPIO.output(8 , GPIO.HIGH)  # 开启灯泡
            time.sleep(1)
        elif request.form.get('submit_button') == 'leave':
            restful_post('visions/streams',post_streams)
            print '开启视频流成功'
            restful_put('voice/tts',ttsdata2)
            time.sleep(1)
            GPIO.output(8 , GPIO.LOW)  # 关闭灯泡
            time.sleep(1)
        else:
            pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0")