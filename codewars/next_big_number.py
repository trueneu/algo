from math import log


def next_bigger(n):
    digits = [(n // 10 ** x) % 10 for x in range(0, int(log(n, 10)) + 1)]
    print(n)
    for i, digit in enumerate(digits):
        digits_bigger_than = [x for x in digits[:i] if x > digit]
        if digits_bigger_than:
            min_digit_bigger_than = min(digits_bigger_than)
            min_digit_index = digits[:i].index(min_digit_bigger_than)
            digits.pop(min_digit_index)
            digits.insert(i, min_digit_bigger_than)

            digits[:i] = sorted(digits[:i], reverse=True)

            r = 0
            for index, d in enumerate(digits):
                r += 10 ** index * d
            return r
    return -1

print(next_bigger(59884848459853))