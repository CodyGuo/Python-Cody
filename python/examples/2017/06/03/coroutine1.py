# -*- coding=utf-8 -*-

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return 
        print('[consumer] %s...' %n)
        r = '200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[produce] %s...' % n)
        r = c.send(n)
        print('[produce] return: %s' % r)
    c.close()

c = consumer()
produce(c)
