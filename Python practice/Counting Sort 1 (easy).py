n = int(input())
arr = list(map(int, input().split()))

def countingsort(arr, n):
    counts = [0]*n
    for i in arr:
        counts[i] += 1
    return counts[:100]

ans = countingsort(arr, n)
print (*ans)
