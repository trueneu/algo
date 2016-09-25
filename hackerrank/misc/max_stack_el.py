import sys
f = open('max_stack_el_input.txt')
n = int(f.readline().strip())
#n = int(input().strip())

stack = list()
m = -sys.maxsize
for i in range(0, n):
    query = [int(x) for x in f.readline().strip().split()]
    #query = [int(x) for x in input().strip().split()]
    if query[0] == 1:
        el = query[1]
        m = max(m, el)
        stack.append((el, m))
    elif query[0] == 2:
        el, m2 = stack.pop()
        if len(stack):
            el2, m3 = stack[-1]
            m = min(m, m3)
        else:
            m = -sys.maxsize
    elif query[0] == 3:
        el, m2 = stack[-1]
        print(m2)