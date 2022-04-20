#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    
    lst = []
    
    def decimal_to_binary(num):
        if (num != 0):
            if (num // 2 != 0):
                lst.insert (0, num % 2)
            else:
                lst.insert(0, 1)
                return lst
        else:
            lst.append(0)
            return lst
                
        return (decimal_to_binary(num // 2))
    
    n_bin = decimal_to_binary(n)
        
    for i in range(32 - (len(n_bin))):
        n_bin.insert(0, 0)

    for i in range(32):
        if (n_bin[i] == 0):
            n_bin[i] = 1
        else:
            n_bin[i] = 0

    n_decimal = 0
    for i in range (32):
        n_decimal += n_bin[-(i+1)] * (2**i)
        
    return n_decimal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
