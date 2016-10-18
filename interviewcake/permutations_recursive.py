from itertools import permutations


def permutations_recursive(s):
    if len(s) == 1:
        return {s}
    elif len(s) == 2:
        return {s, ''.join(reversed(s))}
    p1 = {x[:i] + s[0] + x[i:] for x in permutations_recursive(s[1:]) for i in range(0, len(x) + 1)}
    return p1


def test(s):
    print(permutations_recursive(s))
    print(len(permutations_recursive(s)))
    print(len(list(permutations(s))))

test('abcdefghijklmnop')

