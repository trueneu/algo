a = [1, 2, 3]
x = 2
n = len(a)


def polynom_horner(a, n, x):
    y = 0
    i = n
    while i > 0:
        i -= 1
        y = a[i] + x * y
    return y


def polynom_common(a, n, x):
    i = 0
    y = 0
    while i < n:
        j = 0
        x_pow_i = 1
        while j < i:
            x_pow_i *= x
            j += 1
        y += a[i] * x_pow_i
        i += 1
    return y

print(polynom_horner(a, n, x))
print(polynom_common(a, n, x))

