# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(n,a):
    cnt = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cnt += 1
    return cnt, a[0],a[-1]

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    numSwap, first, last = countSwaps(n,a)
    print ("Array is sorted in {} swaps.".format(numSwap))
    print ("First Element: {}".format(first))
    print ("Last Element: {}".format(last))
