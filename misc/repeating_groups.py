repeating_group_field = ['a', 'b', 'c']

ddata = ['l', 'm', 'n', 2, 'a', 'b', 'a', 'c', 'b', 'g', 'h', 2, 'c', 'c', 'l', 2, 'b', 'b']

# output = ['l', 'm', 'n', [['a', 'b'],['a', 'c', 'b']], 'g', 'h', [['c'], ['c']], 'l', 2, [[b], [b]]]


def chew_data(data):
    def check_type(char):
        nonlocal inside_group
        if type(char) is int:
            inside_group = True
        else:
            inside_group = False
            return char

    inside_group = False
    group_delimiter = ''
    group_result = []
    subgroup_result = []
    for c in data:
        if not inside_group:
            if check_type(c):
                yield c
        else:
            if c == group_delimiter:
                group_result.append(subgroup_result)
                subgroup_result = []
            if not group_delimiter:
                group_delimiter = c
            if c in repeating_group_field:
                subgroup_result.append(c)
            else:
                group_result.append(subgroup_result)
                subgroup_result = []
                yield group_result
                group_result = []
                group_delimiter = ''
                if check_type(c):
                    yield c
    group_result.append(subgroup_result)
    yield group_result

print([x for x in chew_data(ddata)])


