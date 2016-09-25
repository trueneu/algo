def binary_search(numbers_sorted, number_to_find):
    start = 0
    stop = len(numbers_sorted)
    middle = (stop - start) // 2
    while not((middle == start) or (middle == stop)):
        if numbers_sorted[middle] < number_to_find:
            start = middle
            middle = (stop - start) // 2 + start
        elif numbers_sorted[middle] > number_to_find:
            stop = middle
            middle = (stop - start) // 2 + start
        else:
            return middle
    return None

READ_FROM_FILE = True

if READ_FROM_FILE:
    inp = open('input.txt').readline
else:
    inp = input

n = int(inp().strip())

skyscrapers = list(map(int, inp().strip().split()))
possible_heights = set(skyscrapers)
possible_heights_sorted = sorted(possible_heights)
available_heights = {k: 0 for k in possible_heights}

paths_count = 0
last_skyscraper = 1000001
for skyscraper in skyscrapers:
    paths_count += available_heights[skyscraper]
    available_heights[skyscraper] += 1
    if skyscraper > last_skyscraper:
        for height in possible_heights_sorted:
            if height == skyscraper:
                break
            available_heights[height] = 0
    last_skyscraper = skyscraper

print(paths_count * 2)