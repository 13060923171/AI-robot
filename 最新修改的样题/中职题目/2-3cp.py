# !/usr/bin/env python
# coding=utf-8

# 通过APP回读编程部分，编辑机器人拥抱动作，并发送给机器人。在机器人桌面端用python编程通过SDK方法调用该动作

# 动作文件可以在pad上设置好后上传机器人，这样机器人本地就有自定义的运动hts文件yongbao

import time
import requests
import json


# 回读的动作参数可能没有direction和speed
data = {
      "operation": "start",
      "motion": {
        "name": "yongbao",
        "repeat": 1,
      },
      "timestamp": int(time.time())
}
'''
{
      "operation": "start",
      "motion": {
        "name": "yongbao",
        "direction": "both",
        "repeat": 1,
        "speed": "normal"
      },
      "timestamp": int(time.time())
}
'''

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


resful_put('motions',data)
#rb.put_motions(data) 
# rb.put_motions(body=data) # 指定body，不指定应该也可以

