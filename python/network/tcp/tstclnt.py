#!/usr/bin/env python

import socket

HOST = 'localhost'
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    recvData = tcpCliSock.recv(BUFSIZE)
    if not recvData:
        break
    print('recive --> ', recvData.decode('utf-8'))

tcpCliSock.close()