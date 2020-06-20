#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import openadk

from openadk.rest import ApiException

from pprint import pprint

 

configuration = openadk.Configuration()

configuration.host = 'http://10.10.63.76:9090/v1'

 

api_instance = openadk.SensorsApi(openadk.ApiClient(configuration))

 

try:

    api_response = api_instance.get_sensors_environment()

    pprint(api_response)

    pprint(api_response.data.environment)

    if (api_response.data.environment) :

        pprint(api_response.data.environment[0].temperature)

        pprint(api_response.data.environment[0].humidity)

        pprint(api_response.data.environment[0].pressure)

except ApiException as e:

    print("Exception when calling DevicesApi->get_sensors_environment: %s\n" % e)