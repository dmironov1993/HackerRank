from itertools import groupby
string = input()
result = [(sum(1 for _ in group), int(key)) for key, group in groupby(string)]
print (*result, sep=' ')
