# RestfulAPI模板调用

```python
import requests
import json
import time
from __future__ import print_function

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
```

## 这里我定义了两个函数用于对机器人进行get/put请求，put需要传入模块url路径和参数，get只需要参数即可。还加了一个py2兼容py3的print写法。为了方便代码复用，可以将这个代码块添加到pycharm 的一个快速补全功能。到时只需要输入关键字tab补全即可。两个函数的返回值都是json格式的；