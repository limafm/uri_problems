# -*- coding: utf-8 -*-

import math

num = int(input())

#hours
_1hour = 3600
total_hour = int(num/_1hour)

num = num%_1hour

#minutes
_1minute = 60
total_minute = int(num/_1minute)

num = num%_1minute

#sec
total_sec = num

out = "%d:%d:%d" % (total_hour, total_minute, total_sec)
print (out)