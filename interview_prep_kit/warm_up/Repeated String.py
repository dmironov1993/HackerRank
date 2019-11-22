#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    slen = len(s)
    cnt = 0
    for i in range(slen):
        if s[i] == 'a':
            cnt += 1
    p = n//slen
    cnt *= p
    add = n - p*slen
    for i in range(add):
        if s[i] == 'a':
            cnt += 1 
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
