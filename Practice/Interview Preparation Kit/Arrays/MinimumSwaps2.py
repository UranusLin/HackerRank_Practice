#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ans = 0
    ref_list = sorted(arr)
    index_dict = {v:i for i,v in enumerate(arr)}
    for i , v in enumerate(arr):
        right = ref_list[i]
        if right != v :
            swap_index = index_dict[right]
            arr[i],arr[swap_index] = arr[swap_index],arr[i]
            index_dict[v] = swap_index
            index_dict[right] = i
            ans +=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
