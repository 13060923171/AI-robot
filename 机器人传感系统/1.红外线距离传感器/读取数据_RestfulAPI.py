import requests

import json

import time

 

def get_sensor():

    sensor_url = "http://10.10.63.76:9090/v1/sensors/infrared"

    headers={'Content-Type':'application/json'}

    response=requests.get(url=sensor_url, headers=headers)

    #print (response.content)

    res = json.loads(response.content)

    if (len(res["data"])>0):

        print ("infrared id = %d : value = %d mm"%(res["data"]["infrared"][0]["id"],res["data"]["infrared"][0]["value"]))

if __name__ == '__main__':

    while True:

        get_sensor()

        time.sleep(1)