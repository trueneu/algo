from math import inf
from itertools import takewhile


def max_duffel_bag_value(cake_tuples, cap):
    if cap <= 0:
        return 0
    for cake_tuple in cake_tuples:
        if cake_tuple[0] == 0 and cake_tuple[1] > 0:
            return inf

    cake_tuples = sorted(cake_tuples)
    max_values_by_capacity = [0]
    for capacity in range(1, cap + 1):
        max_values_by_capacity.append(0)
        for volume, value in takewhile(lambda x: x[0] <= capacity, cake_tuples):
            max_values_by_capacity[capacity] = max(max_values_by_capacity[capacity],
                                                   value + max_values_by_capacity[capacity - volume])

    return max_values_by_capacity[-1]


cake_tuples = [(3, 40), (5, 70), (0, 1)]
capacity = 8
print(max_duffel_bag_value(cake_tuples, capacity))
