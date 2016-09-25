segments = [(1, 3), (1, 4), (2, 3), (2, 4), (3, 5)]


def left_child_index(i):
    return 2*i + 1


def right_child_index(i):
    return 2*i + 2

sorted_endpoints = sorted([x for segment in segments for x in segment])
print(sorted_endpoints)
