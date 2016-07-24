# -*- coding: utf-8 -*-

YEAR = 365
MONTH = 30

days = int(input())

total_year = days / YEAR
days = days % YEAR

total_month = days / MONTH
days = days % MONTH

print "%d ano(s)" % total_year
print "%d mes(es)" % total_month
print "%d dia(s)" % days
