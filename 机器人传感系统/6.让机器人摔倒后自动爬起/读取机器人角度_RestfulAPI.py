import requests

import json

 

def get_sensor():

    sensor_url = "http://10.10.63.76:9090/v1/sensors/gyro"

    headers={'Content-Type':'application/json'}

    response=requests.get(url=sensor_url, headers=headers)

    print (response.content)

    res = json.loads(response.content)

    if (len(res["data"]["gyro"])>0):

        print ("gyro id = %d : value = %f "%(res["data"]["gyro"][0]["id"],res["data"]["gyro"][0]["euler-x"]))

        print ("gyro id = %d : value = %f "%(res["data"]["gyro"][0]["id"],res["data"]["gyro"][0]["euler-y"]))

        print ("gyro id = %d : value = %f "%(res["data"]["gyro"][0]["id"],res["data"]["gyro"][0]["euler-z"]))

if __name__ == '__main__':

    get_sensor()