string = "dcbdcbx"

def longest_substring_greater(string):
    i = 1
    sub_begin = -1
    sub_end = -2
    sub_begin_max = -1
    sub_end_max = -2
    greater_flag = False

    while i < len(string):
        if sub_begin == -1:
            if string[i] >= string[0]:
                greater_flag = False
                sub_begin = i
                sub_end = i
            if string[i] > string[0]:
                greater_flag = True
        else:
            if string[i] > string[i - sub_begin]:
                greater_flag = True
                sub_end = i
            elif string[i] == string[i - sub_begin]:
                sub_end = i
            else:
                if greater_flag and (sub_end_max - sub_begin_max < sub_end - sub_begin):
                    sub_end_max, sub_begin_max = sub_end, sub_begin
                sub_begin = -1
        i += 1
    if greater_flag and (sub_end_max - sub_begin_max < sub_end - sub_begin):
        sub_end_max, sub_begin_max = sub_end, sub_begin
    return string[sub_begin_max:sub_end_max + 1]

print(longest_substring_greater(string))