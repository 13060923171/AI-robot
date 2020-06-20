import requests

import json

 

def get_sensor():

    sensor_url = "http://10.10.63.76:9090/v1/sensors/touch"

    headers={'Content-Type':'application/json'}

    response=requests.get(url=sensor_url, headers=headers)

    print (response.content)

    res = json.loads(response.content)

    if (len(res["data"]["touch"])>0):

        print ("touch id = %d : value = %d "%(res["data"]["touch"][0]["id"],res["data"]["touch"][0]["value"]))

if __name__ == '__main__':

    get_sensor()