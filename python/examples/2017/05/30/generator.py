# -*- coding=utf-8 -*-

L = [x * x for x in range(10)]
print(L)

#只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
for n in g:
    pass
    # print(n)


#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n = 0
    a, b = 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(10)
for n in f:
    # pass
    print(n)
