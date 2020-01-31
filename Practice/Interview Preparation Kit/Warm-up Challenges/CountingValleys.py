#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    seaLevel = 0
    count = 0
    s = list(s)
    status = None
    for i in s :
        if i == 'D' :
            seaLevel = seaLevel - 1
        else :
            seaLevel = seaLevel + 1
        if status == None and seaLevel < 0:
            status = 'D'
        elif status == 'D' and seaLevel >= 0 :
            count = count + 1
            status = None
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

