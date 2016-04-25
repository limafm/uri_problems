# -*- coding: utf-8 -*-

import sys

try:
    input_str = input()

    while(1):
        input_str = input_str.split()
        a = int(input_str[0])
        b = int(input_str[1])
        res = a^b   //this is a binary xor

        print (res)

        try:
            input_str = input()
        except (EOFError):
           break #end of file reached
except:
    pass

'''

    ## harcoded solution
    input1 = input_str
    input1 = input1.split()

    a = int(input1[0])
    a = bin(a)[2:].zfill(32)

    b = int(input1[1])
    b = bin(b)[2:].zfill(32)

    bin_res = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            bin_res += "0"
        else:
            bin_res += "1"

    res = int(bin_res, 2)
    print (res)

    input_str = input()
    '''