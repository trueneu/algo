numbers_unsorted_reference = [1, 10, -1, 4, 7, 7, 5]


def merge_sort(numbers, start, middle, stop):
    if len(numbers) == 1:
        return numbers

    # dividing
    left_numbers = numbers[start:middle]
    right_numbers = numbers[middle:stop]

    # conquering
    left_sorted = merge_sort(left_numbers, start, (middle - start) // 2, middle)
    right_sorted = merge_sort(right_numbers, 0, (stop - middle) // 2, (stop - middle))

    # merging
    merged = list()

    i = 0
    max_i = min(len(left_sorted), len(right_sorted))
    while len(left_sorted) and len(right_sorted):
        if left_sorted[0] <= right_sorted[0]:
            merged.append(left_sorted.pop(0))
        else:
            merged.append(right_sorted.pop(0))
        i += 1
    merged.extend(left_sorted)
    merged.extend(right_sorted)

    return merged

numbers_unsorted = list(numbers_unsorted_reference)
numbers_sorted = merge_sort(numbers_unsorted, 0, len(numbers_unsorted) // 2, len(numbers_unsorted))

print(numbers_sorted)
