#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr_length = len(arr)
    
    zero_count = 0
    positive_count = 0
    negative_count = 0
    
    for num in arr:
        if (num == 0):
            zero_count += 1
        elif (num > 0):
            positive_count += 1
        elif (num < 0):
            negative_count += 1
    
    print("{:.6f}".format(positive_count / arr_length))
    print("{:.6f}".format(negative_count / arr_length))
    print("{:.6f}".format(zero_count / arr_length))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
