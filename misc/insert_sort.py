numbers_unsorted_reference = [1, 0, 5, -2, 10, 7, -3, 6]


def insert_sort(numbers):
    if len(numbers) < 2:
        return numbers
    i = 1

    while i < len(numbers):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
        i += 1
    return numbers


def insert_sort_desc(numbers):
    if len(numbers) < 2:
        return
    i = 1

    while i < len(numbers):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] < key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
        i += 1


def insert_sort_recursive(numbers, number_to_insert):
    if len(numbers) == 1:
        return numbers

    numbers_remainder_sorted = insert_sort_recursive(numbers[:-1], numbers[-1])
    i = 0
    while i < len(numbers_remainder_sorted):
        if number_to_insert <= numbers_remainder_sorted[i]:
            numbers_remainder_sorted.insert(i, number_to_insert)
            break
        i += 1
    if i == len(numbers_remainder_sorted):
        numbers_remainder_sorted.append(number_to_insert)
    return numbers_remainder_sorted

numbers_unsorted = list(numbers_unsorted_reference)
insert_sort(numbers_unsorted)
print(numbers_unsorted)

numbers_unsorted = list(numbers_unsorted_reference)
insert_sort_desc(numbers_unsorted)
print(numbers_unsorted)

numbers_unsorted = list(numbers_unsorted_reference)
numbers_sorted = insert_sort_recursive(numbers_unsorted[:-1], numbers_unsorted[-1])
print(numbers_sorted)