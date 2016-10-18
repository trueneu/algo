def are_parethesis_balanced(s):
    stack = list()
    opening_brace = {')': '(', ']': '[', '}': '{'}
    invalid = False
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c in [')', ']', '}']:
            if not len(stack) or stack.pop() != opening_brace[c]:
                invalid = True
                break

    return not invalid

print(are_parethesis_balanced('{[(])}'))