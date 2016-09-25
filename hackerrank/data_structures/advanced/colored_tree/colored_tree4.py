from collections import deque
import sys
from collections import Counter

class Node:
    def __init__(self, color, original_index, parent=None):
        self.children_nodes = []
        self.children_len = 0
        self.color = color
        self.original_index = original_index
        self.colors_cache = None
        self.colors_cache_len = 0
        self.parent = parent
        self.children_walked = 0

    def __repr__(self):
        return("Node {0}".format(self.original_index))


""" DEPTH FIRST SEARCH, recursive
def dfs(stack, node):
    stack.append(node)
    for child in node.children_nodes:
        dfs(stack, child)
"""

# DEPTH FIRST SEARCH, ITERATIVE
def dfs(stack, root):
    node = root
    stack.append(root)
    while node:
        if node.children_nodes and node.children_walked < node.children_len:
            next_node = node.children_nodes[node.children_walked]
            stack.append(next_node)
            node.children_walked += 1
            node = next_node
        else:
            node = node.parent

leafs = []

READ_FROM_FILE = True
DEBUG = False

f = None
if READ_FROM_FILE:
    f = open('colored_tree_input3.txt')
    nmroot = f.readline().strip()
else:
    nmroot = input().strip()

n, m, root_node_index = [int(x) for x in nmroot.split()]

sys.setrecursionlimit(max(sys.getrecursionlimit(), n))

#EDGES READ
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    if READ_FROM_FILE:
        edge = [int(x) for x in f.readline().strip().split()]
    else:
        edge = [int(x) for x in input().strip().split()]
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

#COLORS READ

if READ_FROM_FILE:
    colors = [0] + [int(f.readline().strip()) for _ in range(n)]
else:
    colors = [0] + [int(input().strip()) for _ in range(n)]

#TREE BUILD
stack = []
original_indexes_to_nodes = [None for _ in range(n + 1)]

root = Node(colors[root_node_index], root_node_index)
original_indexes_to_nodes[root_node_index] = root
stack.append(root)

while stack:
    curr_node = stack.pop()
    if not len(edges[curr_node.original_index]):
        leafs.append(curr_node)
    children_num = 0
    for child in edges[curr_node.original_index]:
        new_node = Node(colors[child], child, curr_node)
        curr_node.children_nodes.append(new_node)
        edges[child].remove(curr_node.original_index)
        original_indexes_to_nodes[child] = new_node
        stack.append(new_node)
        children_num += 1
    curr_node.children_len = children_num

#COLORS CACHE UP TO ROOT
"""
queue = deque(leafs[:])
while queue:
    curr_node = queue.popleft()
    if not curr_node.children_nodes:
        curr_node.colors_cache = {curr_node.color}
    elif len(curr_node.children_nodes) == 1:
        curr_node.colors_cache = set(curr_node.children_nodes[0].colors_cache)
        curr_node.colors_cache.add(curr_node.color)
    else:
        curr_node.colors_cache = set()
        for child in curr_node.children_nodes:
            curr_node.colors_cache = curr_node.colors_cache.union(child.colors_cache)
        curr_node.colors_cache.add(curr_node.color)
    if curr_node.parent and all([x.colors_cache for x in curr_node.parent.children_nodes]):
        queue.append(curr_node.parent)
"""

#COLORS CACHE UP TO ROOT 2
"""
queue = deque(leafs[:])
while queue:
    curr_node = queue.popleft()
    if not curr_node.children_nodes:
        curr_node.colors_cache = {curr_node.color}
        curr_node.colors_cache_len = 1
    elif len(curr_node.children_nodes) == 1:
        curr_node.colors_cache = curr_node.children_nodes[0].colors_cache
        curr_node.colors_cache.add(curr_node.color)
        curr_node.colors_cache_len = len(curr_node.colors_cache)
    else:
        curr_node.colors_cache = curr_node.children_nodes[0].colors_cache
        for i in range(1, len(curr_node.children_nodes)):
            child = curr_node.children_nodes[i]
            curr_node.colors_cache = curr_node.colors_cache.union(child.colors_cache)
        curr_node.colors_cache.add(curr_node.color)
        curr_node.colors_cache_len = len(curr_node.colors_cache)

    if curr_node.parent and all([x.colors_cache for x in curr_node.parent.children_nodes]):
        queue.append(curr_node.parent)
"""

#COLORS CACHE DOWN FROM ROOT AND BACK UP
stack = []
for child in root.children_nodes:
    dfs(stack, child)

#for n in stack:
#    print(n.original_index)

while stack:
    curr_node = stack.pop()
    if curr_node.parent.colors_cache:
        if curr_node.colors_cache:
            curr_node.colors_cache.add(curr_node.color)
            curr_node.parent.colors_cache = curr_node.parent.colors_cache.union(curr_node.colors_cache)
            curr_node.colors_cache_len = len(curr_node.colors_cache)
            del curr_node.colors_cache
        else:
            curr_node.parent.colors_cache.add(curr_node.color)
            curr_node.colors_cache_len = 1
    else:
        if curr_node.colors_cache:
            curr_node.parent.colors_cache = curr_node.colors_cache
            curr_node.parent.colors_cache.add(curr_node.color)
            curr_node.colors_cache_len = len(curr_node.parent.colors_cache)
        else:
            curr_node.parent.colors_cache = {curr_node.color}
            curr_node.colors_cache_len = 1

root.colors_cache.add(root.color)
root.colors_cache_len = len(root.colors_cache)


if DEBUG:
    print("Colors: {0}".format(colors))
    print("Edges: {0}".format(edges))
    print("Leafs: {0}".format([x.original_index for x in leafs]))
    print("Colors_cache: {0}".format([x.colors_cache for x in original_indexes_to_nodes if x is not None]))

#QUERIES FOR CACHE IMPL1
"""
for _ in range(m):
    if READ_FROM_FILE:
        query = int(f.readline().strip())
    else:
        query = int(input().strip())
    print(len(original_indexes_to_nodes[query].colors_cache))
"""

#QUERIES FOR CACHE IMPL2&3
for _ in range(m):
    if READ_FROM_FILE:
        query = int(f.readline().strip())
    else:
        query = int(input().strip())
    print(original_indexes_to_nodes[query].colors_cache_len)


#QUERIES BRUTE FORCE
"""
queue = deque()
for _ in range(m):
    if READ_FROM_FILE:
        query = int(f.readline().strip())
    else:
        query = int(input().strip())
    queue.append(original_indexes_to_nodes[query])
    result = set()
    while queue:
        curr_node = queue.popleft()
        if not curr_node.colors_cache:
            result.add(curr_node.color)
            queue.extend(curr_node.children_nodes)
        else:
            result = result.union(curr_node.colors_cache)
    original_indexes_to_nodes[query].colors_cache = result
    print(len(result))
"""