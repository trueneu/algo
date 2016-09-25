words = [
    'paj',
    'pamdada',
    'parcha',
    'ploshka',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def find_pivot_wrapper(words):
    if len(words) <= 3:
        if len(words) == 0:
            return None
        elif len(words) == 1:
            return 1
        elif len(words) == 2:
            if words[0] < words[1]:
                pass
    # blah, blah, blah
    # process each edge case on its own

def find_pivot(words, start, end):
    middle = int((end + start) / 2)
    if start >= end - 1:
        return None
    if words[start] < words[start - 1] and words[start] < words[start + 1]:
        return start
    if words[end] < words[end - 1] and words[end] < words[end + 1]:
        return end
    if words[middle] < words[middle - 1] and words[middle] < words[middle + 1]:
        return middle
    r1 = find_pivot(words, start, middle)
    r2 = find_pivot(words, middle, end)
    if r1:
        return r1
    if r2:
        return r2
    return None


for i,v in enumerate(words):
    print(str(i) + " : " + str(v))
print(find_pivot(words, 0 + 1, len(words) - 1))