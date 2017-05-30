# -*- coding=utf-8 -*-

class MessageInfo:
    def __init__(self, msgFlag, msgBody):
        self.msgFlag = msgFlag
        self.msgReServe = 0
        
        msgBody = msgBody.encode(encoding='utf-8')
        # msgBody = bytes(msgBody, encoding='utf-8')
        self.msgBodySize = msgBody.__len__()
        self.msgBody = msgBody
    
    def getMsg(arg):
        pass
    

def createMsg(msgFlag=1001, msgBody=None):
    if msgBody == None:
        return

     # fmt = defaultFmt.format(len(msgBody))
    fmt = defaultFmt % (len(msgBody))
    print('%s -> {%d %s}' % (fmt, msgFlag, msgBody))
    msgInfo = MessageInfo(msgFlag, msgBody)
    print(msgInfo.msgFlag, msgInfo.msgReServe, msgInfo.msgBodySize, msgInfo.msgBody)


if __name__ == '__main__':
    # defaultFmt = '<HHi{0}s'
    defaultFmt = '<HHi%ds'
    msg = 'hello'
    createMsg(1001, msg)
    createMsg(1002, "world!")
    createMsg(1003, None)
    createMsg(1005, 'codyguo')
    
    

    # msginfo = MssageInfo(msgFlag=1001, msgBody='hi codyguo')
    # print(msginfo.msgFlag, msginfo.msgBody)

