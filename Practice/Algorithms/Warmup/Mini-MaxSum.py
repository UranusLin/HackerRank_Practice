#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    temp = arr[:]
    del temp[0]
    mina = sum(temp)
    maxa = sum(temp)
    for i in range(1,len(arr)):
        temp = arr[:]
        del temp[i]
        a = sum(temp)
        if a > maxa :
            maxa = a
        elif a < mina :
            mina = a
    print (mina,maxa)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

