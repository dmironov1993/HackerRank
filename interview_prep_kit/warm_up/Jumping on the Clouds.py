# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jumps = 0
    pos = 0
    while True:
        if (pos + 2 < n):
            if (c[pos+2] - c[pos] == 1):
                jumps += 1
                pos += 1
            else:
                jumps += 1
                pos += 2
        else:
            if c[-1] == 0 and pos != n-1:
                jumps += 1
            break
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
