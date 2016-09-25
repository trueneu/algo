integers = [1]


def product_of_others(array):
    result = [1] * len(array)

    accumulator = 1
    for i in range(len(array)):
        result[i] *= accumulator
        accumulator *= array[i]

    accumulator = 1
    for i in reversed(range(len(array))):
        result[i] *= accumulator
        accumulator *= array[i]
    return result

print(product_of_others(integers))
