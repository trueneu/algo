f = open('ANDxorOR.txt')

#n = int(input().strip())
n = int(f.readline().strip())

#a = list(map(int, input().strip().split()))
a = list(map(int, f.readline().strip().split()))

stack = list()

m = 0

a.append(0)
i = 0
while i < n + 1:
    if (not len(stack)) or a[i] > stack[-1]:
        stack.append(a[i])
        i += 1
    else:
        l = stack.pop()
        if len(stack):
            m = max(m, l ^ stack[-1])

stack = list()
a.pop()
a.insert(0, 0)
i = n
while i >= 0:
    if (not len(stack)) or a[i] > stack[-1]:
        stack.append(a[i])
        i -= 1
    else:
        l = stack.pop()
        if len(stack):
            m = max(m, l ^ stack[-1])

print(m)