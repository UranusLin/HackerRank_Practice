#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    a = scores.pop(0)
    best = a
    worst = a
    ans = [0,0]
    for i in scores:
        if int(a) < int(i) and int(i) > best:
            ans[0] = ans[0] + 1
            best = i
        elif int(a) > int(i) and int(i) < worst:
            ans[1] = ans[1] + 1
            worst = i
        a = i
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

