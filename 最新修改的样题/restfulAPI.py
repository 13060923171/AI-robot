#!usr/bin/env python
# coding=utf-8

import time
import json
import requests

def restful_get(model,params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type':'application/json'}
    response = requests.get(url=url,headers=headers,params=params)
    return response.json()


def restful_put(model,data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type':'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url,headers=headers,data=data)
    return response.json()

hand_data ={
  "motion": {
    "direction": "left",
    "name": "raise",
    "repeat": 1,
    "speed": "normal"
  },
  "operation": "start",
  "timestamp": int(time.time())
}

version_data = {
	"type":"core"
}

#a = restful_put('motions',hand_data)
#a = restful_get('devices/versions',version_data)
#a = restful_get('motions/list')
#print a


