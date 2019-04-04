s = input()

any_alnum = False
any_alpha = False
any_digit = False
any_lower = False
any_upper = False

for element in s:
    if element.isalnum():
        any_alnum = True
    if element.isalpha():
        any_alpha = True
    if element.isdigit():
        any_digit = True
    if element.islower():
        any_lower = True
    if element.isupper():
        any_upper = True
        
print (any_alnum)
print (any_alpha)
print (any_digit)
print (any_lower)
print (any_upper)
