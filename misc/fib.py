def fib(n):
    if n < 0:
        n = -n
    Phi = (1 + 5 ** 0.5) / 2
    phi = 1 / Phi
    f = int((Phi ** n - (-phi) ** n) / (5 ** 0.5))
    return f

print(fib(27))