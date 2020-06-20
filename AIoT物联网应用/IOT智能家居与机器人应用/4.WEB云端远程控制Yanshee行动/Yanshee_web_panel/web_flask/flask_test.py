#!/usr/bin/python
# -*- coding: utf-8 -*- 

import time
import RobotApi
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


RobotApi.ubtRobotInitialize()
#------------------------------Connect----------------------------------------
ret = RobotApi.ubtRobotConnect("SDK", "1", "127.0.0.1")
if (0 != ret):
    print ("Can not connect to robot %s" % robotinfo.acName)
    exit(1)

#----flask init---------------------
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/led/<int:id>',methods=['POST'])
def button_led(id):
    if request.method == 'POST':
        if id == 1:
            RobotApi.ubtSetRobotLED("button", "red", "on")
            print'ok turn on led'
        elif id == 2:
            RobotApi.ubtSetRobotLED("button", "blue", "breath")
            print'ok turn off led'
            
    return redirect(url_for('index'))

@app.route('/robot/<int:id>',methods=['POST'])
def robot_control(id):
    if request.method == 'POST':
        if id == 1:
	    RobotApi.ubtSetRobotMotion("walk", "front", 4,1)
	    RobotApi.ubtStartRobotAction("reset",1)
            print'ok robot move forward'
        elif id == 2:
	    RobotApi.ubtSetRobotMotion("walk", "back", 2,1)
	    RobotApi.ubtStartRobotAction("reset",1)
            print'ok robot backward'
        elif id == 3:
	    RobotApi.ubtSetRobotMotion("walk", "left", 3,1)
	    RobotApi.ubtStartRobotAction("reset",1)
            print'ok robot move left'
        elif id == 4:
	    RobotApi.ubtSetRobotMotion("walk", "right", 3,1)
	    RobotApi.ubtStartRobotAction("reset",1)
            print'ok robot move right'
        elif id == 5:
            RobotApi.ubtSetRobotMotion("raise", "left", 3, 1)
            RobotApi.ubtStartRobotAction("reset",1)
            print'ok robot raise left hand'
        elif id == 6:
	    RobotApi.ubtSetRobotMotion("bow", "", 1, 1)
	    RobotApi.ubtStartRobotAction("reset",1)
            print'ok robot bow'
        elif id == 7:
            RobotApi.ubtVoiceTTS(1,"你好，我是一个智能教学机器人")
            print'ok robot say something'
        elif id == 8:
	    RobotApi.ubtStopRobotAction()
            print'ok robot stop motion'

    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run( host='0.0.0.0', port=8888, debug=True )

#--------------------------DisConnect---------------------------------
RobotApi.ubtRobotDisconnect("SDK","1","127.0.0.1")
RobotApi.ubtRobotDeinitialize()

