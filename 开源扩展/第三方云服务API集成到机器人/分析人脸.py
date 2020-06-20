# -*- coding: utf-8 -*-

import urllib2

import urllib

import time

import json

from picamera import PiCamera

from socket import * # 套接字模块 sendto发送数据

# 我们将Face++云服务端返回的jason数据包，解析出来对人脸进行了数据分析包括年龄、性别、情绪等多个维度的信息分析。
# 通过TTS播报功能把人脸分析的情绪结果通过Yanshee机器人播报出来，同时我们还点亮了头部灯光为绿色，增加了灯光效果。
# 其中调用URL为 https://api-cn.faceplusplus.com/facepp/v3/detect

 

################################

#   Version = " 1.5 "          #

#   Date  = " 2018/05/07 "     #

#   Author = " Sanson Li "     #

################################

 

 

http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
# face++请求API
key = "z-YCP40foHXX2QN8YCBbmfCy-yhm_K22"

secret = "ApWF7q5723dqBQOVPctG8I8zeB6dGDRy"

attr = "gender,age,emotion,smiling,glass" # 属性

 

#get a picture首先我们可以通过pi camera库来拍一张人脸的照片。并命名为：analyse.jpg

camera = PiCamera()

camera.resolution = (1024, 768)

camera.start_preview()

time.sleep(5)

camera.capture('/mnt/1xrobot/tmp/analyse.jpg')

camera.stop_preview()

 

 

HOST = '127.0.0.1'

PORT = 20001

ADDR = (HOST, PORT) # 地址是个包含ip和端口的元组

udpCliSock = socket(AF_INET, SOCK_DGRAM) # 创建一个udp socket ；网络套接字是IP地址与端口的组合

 
# 接着我们定义了一个控制Yanshee机器人头部灯颜色的函数接口，我们默认打开为绿色。也即：当分析人脸时，我们让机器人头部眼睛灯光发出绿色。
def head_led_turn_on():   

    data = str("{\"cmd\":\"set\",\"type\":\"led\",\"para\":{\"type\":\"camera\",\"mode\":\"on\",\"color\":\"red\"}}")

    udpCliSock.sendto(data ,ADDR) # sendto发送数据

 

def head_led_turn_off():   # parameter参数para

    data = str("{\"cmd\":\"set\",\"type\":\"led\",\"para\":{\"type\":\"camera\",\"mode\":\"on\",\"color\":\"blue\"}}")

    udpCliSock.sendto(data ,ADDR)

 

#use tts to speak然后我们编写一个Yanshee机器人调用TTS语音播报的接口函数，用于播放人脸情绪结果和相应的情景组合语句

def tts_speak(content):

 

    time.sleep(1)

    link = str("{\"cmd\":\"connect\",\"account\":\"test123456\",\"port\":9002}")

    udpCliSock.sendto(link, ADDR)

   

    data = str("{\"cmd\":\"voice\",\"type\":\"tts\",\"data\":\"")

    end = str("\"}")

   

    udpCliSock.sendto(data+content+end ,ADDR)

    #print(data +content+end)

   

#give a path 最后我们引用face++需要的python数据结构体（data列表），完成face++ API库调用

filepath = r"/mnt/1xrobot/tmp/analyse.jpg"

boundary = '----------%s' % hex(int(time.time() * 1000)) # 时间16进制

data = []

data.append('--%s' % boundary)

data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key') # API应用名

data.append(key)

data.append('--%s' % boundary)

data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret') # API应用密码

data.append(secret)

data.append('--%s' % boundary)

fr=open(filepath,'rb') # 二进制读取图片

data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file') # 图片

data.append('Content-Type: %s\r\n' % 'application/octet-stream')

data.append(fr.read()) # 图片二进制数据

fr.close()

 

#add attr for face 属性 gender,age,emotion,smiling,glass 年龄、性别、情绪等

data.append('--%s' % boundary)

data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')

data.append(attr)

 

data.append('--%s--\r\n' % boundary)

 

http_body='\r\n'.join(data) # 请求要发送的数据，终于整完了、、、

#buld http request

req=urllib2.Request(http_url) # 请求url

#header

req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary) # 请求头

req.add_data(http_body) # 请求发送的数据

 

 

head_led_turn_on() # 亮灯

content_val = str("处理中 请稍等")

tts_speak(content_val) # 语音播报

 

try:

    #req.add_header('Referer','http://remotserver.com/')

         #post data to server

         resp = urllib2.urlopen(req, timeout=5) # 返回结果;响应头

         #get response

         qrcont=resp.read()

         #print qrcont

         parsed = json.loads(qrcont) # 解析响应以json格式输出

 

         facenum=len(parsed['faces']) # 人脸数，json里面的faces参数

       

         if facenum > 0 :

            print "发现%s个人脸" %(facenum)

            print "gender = %s" %(parsed['faces'][0]['attributes']['gender']['value'])

            print "age = %s" %(parsed['faces'][0]['attributes']['age']['value'])

            print "smile = %s" %(parsed['faces'][0]['attributes']['smile']['value'])

            #print "glass = %s" %(parsed['faces'][0]['attributes']['glass']['value'])

            print "happiness = %s" %(parsed['faces'][0]['attributes']['emotion']['happiness'])

            print "surprise = %s" %(parsed['faces'][0]['attributes']['emotion']['surprise'])

            print "anger = %s" %(parsed['faces'][0]['attributes']['emotion']['anger'])

            print "sadness = %s" %(parsed['faces'][0]['attributes']['emotion']['sadness'])

 

            gender = parsed['faces'][0]['attributes']['gender']['value']

            age = parsed['faces'][0]['attributes']['age']['value']

            smile = parsed['faces'][0]['attributes']['smile']['value']

            happiness = parsed['faces'][0]['attributes']['emotion']['happiness']

            surprise = parsed['faces'][0]['attributes']['emotion']['surprise']

            anger = parsed['faces'][0]['attributes']['emotion']['anger']

            sadness = parsed['faces'][0]['attributes']['emotion']['sadness']

            neutral = parsed['faces'][0]['attributes']['emotion']['neutral']

            disgust = parsed['faces'][0]['attributes']['emotion']['disgust']

            fear = parsed['faces'][0]['attributes']['emotion']['fear']

 

           

            ageval = int(age)

           

            content_val1=str("")

            content_val2=str("")

            content_val3=str("")

            content_val4=str("")

            content_val5=str("")

            content_val6=str("")

            content_val7=str("")

           

            if ageval >0 and ageval< 7 :

                if gender =="Male" :

                    content_val1 = str("你好萌萌哒 你是个乖宝宝还是个捣蛋鬼呢 ")

                else :

                    content_val1 = str("你好萌萌哒 你是个乖宝宝还是个捣蛋鬼呢 ")

                   

                content_val2 = str("你大概年龄%d岁 " % int(float(age)))

               

                if float(smile) > 30 :

                    content_val3 = str("笑的那么灿烂啊 ")

                  

                if float(anger) > 30 :

                    content_val4 = str("你生气了要乖乖听话哦 ")

                   

                if float(surprise) > 30 :

                    content_val5 = str("那么惊讶啊被我吓到了吗 ")

                   

                tts_speak(content_val1+content_val2+content_val3+content_val4+content_val5)

               

            elif ageval >18 and ageval<55:

               

                if gender =="Male" :

                    content_val1 = str("帅哥你好 ")

                else :

                    content_val1 = str("美女你好 ")

                   

                content_val2 = str("你大概年龄%d岁 " % int(float(age)))

               

                if float(smile) > 30 and float(smile) < 50 :

                    content_val3 = str("你的微笑让我很温暖 ")

                elif float(smile) > 50 :

                    content_val3 = str("笑的那么灿烂啊你看起来很开心 ")

                else:

                    content_val3 = str("你的表情好淡定 ")

 

                if float(anger) > 30 :

                    content_val5 = str("你生气了吓到宝宝了 ")

                   

                if float(surprise) > 30 :

                    content_val6 = str("那么惊讶啊不用惊讶 ")

 

                if float(sadness) > 30 :

                    content_val7 = str("假如生活欺骗了你 不要悲伤不要愤慨 忧郁的日子需要镇静 相信吧快乐的日子就要到来")

 

                tts_speak(content_val1+content_val2+content_val3+content_val4+content_val5+content_val6+content_val7)

                   

            elif ageval >55 :

               

                if gender =="Male" :

                    content_val1 = str("您好长者 见到您我真的好高兴 ")

                else :

                    content_val1 = str("您好长者 见到您我真的好高兴 ")

               

                content_val2 = str("您估计年龄%d岁 感觉还是意气风发啊 " %int(float(age)))

               

                if float(smile) > 30 and float(smile) < 50 :

                    content_val3 = str("您的微笑让我很温暖 ")

                elif float(smile) > 50 :

                    content_val3 = str("笑的那么灿烂啊 您看起来很开心 ")

 

                if float(anger) > 30 :

                    content_val4 = str("您生气了吓到宝宝了 ")

 

                if float(surprise) > 30 :

                    content_val5 = str("那么惊讶啊不用惊讶 ")

 

                if float(sadness) > 30 :

                    content_val6 = str("假如生活欺骗了你 不要悲伤不要愤慨 忧郁的日子需要镇静 相信吧快乐的日子就要到来")

 

                tts_speak(content_val1+content_val2+content_val3+content_val4+content_val5+content_val6)

            

        else :

            print "没有发现人脸"

            content_val = str("主人,没有发现人脸")

            tts_speak(content_val)

 

        head_led_turn_off()

       

except urllib2.HTTPError as e:

    print"人脸识别失败"

    content_val = str("主人,人脸识别失败")

    tts_speak(content_val)

    head_led_turn_off()

    print e.read()

except urllib2.URLError as e:

    print"网络请求超时，请检测网络后重新识别"

    content_val = str("网络请求超时，请检测网络后重新识别")

    tts_speak(content_val)

    head_led_turn_off()