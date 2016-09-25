from collections import deque

def bfs(x, counter, queue, visited):

    sqrt_x = int((x ** 0.5) + 0.5)
    for i in range(2, sqrt_x + 1):
        if x % i == 0:
            x_next = max(i, x // i)
            if not visited[x_next]:
                visited[x_next] = True
                queue.append((x_next, counter + 1))

    if x and not visited[x - 1]:
        visited[x - 1] = True
        queue.append((x - 1, counter + 1))

READ_FROM_FILE = True

if READ_FROM_FILE:
    inp = open('input.txt').readline
else:
    inp = input

q = int(inp().strip())

for i in range(q):
    queue = deque()
    visited = [False] * 1000000
    n = int(inp().strip())
    c = 0
    queue.append((n, 0))
    while queue:
        x, counter = queue.popleft()
        if x == 0:
            c = counter
            break
        bfs(x, counter, queue, visited)
    print(c)

