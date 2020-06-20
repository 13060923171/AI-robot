# <u>Tkinter 代码与拓展</u>

## Tkinter 代码

```python
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

def restful_get(model,params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url=url, headers=headers,params=params)
    return response.json()

def resful_post(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()

# 容器
top = Tkinter.Tk(className='机器人遥控器')
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
```

## Tkinter 可能的拓展

```python
#添加多个按钮以及多个动作
#添加拥抱动作
yongbao = {
    "operation": "start",
    "motion": {
        "name": "yongbao",
        "repeat": 1,
        "speed": "very slow"
    },
    "timestamp": int(time.time())
}

#封装函数，按钮拥抱，与动作的执行
def yongbaoCallBack():
    tkMessageBox.showinfo("拥抱", "拥抱")#窗口标题与button文本
    resful_put('motions',yongbao)#机器人执行的动作鞠躬
    time.sleep(1)

# 父容器，按钮文本，执行函数
A = Tkinter.Button(top, text="拥抱", command=yongbaoCallBack)
A.pack()
      
#添加查看温湿度按钮        
#封装函数，按钮查看，查看温湿度并播报
def wenshiduBack():
    wenshidu = resful_put('sensors/environment')
    ttsdata1 = {
      "tts": "大家好，当前温度={0}度".format(wenshidu["data"]["environment"][0]["temperature"]),
      "interrupt": True,
      "timestamp": int(time.time())
	}
    resful_put('voice/tts',ttsdata1)
    tkMessageBox.showinfo("查看温湿度","温度= {0} \n 湿度= {1}".format(wenshidu["data"]["environment"][0]["temperature"],wenshidu["data"]["environment"][0]["humidity"]))
    time.sleep(1)    
    
# 父容器，按钮文本，执行函数
D = Tkinter.Button(top, text="查看温湿度", command=wenshiduCallBack)
D.pack()
    

#语音
ttsdata = {
      "tts": "大家好，我是机器人",
      "interrupt": True,
      "timestamp": int(time.time())
}

#封装函数，按钮查看，查看语音播报
def ttsCallBack():
    tkMessageBox.showinfo("语音", "语音")
    resful_put('voice/tts',ttsdata)#机器人执行的动作语音
    time.sleep(1)
    
E = Tkinter.Button(top, text="语音", command=ttsCallBack)
E.pack()
```

