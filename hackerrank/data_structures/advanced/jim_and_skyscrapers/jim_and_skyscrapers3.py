READ_FROM_FILE = True

if READ_FROM_FILE:
    inp = open('input.txt').readline
else:
    inp = input

n = int(inp().strip())

skyscrapers = list(map(int, inp().strip().split()))

paths_count = 0
size = 0
heights = [0] * n
amounts = [0] * n

for skyscraper in skyscrapers:
    while size > 0 and heights[size - 1] < skyscraper:
        size -= 1
    if size < 1 or heights[size - 1] > skyscraper:
        heights[size] = skyscraper
        amounts[size] = 0
        size += 1

    paths_count += amounts[size - 1]
    amounts[size - 1] += 1

print(paths_count * 2)