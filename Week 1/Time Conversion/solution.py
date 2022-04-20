#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s_main = s[:2]
    s_main_int = int(s_main)
    if ((s_main_int == 12) and (s[-2] == 'A')):
        s_main_int = 0
        
    s_result = ''
    
    if (s[-2] == 'P'):
        if (s_main_int != 12):
            s_main_int += 12
        
        s_main = str(s_main_int) 
        s_result = s_main + s[2:-2]   
    
    elif(s[-2] == 'A'):
        if(s_main_int < 10):
            s_main = str(s_main_int)
            s_result = '0' + s_main + s[2:-2]
        else:
            s_main = str(s_main_int)
            s_result = s_main + s[2:-2]
            
    return s_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
