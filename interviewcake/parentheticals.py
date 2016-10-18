def get_closing_parenth_index(s, opening_parenth_index):
    stack = []
    opening_parenth_stack_pos = None
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
            if i == opening_parenth_index:
                opening_parenth_stack_pos = len(stack) - 1
        elif c == ')':
            stack.pop()
            if len(stack) == opening_parenth_stack_pos:
                return i
        if i > opening_parenth_index and opening_parenth_stack_pos is None:
            print('No opening parenth at that index. YOU LIE (c) Arnold')
            return None
    print('Could not find closing parenth')


def get_closing_parenth_index_o1_mem(s, opening_parenth_index):
    opening_parenth_pos = None
    parenth_count = 0
    for i, c in enumerate(s):
        if c == '(':
            parenth_count += 1
            if i == opening_parenth_index:
                opening_parenth_pos = parenth_count
        elif c == ')':
            parenth_count -= 1
            if parenth_count == opening_parenth_pos - 1:
                return i
        if i > opening_parenth_index and opening_parenth_pos is None:
            print('No opening parenth at that index. YOU LIE (c) Arnold')
            return None
    print('Could not find closing parenth')


print(get_closing_parenth_index_o1_mem('Sometimes (when I nest them (my parentheticals) '
                                'too much (like this (and this))) they get confusing.', 10))
print(get_closing_parenth_index_o1_mem('Sometimes (when I nest them (my parentheticals) '
                                'too much (like this (and this))) they get confusing.', 11))
print(get_closing_parenth_index_o1_mem('Sometimes (when I nest them (my parentheticals) '
                                'too much (like this (and this)) they get confusing.', 10))
print(get_closing_parenth_index_o1_mem('()', 0))