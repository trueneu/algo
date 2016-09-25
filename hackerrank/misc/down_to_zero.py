# f = open('primes_big.txt')
# primes = list()
# for line in f.readlines():
#     primes.extend([int(x) for x in line.split()])
# print(primes)


f = open('down_to_zero_input.txt')
q = int(f.readline().strip())
#q = int(input().strip())

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(0, q):
    x = int(f.readline().strip())
    #x = int(input().strip())
    print(is_prime(x))
