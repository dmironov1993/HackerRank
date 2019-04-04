from itertools import combinations
string = input().strip().split()
for _ in range(1, int(string[1]) + 1):
    for item in enumerate(list(combinations(sorted(string[0]), _))):
        print (*item[1], sep='')
