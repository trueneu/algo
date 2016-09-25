l = [-10, -10, 1, 3, 2]


def biggest_product_of_three(l):
    sorted_l = sorted(l)
    max1, max2 = sorted_l[-1], sorted_l[-2]
    min1, min2 = sorted_l[0], sorted_l[1]
    max_prod = max1 * max2
    min_prod = min1 * min2
    return max([max_prod * sorted_l[-3], min_prod * sorted_l[-1]])

print(biggest_product_of_three(l))
