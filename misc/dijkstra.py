import sys

n = 6

no_edge = sys.maxsize
max_dist = sys.maxsize

m = [[0,        7,      9,  no_edge,    no_edge,    14],
     [7,        0,      10,      15,    no_edge,      no_edge],
     [9,        10,      0,      11,    no_edge,     2],
     [no_edge,  15,     11,       0,          6,     no_edge],
     [no_edge,  no_edge, no_edge, 6,          0,     9],
     [14,       no_edge,       2, no_edge,    9,     0]]

def dijkstra(v, m):
    visited = [False] * len(m)
    distances = [max_dist] * len(m)
    prev = [None] * len(m)

    distances[v] = 0
    curr = v
    while True:
        for i, dist in enumerate(m[curr]):
            if distances[i] > distances[curr] + dist:
                prev[i] = curr
                distances[i] = distances[curr] + dist
        visited[curr] = True

        min_unvisited_dist = max_dist
        min_unvisited_index = None
        for i in range(0, len(m)):
            if distances[i] < min_unvisited_dist and not visited[i]:
                min_unvisited_dist = distances[i]
                min_unvisited_index = i
        if min_unvisited_index is None:
            break
        curr = min_unvisited_index
    return distances, prev


print(dijkstra(0, m))