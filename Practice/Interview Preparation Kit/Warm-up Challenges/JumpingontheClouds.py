#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    i = 0
    count = 0
    while i < n:
        if (i + 2) < n and c[i+2] == 0 :
            count = count +1
            i = i + 2
        elif (i + 2) < n and c[i+2] == 1 :
            count = count + 1
            i = i + 1
        else :
            i = i + 1
            count = count + 1

    return (count - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()

