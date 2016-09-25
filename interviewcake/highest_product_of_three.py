import sys

list_of_ints = [-10, 0, 1]


def find_min_and_pop(l):
    m = sys.maxsize
    i = 0
    for index, item in enumerate(l):
        if item < m:
            m = item
            i = index
    return l.pop(i)


def find_max_and_pop(l):
    m = -sys.maxsize
    i = 0
    for index, item in enumerate(l):
        if item > m:
            m = item
            i = index
    return l.pop(i)


def highest_product_of_three(l):
    """
    O(n * logn) approach

    sorted_l = sorted(l)
    product_first_two = sorted_l[0] * sorted_l[1]
    product_last_two = sorted_l[-1] * sorted_l[-2]
    return max(product_first_two * sorted_l[-1], product_last_two * sorted_l[-3])
    """
    assert len(l) >= 3

    lowest = find_min_and_pop(l)
    second_lowest = find_min_and_pop(l)
    highest = find_max_and_pop(l)
    try:
        second_highest = find_max_and_pop(l)
    except IndexError:
        second_highest = second_lowest

    try:
        third_highest = find_max_and_pop(l)
    except IndexError:
        third_highest = lowest


    product_first_two = lowest * second_lowest
    product_last_two = highest * second_highest
    return max(product_first_two * highest, product_last_two * third_highest)

print(highest_product_of_three(list_of_ints))
