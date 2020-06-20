from flask import *
import json
import requests
import time

app = Flask(__name__)

data_bow = {
    "operation": "start",
    "motion": {
        "name": "bow",
        "repeat": 1,
        "speed": "very slow"
    },
    "timestamp": int(time.time())
}
data_reset = {
    "operation": "start",
    "motion": {
        "name": "reset",
        "repeat": 1,
        "speed": "normal"
    },
    "timestamp": int(time.time())
}

def restful_put(model,data):
    url = "http://127.0.0.1:9090/v1/%s" % model
    headers = {'content-type':'application/json'}
    data = json.dumps(data)
    response = requests.put(url=url,headers=headers,data=data)
    return response.json()

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if request.form.get('submit_button') == 'ON':
            restful_put('motions',data_bow)
            time.sleep(5)
            restful_put('motions',data_reset)
            print 'cheng gong bow'
        else:
            pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0")