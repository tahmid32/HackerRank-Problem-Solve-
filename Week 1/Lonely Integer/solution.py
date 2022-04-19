#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    unique_element = 0
    count_dict = {}
    
    for num in a:
        if (num not in count_dict.keys()):
            count_dict[num] = 0
            count_dict[num] += 1
        
        else:
            count_dict[num] += 1
    
    for key in count_dict:
        if (count_dict[key] == 1):
            unique_element = key
            break
            
    return unique_element

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
