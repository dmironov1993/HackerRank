n = int(input())
array = list(map(int, input().split()))

# insertion sort
def insertion_sort(arr):
    for idx in range(1, len(arr)):
        currvalue = arr[idx]
        pos = idx
        while pos > 0 and arr[pos-1] > currvalue:
            arr[pos] = arr[pos-1]
            pos -= 1
            arr[pos] = currvalue
    return arr

# The closestNumbers function
def closestNumbers(arr):
    sub_list = []
    diff = []
    for i in range(len(arr)-1):
        el = arr[i]
        for j in range(i+1, len(arr)):
            sub_list.append((el, arr[j]))
            diff.append(abs(el - arr[j]))
    return sub_list, diff

sort = insertion_sort(array)
list_, dif = closestNumbers(sort)

count = 0
ans = []
for k in dif:
    if k == min(dif):
        idx = dif.index(k, count)
        ans.append(list_[idx])
    count += 1

print (*[i for sub in ans for i in sub])

