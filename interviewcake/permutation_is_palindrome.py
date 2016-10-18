def permutation_is_palindrome1(string):
    char_count = dict()
    odd_seen = False
    for char in string:
        if char not in char_count.keys():
            char_count[char] = 0
        char_count[char] += 1
    for k, v in char_count.items():
        if v % 2 == 1:
            if odd_seen:
                return False
            else:
                odd_seen = True
    return True


from collections import Counter


def permutation_is_palindrome2(string):
    char_count = Counter(string)
    odd_seen = False
    for c in char_count:
        if char_count[c] % 2 == 1 and len(string) % 2 == 0:
            return False
        elif char_count[c] % 2 == 1:
            if odd_seen:
                return False
            odd_seen = True
    return True

print(permutation_is_palindrome2("civvica"))
print(permutation_is_palindrome2("ivicc"))
print(permutation_is_palindrome2("civil"))
print(permutation_is_palindrome2("livci"))
