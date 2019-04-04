n = int(input())
arr = list(map(int, input().split()))

def countingsort(arr, n):
    max_val = max(arr)
    m = max_val + 1
    counts = [0] * m
    for i in arr:
        counts[i] += 1
    idx = 0
    for i in range(m):
        for j in range(counts[i]):
            arr[idx] = i
            idx += 1
    return arr

ans = countingsort(arr, n)
print (*ans)
