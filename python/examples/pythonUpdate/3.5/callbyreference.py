# -*- coding=utf-8 -*-

class callByRef:
    def __init__(self, **args):
        for (k, v) in args.items():
            setattr(self, k,v)

def func(args):
    args.a = 'new-value'
    args.b = args.b + 1

args = callByRef(a = 'old-value', b = 99)
func(args)

print(args.a, args.b)