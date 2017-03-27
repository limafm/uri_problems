# -*- coding: utf-8 -*-

arr = []

arr.append(float(input()))
arr.append(float(input()))
arr.append(float(input()))
arr.append(float(input()))
arr.append(float(input()))
arr.append(float(input()))

positives = 0
positives_count = 0

for x in arr:
    if x > 0:
        positives += x
        positives_count += 1

print (positives_count, "valores positivos")
print ("%.1f" % (positives/positives_count))
