#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    a = b = c =0
    for i in arr :
        if i > 0 :
            a = a +1
        elif i < 0 :
            b = b+1
        else :
            c = c+1
    print('%.6f'%(a/len(arr)))
    print('%.6f'%(b/len(arr)))
    print('%.6f'%(c/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

