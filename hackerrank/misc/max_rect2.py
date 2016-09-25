f = open('max_rect_input.txt')
#n = int(input().strip())
n = int(f.readline().strip())

#heights = [int(x) for x in input().strip().split()]
heights = [int(x) for x in f.readline().strip().split()]

stack = list()  # (index, height) tuples
m = 0
i = 0
while i < n:
    h = heights[i]
    if (not len(stack)) or h >= stack[-1][1]:
        stack.append((i, h))
        i += 1
    else:
        i_p, h_p = stack.pop()
        m2 = h_p * (i - stack[-1][0] - 1 if len(stack) else i)
        m = max(m2, m)

while len(stack):
    i_p, h_p = stack.pop()
    m2 = h_p * (i - stack[-1][0] - 1 if len(stack) else i)
    m = max(m2, m)
print(m)

