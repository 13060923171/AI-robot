# -*- coding: utf-8 -*-
import sys
import time
from socket import *

def sendmsg(ip,buf):
    PORT = 20005
    ADDR = (ip, PORT)
    udpclientSock = socket(AF_INET, SOCK_DGRAM)
    udpclientSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    udpclientSock.sendto(buf, ADDR)
    udpclientSock.close()

def action_func(Name,Repeat):
    print 'action name: ', Name,'.hts'
    print 'repeat times: ',Repeat
    send_string = "{\"cmd\":\"action\",\"type\":\"start\", \"para\":{\"name\":\""
    send_string = send_string + Name
    send_string = send_string + "\",\"repeat\":" + str(Repeat) + "}}"
    print send_string
    sendmsg("255.255.255.255", send_string)
    
if __name__ == '__main__':
    print 'start play action process'
    default_port = 20006
    if len(sys.argv) == 2:
        action_name = sys.argv[1]
        action_func(action_name, 1)
    elif len(sys.argv) == 3:
        action_name = sys.argv[1]
        repeat = int(sys.argv[2],10)
        action_func(action_name, repeat)
    else:
        print '输入参数错误!'
        print '正确格式: python action_test.py  名称 '