from itertools import product

k,m = map(int, input().strip().split())
my_list = list(map(int, input().strip().split()[1:]) for _ in range(k))
result = max(list(map(lambda x: sum(i**2 for i in x)%m, product(*my_list))))
print (result)
