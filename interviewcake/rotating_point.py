words = [
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'abberation',
]


def get_rotating_point_idx_simple(l):
    # linear
    prev = None
    for idx, item in enumerate(l):
        if prev and item < prev:
            return idx
        prev = item
    return 0


def get_rotating_point_idx(l):
    if len(l) == 1:
        return 0
    if len(l) == 2:
        return min(enumerate(words), key=lambda x: x[1])[0]

    # binary search-like approach
    left = 0
    right = len(l)
    anchor = l[0]
    while right > left + 1:
        mid = (left + right) // 2
        if l[mid] > anchor:
            left = mid
        elif l[mid] < anchor:
            right = mid
    if mid + 1 < len(l):
        items = [l[i] for i in range(mid - 1, mid + 1 + 1)]
    else:
        items = [l[i] for i in range(mid - 1, mid + 1)]
    target = min(enumerate(items), key=lambda x: x[1])[0] + mid - 1
    return target if words[target] < anchor else 0


index = get_rotating_point_idx_simple(words)
print(words[index])
index = get_rotating_point_idx(words)
print(words[index])
