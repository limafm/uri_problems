# -*- coding: utf-8 -*-

# Impossible to me to think in a solution
# Did it based in that explanation:
# http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/

import sys
sys.setrecursionlimit(10500)

def josephus(n, m):
    if n == 1:
        return 1
    return ((josephus(n-1, m) + m - 1) % n) + 1

k = int(input())

for i in range(k):
    n, m = map(long, raw_input().split())

    print "Case %d: %d" % (i+1, josephus(n, m))
