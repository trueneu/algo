numbers_unsorted_reference = [10, 12, 11, 2, 1]

counter = 0

def inversion_count(numbers, start, middle, stop):
    global counter

    if len(numbers) == 1:
        return numbers

    # dividing
    left_numbers = numbers[start:middle]
    right_numbers = numbers[middle:stop]

    # conquering
    left_sorted = inversion_count(left_numbers, start, (middle - start) // 2, middle)
    right_sorted = inversion_count(right_numbers, 0, (stop - middle) // 2, (stop - middle))

    # merging
    merged = list()

    i = 0
    while len(left_sorted) and len(right_sorted):
        if left_sorted[0] <= right_sorted[0]:
            merged.append(left_sorted.pop(0))
        else:
            counter += len(left_sorted)
            merged.append(right_sorted.pop(0))
        i += 1
    merged.extend(left_sorted)
    merged.extend(right_sorted)

    return merged

numbers_unsorted = list(numbers_unsorted_reference)
counter = 0
inversion_count(numbers_unsorted, 0, len(numbers_unsorted) // 2, len(numbers_unsorted))
print(counter)
