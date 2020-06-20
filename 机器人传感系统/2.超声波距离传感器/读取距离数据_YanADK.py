#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import openadk

from openadk.rest import ApiException

from pprint import pprint

import time

 

configuration = openadk.Configuration()

configuration.host = 'http://127.0.0.1:9090/v1'

 

api_instance = openadk.SensorsApi(openadk.ApiClient(configuration))

 

try:

    api_response = api_instance.get_sensors_ultrasonic()

    pprint(api_response)

    pprint(api_response.data.ultrasonic)

except ApiException as e:

    print("Exception when calling DevicesApi->get_sensors_ultrasonic: %s\n" % e)