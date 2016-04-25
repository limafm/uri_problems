# -*- coding: utf-8 -*-

import math

line1 = input().split()
line2 = input().split()

x1 = float(line1[0])
y1 = float(line1[1])
x2 = float(line2[0])
y2 = float(line2[1])

res = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

out = "%.4f" % res
print (out)