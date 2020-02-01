#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s = list(s)
    slen = len(s)
    tempCount = int(n/slen)
    scount = s.count('a')
    count = tempCount * scount
    if n%slen > 0 :
        slen = slen - (n%slen)
        for i in  range(0,slen) :
            s.pop()
        scount = s.count('a')
        count = count + scount
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
