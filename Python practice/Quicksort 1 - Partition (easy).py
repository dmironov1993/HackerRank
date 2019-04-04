# https://www.hackerrank.com/challenges/quicksort1/problem
# quicksort but not standard, see description of the problem
n = int(input())
arr = list(map(int, input().split()))

p = arr[0]
left = []
equal = []
right = []
for i in range(n):
    if p > arr[i]:
        left.append(arr[i])
    else:
        if p == arr[i]:
            equal.append(arr[i])
        else:
            right.append(arr[i])
ans = left + equal + right
print (*ans)
