# -*- coding=utf-8 -*-

def linear(a, b):
    def result(x):
        return a * x + b
    return result

taxes = linear(0.3, 2)
print(taxes(100))


class linearclass():
    """docstring for linearclass."""
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, x):
        return self.a * x + self.b

taxes = linearclass(0.3, 2)
print(taxes(10))


class counter():
    """docstring for counter."""
    value = 0
        
    def set(self, x):
        self.value = x

    def up(self):
        self.value = self.value +1

    def down(self):
        self.value = self.value - 1

count = counter()
inc,dec,reset = count.up, count.down, count.set
inc()
print(count.value)
dec()
print(count.value)
reset(100)
print(count.value)

