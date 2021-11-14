#!/usr/bin/env python3
import threading,struct,time
from PIL import ImageGrab
import socket,cv2
import numpy as np
'''
author by : TsojanTeam Beard_Lin
time : 2021/11/14
'''
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=''#服务端ip
port=4455
client.connect((host,port))
#print(pyautogui.size()) #查看分辨率
def hand():
    p = ImageGrab.grab()

    img1 = np.asarray(p)
    data = cv2.resize(img1, dsize=(1000,668))
    _, imgdata = cv2.imencode(".jpg", data)
    img_len=struct.pack(">I",len(imgdata))#计算出文件长度 同时使用固定4字节格式的数据
    print(img_len)
    try:
        client.sendall(img_len)
        client.sendall(imgdata)

    except:
        print("连接中断")
        return
hand()
