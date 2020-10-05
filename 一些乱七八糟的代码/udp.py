#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

def headangle(angle,ADDR):
    data = str("{\"cmd\":\"servo\",\"type\":\"write\",\"time\":35,\"angle\":\"fffffffffffffffffffffffffff")
    angle_hex = str(hex(angle))
    print("angel_hex= %s"%(angle_hex))
    end = str("\"}")

    if(angle<16):
        hexdate = (data+"0"+angle_hex[-1]+end)
        udpCliSock.sendto(hexdate,ADDR)
        print(hexdate)
    else:
        udpCliSock.sendto(data + angle_hex[2] +angle_hex[3]+end,ADDR)
        print(data + angle_hex[2] +angle_hex[3] +end)

if __name__ == '__main__':
    print("Test UDP communication start.")
    HOST = '127.0.0.1'
    PORT = 20001
    ADDR = (HOST,PORT)
    udpCliSock = socket(AF_INET,SOCK_DGRAM)
    headangle(60,ADDR)
    print("Test UDP communication end.")