numbers = [1, 2, 6, 5, 9]


def multiply_before(numbers, product_list):
    pr = 1
    for i, _ in enumerate(numbers):
        if i == 0:
            continue
        pr *= numbers[i - 1]
        product_list[i] = pr * product_list[i]

def product_of_other(numbers):
    nmb = [1] * len(numbers)
    multiply_before(numbers, nmb)
    nmb = nmb[::-1]
    multiply_before(numbers[::-1], nmb)
    nmb = nmb[::-1]
    return nmb

print(product_of_other(numbers))

