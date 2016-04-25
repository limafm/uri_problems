# -*- coding: utf-8 -*-

name = input()
fixed_salary = input()
sale_total = input()

res = float(fixed_salary) + float(sale_total)*0.15

str_res = "TOTAL = R$ %.2f" % (res)

print (str_res)