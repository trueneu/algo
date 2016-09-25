import sys

sys.stdin = open("colored_tree_input3.txt")

lines = sys.stdin.readlines()

N, M, root = map(int, lines[0].split(' '))
edges = [list() for _ in range(N)]

for i in range(1, N):
    x, y = map(int, lines[i].split(' '))
    edges[x - 1].append(y - 1)
    edges[y - 1].append(x - 1)

id = list(map(int, lines[N:2 * N]))
counting = [0 for _ in range(N)]
colors = [set() for _ in range(N)]


def join(x=set(), y=set()):
    if len(x) < len(y):
        return join(y, x)
    for _ in y:
        x.add(_)
    y.clear()
    return x


def visit(x):
    queue = list()
    queue.append(x)
    counting[x] = -1
    v = 0
    while v < len(queue):
        x = queue[v]
        for y in edges[x]:
            if counting[y] == 0:
                counting[y] = -1
                queue.append(y)
        v += 1
    return queue


def getSub(x):
    global counting
    global id
    _all = set()
    _all.add(id[x])
    for y in edges[x]:
        if counting[y] > 0:
            _all = join(_all, colors[y])
    colors[x] = _all
    counting[x] = len(_all)


order = visit(root - 1)
for i in range(N):
    getSub(order[N - 1 - i])

for i in range(2 * N, 2 * N + M):
    print(counting[int(lines[i]) - 1])