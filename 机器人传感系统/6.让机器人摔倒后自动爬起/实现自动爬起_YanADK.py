#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import openadk

import time

from openadk.rest import ApiException

 

configuration = openadk.Configuration()

configuration.host = 'http://10.10.63.76:9090/v1'

start_time= int(time.time())

 

api_instance_sensor = openadk.SensorsApi(openadk.ApiClient(configuration))

api_instance_motion = openadk.MotionsApi(openadk.ApiClient(configuration))

api_instance_tts = openadk.VoiceApi(openadk.ApiClient(configuration))

 

body_tts_front = { "tts": "Detected fall forward, I am going to get up", "interrupt": False,"timestamp": start_time}

body_tts_back = { "tts": "Detected fall backward, I am going to get up", "interrupt": False,"timestamp": start_time}

body_motion_front = {"motion": {"name": "GetupFront","repeat": 1},"operation": "start","timestamp": start_time}

body_motion_back = {"motion": {"name": "GetupRear","repeat": 1},"operation": "start","timestamp": start_time}

body_motion_reset = {"motion": {"name": "reset","repeat": 1},"operation": "start","timestamp": start_time}

 

while True:

    try:

        time.sleep(1)

        api_response = api_instance_sensor.get_sensors_gyro()

        #print(api_response)

        if(api_response.data.gyro) :

            print("euler_x = %f " %(api_response.data.gyro[0].euler_x))

            #print("euler_y = %f " %(api_response.data.gyro[0].euler_y))

            #print("euler_z = %f " %(api_response.data.gyro[0].euler_z))

            print("-----------------------------------------")

        if api_response.data.gyro[0].euler_x > 160 or api_response.data.gyro[0].euler_x< -160:

            print 'Detected fall backward, I am going to get up'

            api_instance_tts.put_voice_tts(body_tts_back)

            print("Play TTS voice successfully!")

            #api_instance_motion.put_motions(body=body_motion_reset,async_req=False)

            ret=api_instance_motion.put_motions(body=body_motion_back,async_req=False)

            time.sleep(ret.data.total_time/1000)

            #print(ret.data.total_time)

        elif api_response.data.gyro[0].euler_x > -20 and api_response.data.gyro[0].euler_x < 20:

            print 'Detected fall forward, I am going to get up'

            api_instance_tts.put_voice_tts(body_tts_front)

            #api_instance_motion.put_motions(body=body_motion_reset)

            ret=api_instance_motion.put_motions(body=body_motion_front)

            time.sleep(ret.data.total_time/1000)

    except ApiException as e:

        print("Exception when calling DevicesApi->put_voice_tts: %s\n" % e)