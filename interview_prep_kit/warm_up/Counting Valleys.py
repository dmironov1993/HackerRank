#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    cntu = 0
    cntd = 0
    cnt_valley = 0
    for i in range(n):
        if s[i] == 'U':
            cntu += 1
        else:
            cntd += 1
        if cntu == cntd:
            if s[i] == 'U' and (s[i-1] == 'U' or s[i-1] == 'D'):
                cnt_valley += 1
    return cnt_valley
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
