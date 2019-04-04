def score_words(words):
    dictionary = ['a', 'e', 'i', 'o', 'u', 'y']
    score = 0
    for word in words:
        count = 0
        for element in list(word):
            if element in dictionary:
                count += 1
        if count % 2 == 0:
            score += 2
        else:
            score += 1
    return score
