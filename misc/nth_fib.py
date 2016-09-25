def nth_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fn2 = 0
    fn1 = 1
    for i in range(1, n):
        fnn = fn1 + fn2
        fn1, fn2 = fnn, fn1
    return fnn

print(nth_fib(60))