n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input().strip())

count_dict = dict()
for element in word_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

print (len(set(word_list)))
print (*list(count_dict.values()))
