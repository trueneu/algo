import sys
def find_max_divisor(n):
    sqrt_n = int((n ** 0.5) + 0.5)
    for x in range(sqrt_n, 1, -1):
        if n % x == 0:
            return n // x

def find_all_divisors(n):
    res = []
    sqrt_n = int((n ** 0.5) + 0.5)
    for x in range(sqrt_n, 1, -1):
        if n % x == 0:
            res.append(n // x)
    return res

READ_FROM_FILE = True

if READ_FROM_FILE:
    inp = open('input.txt').readline
else:
    inp = input

def tree_build2(n):
    c = 0
    q = [n]
    while 0 not in q:
        new_q = []
        for x in q:
            d = find_all_divisors(x)
            if d:
                for dd in d:
                    new_q.append(dd)
            new_q.append(x - 1)
        q = new_q
        c += 1
    return c


def tree_build(n):
    c = 0
    q = [n]
    while 0 not in q:
        new_q = []
        for x in q:
            d = find_max_divisor(x)
            if d:
                new_q.append(d)
            new_q.append(x - 1)
        q = new_q
        c += 1
    return c

print(tree_build2(26))
sys.exit(0)


q = int(inp().strip())
for _ in range(q):
    n = int(inp().strip())
    print(tree_build2(n))


