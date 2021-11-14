import socket,struct,cv2
import threading,time
import numpy as np
'''
author by : TsojanTeam Beard_Lin
time : 2021/11/14
'''
def run(clientsocket):
    while True:
        img_len = clientsocket.recv(4)
        lenb=struct.unpack(">I",img_len)[0]
        img_by=b''
        while lenb > 1024:#在长度大于1024时依次读取
            img_data=clientsocket.recv(1024)
            img_by+=img_data
            lenb-=1024
        while lenb > 0:#在上一个循环完成后 此循环用来避免len为0并且确保图片数据读取完毕
            img_data=clientsocket.recv(lenb)
            img_by+=img_data
            lenb=0
        img_decode=np.frombuffer(img_by,dtype=np.uint8)
        img= cv2.imdecode(img_decode,cv2.IMREAD_COLOR)
        cv2.imwrite(str(time.time())+".jpg",cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        cv2.waitKey(90)
        time.sleep(15)
if __name__ == '__main__':
    while True:
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '0.0.0.0'
        port = 4455
        socket_server.bind((host, port))
        socket_server.listen(5)
        clientsocket, addr = socket_server.accept()
        threading.Thread(target=run,args=(clientsocket,)).start()
