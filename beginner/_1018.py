# -*- coding: utf-8 -*-

import math

num = int(input())
rest = num

# 100
div = int(rest/100)
if (div > 0):
    cem = div
    rest = rest%100
else:
    cem = 0

# 50
div = int(rest/50)
if (div > 0):
    cinquenta = div
    rest = rest%50
else:
    cinquenta = 0

# 20
div = int(rest/20)
if (div > 0):
    vinte = div
    rest = rest%20
else:
    vinte = 0

# 10
div = int(rest/10)
if (div > 0):
    dez = div
    rest = rest%10
else:
    dez = 0

# 5
div = int(rest/5)
if (div > 0):
    cinco = div
    rest = rest%5
else:
    cinco = 0

# 2
div = int(rest/2)
if (div > 0):
    dois = div
    rest = rest%2
else:
    dois = 0

# 1
if (rest == 1):
    um = 1
else:
    um = 0

print (num)
out_cem = "%d nota(s) de R$ 100,00" % cem
print (out_cem)
out_cinquenta = "%d nota(s) de R$ 50,00" % cinquenta
print (out_cinquenta)
out_vinte = "%d nota(s) de R$ 20,00" % vinte
print (out_vinte)
out_dez = "%d nota(s) de R$ 10,00" % dez
print (out_dez)
out_cinco = "%d nota(s) de R$ 5,00" % cinco
print (out_cinco)
out_dois = "%d nota(s) de R$ 2,00" % dois
print (out_dois)
out_um = "%d nota(s) de R$ 1,00" % um
print (out_um)