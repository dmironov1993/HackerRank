from itertools import combinations_with_replacement as cwr

n = input().strip().split()
for element in list(cwr(sorted(n[0]), int(n[1]))):
    print (*element, sep='')
