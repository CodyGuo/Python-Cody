# -*- coding=utf-8 -*-

while True:
    reply = input('Enter number: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 5, '{' + reply + '}', 'Bad!' * 5)
    else:
        print(int(reply) ** 2)
print('Bye!')