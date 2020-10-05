#!/usr/bin/env python

# -*- coding: utf-8 -*-


import io

import picamera

import cv2

import numpy

import time

import RPi.GPIO as GPIO

# GPIO setting for fan control

GPIO.setwarnings(False)  # Ignore warning for now

GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

# Set pin 8 to be an output pin and set initial value to high

GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

# get the pictures and found face

while True:

    # Create a memory stream so photos doesn't need to be saved

    stream = io.BytesIO()

    with picamera.PiCamera() as camera:

        camera.resolution = (320, 240)

        camera.capture(stream, format='jpeg')

    # Convert the picture into a numpy array

    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    # Now creates an OpenCV image

    image = cv2.imdecode(buff, 1)

    # Load a cascade file for detecting faces

    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

    # Convert to grayscale

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Look for faces in the image using the loaded cascade file

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print
    "Found " + str(len(faces)) + " face(s)"

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

cv2.imwrite('result.jpg', image)

# if found face turn on the fan

if len(faces) > 0:

    GPIO.output(8, GPIO.HIGH)  # Turn on

else:

    GPIO.output(8, GPIO.LOW)  # Turn off

time.sleep(1)