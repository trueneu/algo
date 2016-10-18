def reverse_words(s):
    return ' '.join(reversed(s.split()))


def reverse_words2(s):
    words = s.split()
    words_len = len(words)
    for i in range(words_len - 1, -1, -1):
        words.insert(i, words.pop(0))
    return ' '.join(words)

print(reverse_words2("find you will pain only go you recordings security the into if"))
