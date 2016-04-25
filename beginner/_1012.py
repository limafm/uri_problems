# -*- coding: utf-8 -*-
import math

pi = 3.14159

input1 = input()
input1 = input1.split()

a = float(input1[0])
b = float(input1[1])
c = float(input1[2])

# triangle area
tri = a*c/2
res_tri = "TRIANGULO: %.3f" % tri

# circle area
cir = pi*pow(c,2)
res_cir = "CIRCULO: %.3f" % cir

# trapezium area
tra = 1/2*c*(a+b)
res_tra = "TRAPEZIO: %.3f" % tra

# square area
square = pow(b,2)
res_square = "QUADRADO: %.3f" % square

# rectangle area
rec = a*b
res_rec = "RETANGULO: %.3F" % rec

# printing results
print (res_tri)
print (res_cir)
print (res_tra)
print (res_square)
print (res_rec)