def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


def fib(n):
    if n < 0:
        raise Exception("Index was negative. No such thing as a negative index in a series.")
    fib_gen = fib_generator(n)
    for x in fib_gen:
        pass
    return x

print(fib(20))