from flask import Flask,render_template
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setwarnings(False)

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/on")
def on():
    GPIO.output(7,GPIO.HIGH)
    return render_template("main.html")

@app.route("/off")
def off():
    GPIO.output(7,GPIO.LOW)
    return render_template("main.html")

@app.route("/shining")
def shining():
    i=0
    while i<5:
        GPIO.output(7,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(7,GPIO.LOW)
        time.sleep(.5)
        i=i+1
    return render_template("main.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)