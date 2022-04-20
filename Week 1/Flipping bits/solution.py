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
    n_bin_str = bin(n)
    
    actual_n_bin_str = n_bin_str[2:]
    actual_n_bin = [int(i) for i in actual_n_bin_str]

    for i in range(32 - (len(actual_n_bin))):
        actual_n_bin.insert(0, 0)

    for i in range(32):
        if (actual_n_bin[i] == 0):
            actual_n_bin[i] = 1
        else:
            actual_n_bin[i] = 0

    n_decimal = 0
    for i in range (32):
        n_decimal += actual_n_bin[-(i+1)] * (2**i)
        
    return n_decimal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
