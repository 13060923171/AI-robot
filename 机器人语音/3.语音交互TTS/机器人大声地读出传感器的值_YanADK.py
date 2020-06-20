#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import argparse

from subprocess import call

import time

import datetime

import openadk

from openadk.rest import ApiException

from pprint import pprint

# YanADK举例

configuration = openadk.Configuration()

configuration.host = 'http://127.0.0.1:9090/v1'

api_instance = openadk.SensorsApi(openadk.ApiClient(configuration))

 

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

 

def main():

    text_to_speech("Hello! I am Yanshee!") 

    while True:

        try:

            api_response = api_instance.get_sensors_infrared()

            pprint(api_response)

            pprint(api_response.data.infrared[0].value)

            text = "I have detected something " + str(api_response.data.infrared[0].value) + "centimeter ahead"

            text_to_speech(text)

            time.sleep(1)

        except ApiException as e:

            print("Exception when calling DevicesApi->get_sensors_infrared: %s\n" % e)

                

if __name__ == '__main__':

    main()