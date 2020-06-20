#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import pyaudio,wave
import os,sys
 
os.close(sys.stderr.fileno())
pa = pyaudio.PyAudio() 
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True, 
                frames_per_buffer=2000) 
 
save_buffer = '' 
 
wf = wave.open('output.wav', 'wb')
wf.setnchannels(1) 
wf.setsampwidth(2) 
wf.setframerate(16000)
try:
    while True: 
        string_audio_data = stream.read(1000)
        save_buffer += string_audio_data
        if len(save_buffer) >= 160000:
            wf.writeframes(save_buffer)
            break
except:
    wf.close()