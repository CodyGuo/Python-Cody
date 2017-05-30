# -*- coding=utf-8 -*-

#自定义函数

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type:', x)
	if x>0:
		return x
	else:
		return -x

print('user define function my_abs:',my_abs(-12))

my_abs('a')
#print('user define function my_abs raise TypeError:',my_abs('a'))


#返回多个值
print('====返回多个值例子====')
import math
def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny
print('表达式x, y = move(100, 100, 60, math.pi / 6)返回多个值','=',move(100, 100, 60, math.pi / 6))
r = move(100, 100, 60, math.pi / 6)
print('返回单一值:', r)