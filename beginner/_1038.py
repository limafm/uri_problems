# -*- coding: utf-8 -*-

mapa = {}
mapa[1] = 4.00
mapa[2] = 4.50
mapa[3] = 5.00
mapa[4] = 2.00
mapa[5] = 1.50

x, y = map(int, raw_input().split())

total = mapa[x]*y

print "Total: R$ %.2f" % total
