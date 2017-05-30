# -*- coding=utf-8 -*-

def now(*args):
    print('2017-5-30')

f = now
print(f())
print(f.__name__)

def log(func):
    def wrapper(*args, **kv):
        print('call %s():' % func.__name__)
        return func(*args, **kv)

    return wrapper

@log
def now(*args):
    print('2017-5-30')

print(now())


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-1-1')


print(now())

import functools

print('-'*5, 'functools', '-'*5)
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

print(log(now))