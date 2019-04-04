n, m = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        continue

print (happiness)
