#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import openadk

from openadk.rest import ApiException

 

configuration = openadk.Configuration()

configuration.host = 'http://10.10.63.76:9090/v1'

 

api_instance = openadk.SensorsApi(openadk.ApiClient(configuration))

 

try:

    api_response = api_instance.get_sensors_gyro()

    print(api_response)

    if(api_response.data.gyro) :

        print("euler_x = %.3f " %(api_response.data.gyro[0].euler_x))

        print("euler_y = %.3f " %(api_response.data.gyro[0].euler_y))

        print("euler_z = %.3f " %(api_response.data.gyro[0].euler_z))

except ApiException as e:

    print("Exception when calling DevicesApi->get_sensors_gyro: %s\n" % e)