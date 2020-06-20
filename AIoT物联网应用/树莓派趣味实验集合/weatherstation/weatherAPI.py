#! /usr/bin/python
# coding = utf-8

import urllib.request
import json
import gzip

cityname ="深圳"

def GetWeatherInfo():
    #访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityname)    
    try:
        #发出请求并读取到weather_data
        weather_data = urllib.request.urlopen(url).read()
        #以utf-8的编码方式解压数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        #将json数据转化为dict数据
        weather_dict = json.loads(weather_data)
        #print(weather_dict)
        return weather_dict
    except:
        return None


