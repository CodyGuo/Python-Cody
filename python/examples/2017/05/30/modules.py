# -*- coding=utf-8 -*-

' a test module '
__author__ = 'CodyGuo'

import sys


def __priviate_1(name):
    print('Hello,%s' % name)


def _private_2(name):
    return 'Hi,%s' % name


def greeting(name):
    if len(name) > 3:
        return __priviate_1(name)
    else:
        return _private_2(name)


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world.')
    elif len(args) == 2:
        print('Helo %s!' % args[1])
    else:
        print('Too many args !')


# if __name__ == '__main__':
# test()
# greeting('module test')
# _priviate_1('_priviate_1')
