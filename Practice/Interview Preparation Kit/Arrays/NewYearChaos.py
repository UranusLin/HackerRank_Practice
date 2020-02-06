#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    for pos , value in enumerate(q):
        if (value - 1) - pos > 2 :
            ans = 'Too chaotic'
            break
        for j in range(max(0,value -2),pos) :
            if q[j] > value :
                ans += 1

    print(ans)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
