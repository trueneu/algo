f = open('max_rect_input.txt')
#n = int(input().strip())
n = int(f.readline().strip())

#indexes_to_heights = [int(x) for x in input().strip().split()]
indexes_to_heights = [int(x) for x in f.readline().strip().split()]
heights = set(indexes_to_heights)

max_square = 0

prev_h = 0
possible_heights = sorted(heights)
r_curr = {k: 0 for k in possible_heights}

def binary_search(lst, num):
    a = 0
    b = len(lst) - 1
    r = b // 2
    while b - a > 1:
        if lst[r] > num:
            b = r
            r = (a + b) // 2
        else:
            a = r
            r = (a + b) // 2
    return r if lst[b] != num else b

for h in indexes_to_heights:
    h_index = binary_search(possible_heights, h)
    try:
        r_curr.update({k: k + r_curr[k] for k in possible_heights[:h_index + 1]})
    except IndexError:
        r_curr = {k: k + r_curr[k] for k in possible_heights}

    try:
        max_square = max(max(r_curr.values()), max_square)
        r_curr.update({k: 0 for k in possible_heights[h_index + 1:]})
    except IndexError:
        pass

max_square = max(max(r_curr.values()), max_square)

print(max_square)
