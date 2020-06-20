# coding=utf-8
from flask import *
import time
import json
import requests

import RPi.GPIO as GPIO


reset_data = {
    "operation": "start",
    "motion": {
        "name": "reset",
    },
    "timestamp": int(time.time())
}
post_streams = {
    "resolution": "640x480"
}
both_hand_data = {
    "operation": "start",
    "motion": {
        "name": "raise",
        "direction": "both",
        "repeat": 2,
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
    "tts": "see you",
    "interrupt": True,
    "timestamp": int(time.time())
}
ttsdata1 = {
    "tts": "welcome",
    "interrupt": True,
    "timestamp": int(time.time())
}


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


def restful_delete(model, params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url=url, headers=headers, params=params)
    return response.json()


def restful_post(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()


app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, 0, initial=0)

name = ''
login = ''
angle = 90
temperature = 0


@app.route('/<int:id>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def hello_world(id=None):
    global name, login, angle, temperature
    if request.method == 'POST':
##        temperature = 28
        temperature = restful_get('sensors/environment')
        temperature = temperature["data"]["environment"][0]["temperature"]
        if id == 1:  # back home:light stream hand tts
            try:
                GPIO.output(8, 1)
                restful_delete('visions/streams')
                restful_put('motions', both_hand_data)
                time.sleep(1)
                restful_put('motions', reset_data)
                time.sleep(1)
                restful_put('voice/tts', ttsdata1)
##                print 'this is post111111'
                return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)
            except:
##                print 'please try again!'
                return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)

        if id == 2:  # out: off open_stream tts
            try:
                GPIO.output(8, 0)
                restful_post('visions/streams',post_streams)
                restful_put('motions', both_hand_data)
                time.sleep(1)
                restful_put('motions', reset_data)
                time.sleep(1)
                restful_put('voice/tts', ttsdata2)
##                print 'this is post222222'
                return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)
            except:
##                print 'please try again!'
                return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)

        if id == 3:  # set NeckLR angle
            try:
                if request.form.get('points'):
                    angle = int(request.form.get('points'))
##                    print angle
                    NeckLR_data = {
                        "angles": {
                            "NeckLR": angle
                        }
                    }
                    restful_put('servos/angles', NeckLR_data)
                    # print type(angle)  # <type 'unicode'> 你好
##                print 'this is post33333'
                return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)
            except:
##                print 'please try again!'
                return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)

        if request.form.get('account') == 'admin' and request.form.get('pwd') == 'admin':
            login = 'success'
            name = 'admin'
##            print 'login success!'
            return render_template('hello.html', name=name, login=login, angle=angle, temperature=temperature)
        else:
##            print 'login fail!'
            login = 'fail'

    return render_template('login.html', login=login)
