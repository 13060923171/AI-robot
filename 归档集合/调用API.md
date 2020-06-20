# [快速导航](https://gitee.com/robot_preparation/code)

**补充这篇md的有些代码可能有bug，例如视觉识别获取任务结果哪里，需要开启任务后才能去获取结果；没有任务就获取不了结果；而且更正一下这里的API又被叫做YanADK好像并不是RestfulAPI（这个是json和requests库）两个传参都是json比较类似。**

# 调用API

按步骤应该准备好API文档，可以在机器人上显示，理论上也可以远程登录显示将127.0.0.1换成机器人的IP就可以了，如果方便的话可以在PC上显示，PC上查看文档+编程，效率会高一些。

# API调用模板及规律

首先我们来看官方给的[教程](http://yandev.ubtrobot.com/#/zh/api),里面有python实现的实例代码，如果在机器人内部查看的[文档](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0#/voice/putVoiceTTS)应该是这样的;也就是机器人不会提供代码示例，但是提供参数。

```python
# !/usr/bin/env python
# coding=utf-8

from __future__ import print_statement # 让print可以带括号即py3写法
import time # 生成时间戳
import openadk # 机器人Restful API 库
from openadk.rest import ApiException # 可省略，机器异常处理
from pprint import pprint # 可省略

timestamp = int(time.time()) # Unix时间戳，json里面的timestamp
print(timestamp) # 1590141538
# 实例化API中的动作对象,例如动作的是MotionsApi，一般是首字母大写后加Api
api_instance = openadk.MotionsApi()
# body =  # MotionsOperation | 运动控制的参数
body =  {
        "operation": "start",
        "motion": {
            "name": "raise",
            "direction": "left",
            "repeat": 1,
            "speed": "normal"
        },
        "timestamp": timestamp
        }

try:
    # 调用API实例对象的运动控制方法，put_motions 传入json格式参数
    api_response = api_instance.put_motions(body)
    pprint(api_response) # 0 表示成功
except ApiException as e:
    # 机器人内置的异常处理机制，可以不导入直接expect
    print("Exception when calling MotionsApi->putMotions: %s\n" % e)
```

上面这个是官网的示例，主要流程就是 

  1. 导入API库openadk

  2. 实例化一个api对象，例如要调用语音API的`rb = openadk.VoiceApi()`实例化对象的类名有个命名规律就是**首字母大写+Api**；再举个例子实例化传感器的API`rb = openadk.SensorApi()`;

  3. 设定每个API方法的参数，就是上面的body，是个JSON（可以理解为python的字典）；这个内部文档有示例，**所以我们可以把它复制过来到pycharm上节约时间，前提是我们在远程打开了机器人的API文档**。有些函数要的参数比较复杂，种类有限制，我觉得掌握常用的几个就可以了。例如我们要实现人脸追踪可以直接调用视觉的API:

     ```python
     # !/usr/bin/env python
     # coding=utf-8
     
     from __future__ import print_statement
     import time
     import openadk
     from openadk.rest import ApiException
     from pprint import pprint
     
     timestamp = int(time.time())
     # create an instance of the API class
     api_instance = openadk.VisionsApi()
     # tracking 追踪，这是人脸追踪的json
     body ={
       "type": "tracking",
       "operation": "start",
       "option": "face",
       "timestamp": timestamp
     }
     '''
     tracking
     recognition 识别 可以人脸/颜色
     gender 性别识别
     age_group 年龄识别
     quantity 
     color_detect 颜色识别
     age
     expression 表情识别
     '''
     
     try:
         # 指定视觉任务停止或开始
         # 命名规律是put请求方式_下划线分隔小写单词
         # 例如POST/visions​/streams打开摄像头的视频流
         # ​按照规律就是 post_visions_​streams()
         api_response = api_instance.put_visions(body)
         pprint(api_response)
     except ApiException as e:
         print("Exception when calling VisionsApi->putVisions: %s\n" % e)
     ```

     上面以PUT更新资源的方式调用视觉API的开启人脸追踪任务，我们不用再使用GET方式取得任务的返回结果，理论上人脸追踪是没有一个固定的返回结果的，就就是打开一个窗口显示追踪到的人脸，所以在GET取得任务返回结果里面找不到人脸追踪的类型；但是如果我们开启了人脸数量检测quantity，那么就需要使用GET方法取得结果。例如我们获取人脸的数量检测任务的结果。当然前提是有开启这个任务。

     ```python
     # !/usr/bin/env python
     # coding=utf-8
     from __future__ import print_statement
     import time
     import openadk
     from openadk.rest import ApiException
     from pprint import pprint
     
     # create an instance of the API class
     api_instance = openadk.VisionsApi()
     option = option_example # String | 模型名 (optional) 有face、color、object
     type = type_example # String | 任务名称 (optional) age/gender/quantity...
     
     try:
         # 获取任务結果
         api_response = api_instance.get_vision(option=option, type=type)
         pprint(api_response)
     except ApiException as e:
         print("Exception when calling VisionsApi->getVision: %s\n" % e)
     ```

# API简化写法

为了更方便调用API，我们可以省去一些不必要的代码，下面我将一些不影响功能的模块去掉，以语音TTS播报为例：

```python
# !/usr/bin/env python
# coding=utf-8
import time
import openadk

rb = openadk.VoiceApi()

data = {
  "tts": "你好，我是Yanshee",
  "interrupt": True,
  "timestamp": int(time.time())
}
rb.put_voice_tts(data) # 不返回响应码


```

这样既实用又简洁好记。只要记得实例化的类名命名规律和调用对应方法的命名规律就可以看着API文档实现对机器人的控制。更简单的实现颜色识别、运动控制、传感器读取、语音识别。在之后的模型部署和场景设计亦或者通信设计就可以更方便的使用API配合。



# 补充

之前我们的代码没有使用到最新版的API，所以对编程这块我们依赖Block编程，但是这个API如果可以有文档参考的的话还是很简单的调用，我们接下来应该熟练掌握调用常用的几个API例如视觉识别的，之前用opencv做的项目其实都不用自己写代码了，直接调用API即可。我打算把一些常用的项目通过API来实现，例如什么人脸数量检测、人脸年龄检测、人脸表情检测、人脸识别、颜色识别、追踪颜色小球、读取传感器数据。。。一些常用的API代码可以参照上面的方法来实现。到时我们就可以拿这些代码回学校后在机器人上验证就行了。可以把更多的时间放在后边的深度学习以及场景搭建方面。

# 下一篇：[待验证样题](https://gitee.com/robot_preparation/code/blob/master/%E5%BD%92%E6%A1%A3%E9%9B%86%E5%90%88/%E6%A0%B7%E9%A2%98%E9%93%BE%E6%8E%A5.md)