f = open('plants.txt')
#n = int(input().strip())
n = int(f.readline().strip())

stack = list()
#plants = [int(x) for x in input().strip().split()]
plants = [int(x) for x in f.readline().strip().split()]

gen = 0
gen_max = 0

for plant in plants:
    if not len(stack):
        gen = 0
        stack.append((plant, gen))
    elif plant > stack[-1][0]:
        gen = 1
        stack.append((plant, gen))
    else:
        gen = 0
        while len(stack) and plant <= stack[-1][0]:
            gen = max(stack[-1][1] + 1, gen)
            stack.pop()
        if not len(stack):
            gen = 0
        stack.append((plant, gen))

    gen_max = max(gen, gen_max)

print(gen_max)
