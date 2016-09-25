numbers = [2, 8, 7, 1, 3, 5, 0, 5]


def partition(numbers, p, r):
    i = p - 1
    x = numbers[r]
    j = p
    while j < r:
        if numbers[j] <= x:
            i += 1
            numbers[j], numbers[i] = numbers[i], numbers[j]
        j += 1
    numbers[r], numbers[i+1] = numbers[i+1], numbers[r]
    return i+1


def quicksort(numbers, p, r):
    if p < r:
        q = partition(numbers, p, r)
        quicksort(numbers, p, q - 1)
        quicksort(numbers, q + 1, r)

quicksort(numbers, 0, len(numbers) - 1)
print(numbers)