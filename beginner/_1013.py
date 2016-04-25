# -*- coding: utf-8 -*-

import math

input1 = input()
input1 = input1.split()

a = float(input1[0])
b = float(input1[1])
c = float(input1[2])

maior = (a+b+math.fabs(a-b))/2

maior = (maior+c+math.fabs(maior-c))/2

res = "%d eh o maior" % maior

print (res)