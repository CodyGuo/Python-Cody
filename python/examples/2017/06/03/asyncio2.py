# -*- coding=utf-8 -*-
import asyncio
import time

# @asyncio.coroutine
async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # r, w = yield from connect 
    r, w = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host 
    w.write(header.encode('utf-8'))
    # yield from w.drain()
    await w.drain()
    while True:
        # line = yield from r.readline()
        line = await r.readline()
        if line == b'\r\n':
            break 
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    w.close()

loop = asyncio.get_event_loop()

tasks = [wget(host) for host in ['www.163.com', 'www.qq.com', 'www.hupu.cn', 'erp.hupu.cn']]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time()
print('运行时间 --> %s s' % (end - start))