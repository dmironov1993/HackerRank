def function(string, sub_string):
    n = 0
    start = 0
    stop = len(sub_string)
    for i in range(len(string)):
        result = string.find(sub_string, start, stop)
        if result != -1:
            n += 1
            start = stop - 1
            stop = start + len(sub_string)
        else:
            start += 1
            stop += 1
    return n
