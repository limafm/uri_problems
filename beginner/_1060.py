# -*- coding: utf-8 -*-

cont = 0
for i in range(6):
    value = float(input())

    if value > 0:
        cont += 1
print "%d valores positivos" % cont
