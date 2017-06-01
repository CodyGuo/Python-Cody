# -*- coding=utf-8 -*-
import time
''' 
    斐波那契数列
    Fibonacci(40) = 102334155
    计算Fibonacci用时 56.781259536743164 s
'''


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    start = time.time()
    n = 40
    fibN = fib(n)
    end = time.time()
    print('Fibonacci(%d) = %d' % (n, fibN))
    print('计算Fibonacci用时 %s s' % (end - start))
