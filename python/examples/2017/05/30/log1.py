# -*- coding=utf-8 -*-

#抛出错误
class FooError(ValueError):
    print("ValueError:", "异常失败.")

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
