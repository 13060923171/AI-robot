#!/usr/bin/env python
#encoding: utf-8

import pygame
import time
import weatherAPI
import os
import sys
import subprocess
import tty,termios
import threading


def ShowPicture(picturepath,x0,y0):
    background=pygame.image.load(picturepath)
    background.convert_alpha()
    window.blit(background,(x0,y0))
    return
def ShowCircle():
    pygame.draw.circle(window,pygame.Color(255,255,255),(width/2,height/2),radius,fill)
    return
def ShowLine(x0,y0,x1,y1):
    pygame.draw.line(window,pygame.Color(255,255,255),(x0,y0),(x1,y1),fill)
    return

def get_ip(device):
    ip = subprocess.check_output("ip -4 addr show " + device + " | grep inet | awk '{print $2}' | cut -d/ -f1", shell = True).strip()
    return ip

#背景参数设置                         
width=1920
height=1080
fill=1
#初始化背景
pygame.init()
#window=pygame.display.set_mode((width,height),pygame.FULLSCREEN)#全屏
window=pygame.display.set_mode((width,height))#不全屏
window.fill(pygame.Color(255,255,255))

Yellow=(255,255,0)
Red=(255,0,0)
LightBlue=(190,190,255)
Green=(0,255,0)
Black=(0,0,0)
White=(255,255,255)

flag = 0

def ShowRec(x0,y0,x1,y1,color,fill):
    pygame.draw.rect(window,color,(x0,y0,x1,y1),fill)
    return

def ShowStr(mystring,x0,y0,size):
    font=pygame.font.Font('gkai00mp.ttf',size,bold=1)
    textSuface=font.render(mystring,1,pygame.Color(255,255,255))
    window.blit(textSuface,(x0,y0))                    
    return

def keyboard_thread():
    global flag 
    print ('press Q to quit')
    while True:
        fd=sys.stdin.fileno()
        old_settings=termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch=sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch=='q':
            print ("keyboard_thread exit!")
            flag = 1
            break
        elif ord(ch)==0x3:
	    #ctrl+c
            print ("keyboard_thread exit!")
            flag = 1
            break

def display_thread():
	global width
	global height
	global flag
	loop=0
	last_ip = ip = ''
	updatingtime=""
	WeatherValidation=False
	while True:
	    window.fill(pygame.Color(0,0,50))
	    #draw grids
	    ShowRec(10,10,width-20,height-80,White,1)
	    ShowLine(10,height/5,width-10,height/5)
	    ShowLine(10,height/5*3,width-10,height/5*3)
	    ShowLine(width/2,height/5,width/2,height-70)
	    ShowLine(width/4,height/5*3,width/4,height-70)
	    ShowLine(width/4*3,height/5*3,width/4*3,height-70)
	    #time show                                                                   
	    mylocaltime=time.localtime()
	    myclock=time.strftime("%H:%M:%S",mylocaltime)#13:15:03 2018-10-11
	    ShowStr(myclock,10,5,190)
	    mydate=time.strftime("%Y-%m-%d",mylocaltime)#2018-10-11
	    ShowStr(mydate,900,5,100)
	    mytime=time.strftime("%A",mylocaltime)#Thursday
	    ShowStr(mytime,900,100,80)
	    #ip show
	    ip = get_ip('wlan0')
	    ShowStr(ip,width/2+40,height/5*2+150,40)
	    
	    time.sleep(1)
	
	    #weather show
	    if loop % 600 == 0 : #update
	        jsonArr= weatherAPI.GetWeatherInfo()
	        if jsonArr!=None : #read weather data 
	            updatingtime=time.strftime("%H:%M:%S",mylocaltime)    
	            if jsonArr["desc"]!="OK":
	                print("weather data is none")
	                WeatherValidation=False
	            else:
	                result=jsonArr["data"]
	                forecast = result['forecast']
	                WeatherValidation=True
	                #print (result["city"],forecast[0]['type'],result["wendu"],forecast[0]['high'],forecast[0]['low'])
	    if WeatherValidation==True:
	        fengli = []
	        s1 = forecast[0]['fengli']
	        s2 = s1.split('[')
	        s3 = s2[2].split(']')
	        fengli.append(s3[0])
	        s1 = forecast[1]['fengli']
	        s2 = s1.split('[')
	        s3 = s2[2].split(']')
	        fengli.append(s3[0])
	        s1 = forecast[2]['fengli']
	        s2 = s1.split('[')
	        s3 = s2[2].split(']')
	        fengli.append(s3[0])
	        s1 = forecast[3]['fengli']
	        s2 = s1.split('[')
	        s3 = s2[2].split(']')
	        fengli.append(s3[0])
	        s1 = forecast[4]['fengli']
	        s2 = s1.split('[')
	        s3 = s2[2].split(']')
	        fengli.append(s3[0])
	        
	        q = int(result["aqi"])
	        if q > 0 and q < 50 :
	            level = "优"
	        if q > 49 and q <100 :
	            level = "良"
	        if q > 99 and q <150 :
	            level = "轻度污染"
	        if q > 149 and q <200 :
	            level = "中度污染"
	        if q > 199 and q <300 :
	            level = "重度污染"
	        if q > 299 and q <500 :
	            level = "严重污染"
		#室外温湿度
	        ShowPicture("pictures/"+forecast[0]['type']+".png",width/16,height/5+180)
	        ShowStr(result["city"],20,height/5+10,140)
	        ShowStr(forecast[0]['type'],20,height/5*2+50,120)
	        ShowStr(result["wendu"]+"℃",width/4,height/5+10,170)
	        ShowStr("最"+forecast[0]['high']+" "+"最"+forecast[0]['low'],width/4-80,height/5*2,48)
	        ShowStr("湿度:"+"60"+"%",width/4,height/5*2+110,48)
	        ShowStr(forecast[0]['fengxiang'],width/2+20,height/5+20,60)
	        ShowStr(fengli[0],width/2+50,height/5+120,60)
	        #空气质量
	        ShowStr("空气质量: "+level,width/2+450,height/5+120,70)
	        ShowStr("PM2.5: "+result["aqi"],width/2+450,height/5+20,70)
	        ShowStr(""+result["ganmao"],width/2+40,height/5+260,35)
	
	        #未来几天天气预报
	        ShowStr(forecast[1]["date"],width/32,height/5*3+height/30,48)
	        ShowStr(forecast[1]["type"],width/32,height/5*3+height/5-40,80)
	        ShowStr(fengli[1],width/32+70,height/5*3+height/10,64)
	        ShowStr(forecast[1]["low"]+"~"+forecast[1]["high"],width/32,height-130,32)
	        ShowPicture("pictures/"+forecast[1]["type"]+".png",width/32,height/5*3+height/10)
	
	        ShowStr(forecast[2]["date"],width/4+width/32,height/5*3+height/30,48)
	        ShowStr(forecast[2]["type"],width/4+width/32,height/5*3+height/5-40,80)
	        ShowStr(fengli[2],width/4+width/32+70,height/5*3+height/10,64)
	        ShowStr(forecast[2]["low"]+"~"+forecast[2]["high"],width/4+width/32,height-130,32)
	        ShowPicture("pictures/"+forecast[2]["type"]+".png",width/4+width/32,height/5*3+height/10)
	
	        ShowStr(forecast[3]["date"],width/4*2+width/32,height/5*3+height/30,48)
	        ShowStr(forecast[3]["type"],width/4*2+width/32,height/5*3+height/5-40,80)
	        ShowStr(fengli[3],width/4*2+width/32+70,height/5*3+height/10,64)
	        ShowStr(forecast[3]["low"]+"~"+forecast[3]["high"],width/4*2+width/32,height-130,32)
	        ShowPicture("pictures/"+forecast[3]["type"]+".png",width/4*2+width/32,height/5*3+height/10)
	
	        ShowStr(forecast[4]["date"],width/4*3+width/32,height/5*3+height/30,48)
	        ShowStr(forecast[4]["type"],width/4*3+width/32,height/5*3+height/5-40,80)
	        ShowStr(fengli[4],width/4*3+width/32+70,height/5*3+height/10,64)
	        ShowStr(forecast[4]["low"]+"~"+forecast[4]["high"],width/4*3+width/32,height-130,32)
	        ShowPicture("pictures/"+forecast[4]["type"]+".png",width/4*3+width/32,height/5*3+height/10)
	    #记录请求数据时间
	    ShowStr("数据更新时间: "+updatingtime,width/4*3,height/5*2+150,32)
	    
	    #update 
	    pygame.display.update()
	    loop +=1
	    if flag == 1 :
	        print ("display_thread exit!")
	        break

if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=keyboard_thread) 
    threads.append(t1) 
    t2 = threading.Thread(target=display_thread)                             
    threads.append(t2)                                                                                                                       

    for t in threads:
        t.setDaemon(True) 
        t.start()
    for t in threads:
        t.join()
    print ("All panel exit")
