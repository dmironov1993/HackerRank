from itertools import permutations as pm

string, k = input().strip().split()
for _ in sorted(pm(string, int(k))):
    print (*_, sep='')
