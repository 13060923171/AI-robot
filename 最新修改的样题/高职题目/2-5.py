#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter #导入Tkinter按钮组件
import tkMessageBox #导入Tkinter中常用的对话框控件(消息框)
import requests
import json
import time

put_bow = {
    "operation": "start",
    "motion": {
        "name": "bow",
        "repeat": 1,
        "speed": "slow"
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
# 上传图片
post_photo = {
    "resolution": "1280x800"
}


def resful_put(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url, data=data, headers=headers)
    return response.json()

def resful_post(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()

# 容器
top = Tkinter.Tk(className='RobotPane')
# 设置分辨率
top.geometry('100x200')

#封装函数，按钮鞠躬，与动作的执行
def bowCallBack():
    tkMessageBox.showinfo("鞠躬", "鞠躬")#窗口标题与button文本
    resful_put('motions',put_bow)#机器人执行的动作鞠躬
    time.sleep(5)
    resful_put('motions',reset_data)
#封装函数，按钮拍照，与动作的执行
def photoCallBack():
    tkMessageBox.showinfo("拍照", "拍照")
    resful_post('visions/photos',post_photo)#机器人执行的动作拍照
    time.sleep(1)

# w = Button(master按钮父容器，按钮文本，按钮被点击时执行的函数)
B = Tkinter.Button(top, text="鞠躬", command=bowCallBack)
B.pack()

C = Tkinter.Button(top, text="拍照", command=photoCallBack)
C.pack()

top.mainloop()
