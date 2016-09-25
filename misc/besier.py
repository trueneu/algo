from copy import deepcopy

def indices(n, d):
    if n == 1:
        r = list()
        r2 = list()
        r.append(d)
        r2.append(r)
        return r

    ll = list()
    for i in range(0, d + 1):
        r = indices(n - 1, d - i)
        l = list()
        l.append(i)
        for rrr in r:
            x = deepcopy(l)
            x.extend(rrr)
            ll.append(l)

    return ll

print(indices(3, 2))