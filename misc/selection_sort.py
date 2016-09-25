numbers_unsorted_reference = [1, 0, 5, -2, 10, 7, -3, 6]


def selection_sort(numbers):
    if len(numbers) < 2:
        return
    i = 0
    while i < len(numbers) - 1:
        j = i + 1
        min_number = numbers[j]
        min_number_index = j
        while j < len(numbers):
            if numbers[j] < min_number:
                min_number = numbers[j]
                min_number_index = j
            j += 1
        if min_number < numbers[i]:
            numbers[i], numbers[min_number_index] = numbers[min_number_index], numbers[i]
        i += 1

numbers_unsorted = list(numbers_unsorted_reference)
selection_sort(numbers_unsorted)
print(numbers_unsorted)