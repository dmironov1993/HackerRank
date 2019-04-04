from itertools import combinations as cmb
n = int(input())
s = input().strip().split()
k = int(input())
p = 0
for element in s:
    if element == 'a':
        p += 1
if p == 0:
    numerator = len(list(cmb(s,k)))
else:
    numerator = len(list(cmb(s[:-p],k)))
    
print (1-numerator/len(list(cmb(s,k))))
