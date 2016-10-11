s = 'abcdefg'


def reverse_string(s):
    char_list = [x for x in s]
    n = 0
    while n < len(char_list) // 2:
        char_list[n], char_list[-(n + 1)] = char_list[-(n + 1)], char_list[n] 
        n += 1
    return ''.join(char_list)


print(reverse_string(s))