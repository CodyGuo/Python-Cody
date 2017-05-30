# -*- coding=utf-8 -*-

while True:
    reply = input('Enter number: ')
    if reply == 'stop': 
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 5, '{'+reply+'}', 'Bad!' * 5)
    else:
        if num < 20:
            print(num, 'too low')
        else:
            print(num ** 2)
print('Bye!')