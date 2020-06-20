#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import requests

import json

import time

 

root_url = "http://10.10.63.76:9090/v1"

sensor_url = root_url+"/sensors/gyro"

tts_url = root_url+"/voice/tts"

motion_url = root_url+"/motions"

headers={'Content-Type':'application/json'}

start_time= int(time.time())

 

body_tts_front = { "tts": "Detected fall forward, I am going to get up", "interrupt": False,"timestamp": start_time}

body_tts_back = { "tts": "Detected fall backward, I am going to get up", "interrupt": False,"timestamp": start_time}

body_motion_front = {"motion": {"name": "GetupFront","repeat": 1},"operation": "start","timestamp": start_time}

body_motion_back = {"motion": {"name": "GetupRear","repeat": 1},"operation": "start","timestamp": start_time}

body_motion_reset = {"motion": {"name": "reset","repeat": 1},"operation": "start","timestamp": start_time}

 

while True:

        time.sleep(1)

        response=requests.get(url=sensor_url, headers=headers)

        res = json.loads(response.content)

        if(len(res["data"]["gyro"])>0) :

            print ("gyro euler-x = %f "%(res["data"]["gyro"][0]["euler-x"]))

            print ("gyro euler-y = %f "%(res["data"]["gyro"][0]["euler-y"]))

            print ("gyro euler-z = %f "%(res["data"]["gyro"][0]["euler-z"]))

            print ("------------------------------------------------")

            if res["data"]["gyro"][0]["euler-x"] > 160 or res["data"]["gyro"][0]["euler-x"] < -160:

                print 'Detected fall backward, I am going to get up'

                json_data = json.dumps(body_tts_back)

                requests.put(url=tts_url,data=json_data, headers=headers)

                print("Play TTS voice successfully!")

                json_data = json.dumps(body_motion_back)

                res=requests.put(url=motion_url,data=json_data, headers=headers)

                ret = json.loads(res.content)

                time.sleep(ret["data"]["total_time"]/1000)

                print(ret["data"]["total_time"])

            elif res["data"]["gyro"][0]["euler-x"] > -20 and res["data"]["gyro"][0]["euler-x"] < 20:

                print 'Detected fall forward, I am going to get up'

                json_data = json.dumps(body_tts_front)

                requests.put(url=tts_url,data=json_data, headers=headers)

                json_data = json.dumps(body_motion_front)

                res=requests.put(url=motion_url,data=json_data, headers=headers)

                ret = json.loads(res.content)

                time.sleep(ret["data"]["total_time"]/1000)