# -*- coding: utf-8 -*-
import math

n1, n2, n3, n4 = map(float, raw_input().split())

total = (n1*2 + n2*3 + n3*4 + n4)/10

print "Media: %.1f" % total
if total >= 7.0:
	print "Aluno aprovado."
elif total < 5.0:
	print "Aluno reprovado."
else:
	print "Aluno em exame."
	exame = float(input())
	print "Nota do exame: %.1f" % exame
	total = (total + exame)/2
	if total >= 5.0:
		print "Aluno aprovado."
	else:
		print "Aluno reprovado."
	print "Media final: %.1f" % total
