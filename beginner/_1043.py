# -*- coding: utf-8 -*-

a, b = map(int, input().split())

if a > b:
    res = a % b
else:
    res = b % a

if res == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")
