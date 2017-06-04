# -*- coding=utf-8 -*-
import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello world. (%s)' % threading.current_thread())

    yield from asyncio.sleep(3)
    print('Hello again. (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()

tasks = [hello(), hello()]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()