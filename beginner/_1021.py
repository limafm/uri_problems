# -*- coding: utf-8 -*-

total = float(input())
total += 0.001

print "NOTAS:"

notas_cem = total / 100
print "%d nota(s) de R$ 100.00" % notas_cem
total = total % 100

notas_cinquenta = total / 50
print "%d nota(s) de R$ 50.00" % notas_cinquenta
total = total % 50

notas_vinte = total / 20
print "%d nota(s) de R$ 20.00" % notas_vinte
total = total % 20

notas_dez = total / 10
print "%d nota(s) de R$ 10.00" % notas_dez
total = total % 10

notas_cinco = total / 5
print "%d nota(s) de R$ 5.00" % notas_cinco
total = total % 5

notas_dois = total / 2
print "%d nota(s) de R$ 2.00" % notas_dois
total = total % 2

print "MOEDAS:"

moeda_um_real = total / 1
print "%d moeda(s) de R$ 1.00" % moeda_um_real
total = total % 1

moeda_cinquenta = total / 0.5
print "%d moeda(s) de R$ 0.50" % moeda_cinquenta
total = total % 0.50

moeda_vinteecinco = total / 0.25
print "%d moeda(s) de R$ 0.25" % moeda_vinteecinco
total = total % 0.25

moeda_dez = total / 0.10
print "%d moeda(s) de R$ 0.10" % moeda_dez
total = total % 0.10

moeda_cinco = total / 0.05
print "%d moeda(s) de R$ 0.05" % moeda_cinco
total = total % 0.05

moeda_um = total / 0.01
print "%d moeda(s) de R$ 0.01" % moeda_um
