# -*- coding=utf-8 -*-
import socket
import struct


class MsgInfo():
    """docstring for MsgInfo."""

    def __init__(self, flag=None, msgBody=None):
        if not flag or not msgBody:
            raise 'flag or msgBody not None'
        self.Flag = flag
        self.ReServe = 0
        self.TotalLen = len(msgBody)
        self.Msg = msgBody.encode('utf-8')

    def __str__(self):
        return ('Flag: %d\nReseve: %d\nTotalLen: %d\nMsg: %s') % (
            self.Flag, self.ReServe, self.TotalLen, self.Msg)


class packer():
    __fmt = '<HHi%ds'

    def pack(self, msgInfo=MsgInfo):
        fmt = self.__fmt % msgInfo.TotalLen
        packMsg = struct.pack(fmt, msgInfo.Flag, msgInfo.ReServe,
                              msgInfo.TotalLen, msgInfo.Msg)
        return packMsg

    def unpack(self, bufMsg=None):
        bufLen = len(bufMsg)
        fmt = self.__fmt % (bufLen - 8)
        unpackMsg = struct.unpack(fmt, bufMsg[:bufLen])
        return unpackMsg


def send(
        sock=None,
        msgName=None,
        flag=None,
        msgBody=None, ):

    print('-' * 10, msgName, '-' * 10)
    msgInfo = MsgInfo(flag, msgBody)
    rAddr = sock.getpeername()
    print('发送给服务器{%s}的消息 {%s} --> \n' % (rAddr, msgName), msgInfo, sep='')
    msg = packer().pack(msgInfo)
    sock.send(msg)
    receive(sock, msgName)


def receive(sock=None, msgName=None):
    dataBuffer = bytes()
    headerSize = 8
    flag = False
    print('来自服务器的响应 {%s} --> \n' % msgName)
    while True:
        if flag:
            break
        data = sock.recv(100)
        while True:
            if data:
                # 把数据存入缓冲区，类似于push数据
                dataBuffer += data
                if len(dataBuffer) < headerSize:
                    print("接收到的数据包（%s Byte）小于消息头部长度，正在努力获取中..." %
                          len(dataBuffer))
                    break
                # 读取包头
                headPack = struct.unpack('<HHi', dataBuffer[:headerSize])
                bodySize = headPack[2]

                # 分包情况处理，跳出函数继续接收数据
                if len(dataBuffer) < headerSize + bodySize:
                    print("接收到的数据包（%s Byte）不完整（总共%s Byte），正在努力获取中..." %
                          (len(dataBuffer), headerSize + bodySize))
                    break

                # 读取消息正文的内容
                recMsg = dataBuffer[headerSize:headerSize + bodySize]
                print(recMsg.decode('utf-8'), sep='')
                flag = True
                if flag: break

        # recMsg = packer().unpack(bufMsg)
        # msgLen = recMsg[2] - 8
        # bufMsg = sock.recv(int(msgLen))
        # recMsg = packer().unpack(bufMsg)
        # if not recMsg:
        #     break
        #     print(
        #         '来自服务器的响应 {%s} --> \n' % msgName,
        #         recMsg[0:3],
        #         recMsg[3].decode('utf-8'),
        #         sep='')


def main():
    serverIP = '10.10.2.227'
    port = 6002
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIP, port))

    # 建立长连接
    send(
        sock, '建立长连接', 1001,
        '50-7B-9D-6D-E0-C1;10.10.2.162;empty;0;0;492420E4F57C64EE427458A72839400C'
    )

    # 客户端版本
    send(sock, '获取客户端版本', 1002, '50-7B-9D-6D-E0-C1')

    # 客户端获取重定向地址
    send(sock, '客户端获取重定向地址', 1003, '50-7B-9D-6D-E0-C1')

    # 客户端获取设备认证信息
    send(sock, '客户端获取设备认证信息', 1005, '50-7B-9D-6D-E0-C1;10.10.2.162')

    # 客户端请求警报策略
    send(sock, '客户端请求警报策略', 1019, '50-7B-9D-6D-E0-C1;10.10.2.162')

    # 客户端查询AD域服务器集合
    send(sock, '客户端查询AD域服务器集合', 1028, '0')


if __name__ == '__main__':
    main()