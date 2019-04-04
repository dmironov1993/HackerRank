# insertion sort
n = int(input())
arr = list(map(int, input().split()))
def insertion_sort(arr, n):
    count = 0
    for idx in range(1,n):
        pos = idx
        currvalue = arr[pos]
        while pos>0 and arr[pos-1]>currvalue:
            arr[pos]=arr[pos-1]
            pos -= 1
            arr[pos]=currvalue
            count += 1    
    return count
ans = insertion_sort(arr, n)
print (ans)
