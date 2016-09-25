READ_FROM_FILE = True

if READ_FROM_FILE:
    inp = open('input.txt').readline
else:
    inp = input

n = int(inp().strip())

skyscrapers = list(map(int, inp().strip().split()))

stack = []

stack.append(skyscrapers[0])

paths_count = 0

i = 1
while i < len(skyscrapers):
    last_skyscraper = stack[-1]
    curr_skyscraper = skyscrapers[i]
    if curr_skyscraper < last_skyscraper:
        stack.append(curr_skyscraper)
    else:
        queue = []
        while len(stack) and last_skyscraper <= curr_skyscraper:
            if last_skyscraper == curr_skyscraper:
                paths_count += 1
                queue.append(stack.pop())
            else:
                stack.pop()
            try:
                last_skyscraper = stack[-1]
            except IndexError:
                pass
        stack.extend(queue)

        stack.append(curr_skyscraper)
    i += 1

print(paths_count * 2)