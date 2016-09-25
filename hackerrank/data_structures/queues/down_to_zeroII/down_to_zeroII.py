import sys


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

def tree_build2(n, known_results):
    c = c_addition = 0
    parent = 0
    q = {n: None}
    history = []
    get_out = False

    while 0 not in q:
        history.append(q)
        new_q = {}
        for x in q:
            if x in known_results:
                parent = q[x]
                c_addition = min([v for k, v in known_results.items() if k in q])
                history = history[:-1]
                get_out = True
                break

            d = find_all_divisors(x)
            if d:
                for dd in d:
                    new_q[dd] = x
            new_q[x - 1] = x
        if get_out:
            break
        q = new_q
        c += 1
    else:
        parent = q[0]
    i = -1
    counter = c_addition + 1
    while parent:
        known_results[parent] = counter
        parent = history[i][parent]
        i -= 1
        counter += 1

    return c + c_addition

q = int(inp().strip())
known = {}
original_queries = []

for i in range(q):
    n = int(inp().strip())
    original_queries.append(n)

sorted_queries = sorted(original_queries)
for n in sorted_queries:
    c = tree_build2(n, known)
    known[n] = c

for n in original_queries:
    print(known[n])


