def ar_prog_sum(n, d):
    return d * n * (n + 1) // 2

#n = int(input().strip())
n = 1
for i in range(0, n):
    #k = int(input().strip())
    k = 100
    threes = (k - 1) // 3
    fives = (k - 1) // 5
    fifteens = fives // 3
    print(ar_prog_sum(threes, 3) + ar_prog_sum(fives, 5) - ar_prog_sum(fifteens, 15))
