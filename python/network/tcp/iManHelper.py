# -*- coding=utf-8 -*-

import struct
import socket


def createMsg(flag=1001, msg=None):
    return encode(flag, msg)


def encode(flag=None, msg=None):
    if flag == None:
        return
    Flag = flag
    ReServe = 0
    TotalLen = len(msg)
    Msg = bytes(msg)

    fmt = '<HHi%ds' % (TotalLen)
    imanMsg = struct.pack(fmt, Flag, ReServe, TotalLen, Msg)
    return imanMsg


def decode(msg=None):
    len_buf = len(msg)
    formatPack2 = '<HHi%ds' % (len_buf - 8)
    flag, _, _, msg = struct.unpack(formatPack2, buf[:len_buf])
    return flag, msg


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.10.2.227', 6002))

sendMsg = createMsg(
    1001,
    b'50-7B-9D-6D-E0-C1;10.10.2.162;empty;0;0;492420E4F57C64EE427458A72839400C'
)
sock.send(sendMsg)
buf = sock.recv(1024)
flag, msg = decode(buf)
print(flag, msg)

i = 0
while i < 100:
    i = i + 1
    sendMsg = createMsg(1002, b'50-7B-9D-6D-E0-C1')
    sock.send(sendMsg)
    buf = sock.recv(1024)
    flag, msg = decode(buf)
    print(flag, msg)

    sendMsg = createMsg(1003, b'50-7B-9D-6D-E0-C1')
    sock.send(sendMsg)
    buf = sock.recv(1024)
    flag, msg = decode(buf)
    print(flag, msg)

    sendMsg = createMsg(1019, b'50-7B-9D-6D-E0-C1;10.10.2.162')
    sock.send(sendMsg)
    buf = sock.recv(1024)
    flag, msg = decode(buf)
    print(flag, msg)

    # sendMsg = createMsg(1021, b'50-7B-9D-6D-E0-C1;10.10.2.162;1')
    # sock.send(sendMsg)
    # buf = sock.recv(1024)
    # flag, msg = decode(buf)
    # print(flag, msg)

    sendMsg = createMsg(1028, b'0')
    sock.send(sendMsg)
    buf = sock.recv(1024)
    flag, msg = decode(buf)
    print(flag, msg.decode("utf-8"))
