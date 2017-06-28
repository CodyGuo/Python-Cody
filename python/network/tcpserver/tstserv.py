#!/usr/bin/env python

import socket
from time import ctime

HOST = ''
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waitting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...Conneted from:', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print('recive from [%s]: %s' %(addr, data.decode('utf-8')))
        tcpCliSock.send(('[%s] %s' % (
            ctime(), data.decode('utf-8'))).encode('utf-8'))
    tcpCliSock.close()

tcpSerSock.close()