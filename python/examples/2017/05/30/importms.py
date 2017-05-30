# -*- coding=utf-8 -*-

import modules

print(modules.__doc__)
print(modules.__author__)

print('test -->')
modules.test()

print('greeting -->')
modules.greeting('greeting')

print('priviate1 -->')
modules.__priviate_1('priviate1')

print('priviate2 -->')
print(modules._private_2('priviate2'))
