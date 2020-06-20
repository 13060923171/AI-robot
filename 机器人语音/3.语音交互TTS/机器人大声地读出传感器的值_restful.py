#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import argparse

from subprocess import call

import time

import datetime

import requests

import json

 

sensor_url = "http://127.0.0.1:9090/v1/sensors/infrared"

headers={'Content-Type':'application/json'}

 

#Calls the Espeak TTS Engine to read aloud a sentence

def text_to_speech(text):

    #   -ven+m7: Male voice

    #  The variants are +m1 +m2 +m3 +m4 +m5 +m6 +m7 for male voices and +f1 +f2 +f3 +f4 which simulate female voices by using higher pitches. Other variants include +croak and +whisper.

    #  Run the command espeak --voices for a list of voices.

    #   -s180:          set reading to 180 Words per minute

    #   -k20:           Emphasis on Capital letters

    #call(" amixer set PCM 100 ", shell=True)    # Crank up the volume!

 

    cmd_start=" espeak -ven-us+m7 -a 200 -s180 -k20 --stdout '"

    cmd_end="' | aplay"

    call ([cmd_start+text+cmd_end], shell=True)

def get_sensor():

    response=requests.get(url=sensor_url, headers=headers)

    #print (response.content)

    res = json.loads(response.content)

    if (len(res["data"])>0):

        print ("infrared id = %d : value = %d mm"%(res["data"]["infrared"][0]["id"],res["data"]["infrared"][0]["value"]))

        text = "I have detected something " + str(res["data"]["infrared"][0]["value"]) + "centimeter ahead"

        text_to_speech(text)

def main():

    text_to_speech("Hello! I am Yanshee!") 

    while True:

        get_sensor()

        time.sleep(1)

if __name__ == '__main__':

    main()