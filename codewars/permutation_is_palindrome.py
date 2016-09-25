def permutation_is_palindrome(string):
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

print(permutation_is_palindrome("civic"))
print(permutation_is_palindrome("ivicc"))
print(permutation_is_palindrome("civil"))
print(permutation_is_palindrome("livci"))
