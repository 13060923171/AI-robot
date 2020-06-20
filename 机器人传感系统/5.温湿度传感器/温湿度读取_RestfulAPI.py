import requests

import json

 

def get_sensor():

    sensor_url = "http://10.10.63.76:9090/v1/sensors/environment"

    headers={'Content-Type':'application/json'}

    response=requests.get(url=sensor_url, headers=headers)

    print (response.content)

    res = json.loads(response.content)

    if (len(res["data"])>0):

        print ("env id = %d : temperature = %d "%(res["data"]["environment"][0]["id"],res["data"]["environment"][0]["temperature"]))

        print ("env id = %d : humidity = %d "%(res["data"]["environment"][0]["id"],res["data"]["environment"][0]["humidity"]))

        print ("env id = %d : pressure = %d "%(res["data"]["environment"][0]["id"],res["data"]["environment"][0]["pressure"]))

if __name__ == '__main__':

    get_sensor()