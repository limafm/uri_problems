# -*- coding: utf-8 -*-

input1 = input()
input1 = input1.split()
code1 = float(input1[0])
unit1 = float(input1[1])
price1 = float(input1[2])

input2 = input()
input2 = input2.split()
code2 = float(input2[0])
unit2 = float(input2[1])
price2 = float(input2[2])

res = price1*unit1 + price2*unit2

str_res = "VALOR A PAGAR: R$ %.2f" % (res)

print (str_res)