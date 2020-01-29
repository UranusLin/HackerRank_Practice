#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
    for v in range(n):
        for j in range (n-v-1):
            print (' ',end='')
        for i in range (v+1):
            print ('#',end='')
        print('\n',end='')

if __name__ == '__main__':
    n = int(input())

    staircase(n)

