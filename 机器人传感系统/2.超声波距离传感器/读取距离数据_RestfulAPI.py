import requests

import json

 

def get_sensor():

    sensor_url = "http://127.0.0.1:9090/v1/sensors/ultrasonic"

    headers={'Content-Type':'application/json'}

    response=requests.get(url=sensor_url, headers=headers)

    print (response.content)

    res = json.loads(response.content)

    if (len(res["data"])>0):

        print ("ultrasonic id = %d : value = %d "%(res["data"]["ultrasonic"][0]["id"],res["data"]["ultrasonic"][0]["value"]))

if __name__ == '__main__':

        get_sensor()