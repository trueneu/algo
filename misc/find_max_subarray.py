import sys

numbers = [1, 0, -15, 5, -2, 10, 7, -3, 6]


def find_max_crossing_subarray(arr, mid):
    left_sum = -sys.maxsize - 1
    subsum = left = 0
    i = mid - 1
    while i >= 0:
        subsum += arr[i]
        if subsum > left_sum:
            left_sum = subsum
            left = i
        i -= 1

    right_sum = -sys.maxsize - 1

    subsum = right = 0
    i = mid
    while i < len(arr):
        subsum += arr[i]
        if subsum > right_sum:
            right_sum = subsum
            right = i
        i += 1

    return left_sum + right_sum, left, right


def find_max_subarray(arr, left, right):
    if len(arr) == 1:
        return arr[0], left, right

    mid = (right - left) // 2

    left_sum, left_left, left_right = find_max_subarray(arr[left:mid], 0, mid)
    right_sum, right_left, right_right = find_max_subarray(arr[mid:right], 0, right - mid)
    cross_sum, cross_left, cross_right = find_max_crossing_subarray(arr, mid)

    if left_sum > right_sum and left_sum > cross_sum:
        return left_sum, left_left, left_right

    if right_sum > left_sum and right_sum > cross_sum:
        return right_sum, right_left + mid, right_right + mid

    if cross_sum >= right_sum and cross_sum >= left_sum:
        return cross_sum, cross_left, cross_right


def find_max_subarray_linear(arr):
    if len(arr) == 1:
        return arr[0], 0, 0
    if len(arr) < 1:
        raise Exception()

    i = 0
    left_left = 0
    left_right = 0
    right_left = 0
    right_right = 0

    left_summ = arr[0]
    right_summ = arr[0]
    #while i < len(arr) - 1:
    #    if
    #return summ, left, right

print(find_max_subarray(numbers, 0, len(numbers)))
print(find_max_subarray_linear(numbers))

