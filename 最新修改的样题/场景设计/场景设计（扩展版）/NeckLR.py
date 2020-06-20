import time
import json
import requests


def restful_get(model, params=None):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type': 'application/json'}
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def restful_put(model, data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type': 'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url, headers=headers, data=data)
    return response.json()


angle = 110
NeckLR_data = {
  "angles": {
    "NeckLR": angle,
  },
  "runtime": 504
}

response = restful_put('servos/angles', NeckLR_data)
print response
time.sleep(2)
angle = 90
NeckLR_data = {
  "angles": {
    "NeckLR": angle,
  },
  "runtime": 504
}
response = restful_put('servos/angles', NeckLR_data)
print response
