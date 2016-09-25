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

numbers_sorted = [-3, -2, 1, 5, 6, 7, 10, 12]
print(binary_search(numbers_sorted, 1))
