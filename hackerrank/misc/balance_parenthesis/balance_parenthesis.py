f = open('balance_parenthesis_input_reduced.txt')
#n = int(input().strip())
n = int(f.readline().strip())
stack = list()
opening_brace = {')': '(', ']': '[', '}': '{'}
for i in range(0, n):
    invalid = False
    #line = input().strip()
    line = f.readline().strip()
    for c in line:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c in [')', ']', '}']:
            if not len(stack) or stack.pop() != opening_brace[c]:
                invalid = True
                break

    print("NO") if invalid else print("YES")