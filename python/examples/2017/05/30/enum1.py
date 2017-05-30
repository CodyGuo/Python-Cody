#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 枚举

from enum import Enum


month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print('enum >')
print(month.Jan)
print(month.Jan.value)
print(month.__name__)

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum,unique

@unique
class Weekday(Enum):
	Jan = 1
	Feb = 2

print('unique >')
print(Weekday.Feb)
print(Weekday.Feb.value)