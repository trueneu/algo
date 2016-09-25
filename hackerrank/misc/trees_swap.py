import sys
sys.setrecursionlimit(2000)

class TreeNode:
    def __init__(self, data=None):
        self.right = None
        self.left = None
        self.parent = None
        self.data = data
        self.depth = 1

def in_order(root):
    if root.left:
        in_order(root.left)
    print(root.data, end=" ")
    if root.right:
        in_order(root.right)


def swap_children(node):
    node.left, node.right = node.right, node.left

f = open('trees_swap_input.txt')
n = int(f.readline().strip())
# n = int(input().strip())

d = 0
nodes = [TreeNode(i + 1) for i in range(0, n)]
for i in range(0, n):
    children = [int(x) for x in f.readline().strip().split()]
    # children = [int(x) for x in input().strip().split()]
    if children[0] != -1:
        nodes[i].left = nodes[children[0] - 1]
        nodes[children[0] - 1].parent = nodes[i]
        nodes[children[0] - 1].depth = nodes[i].depth + 1

    if children[1] != -1:
        nodes[i].right = nodes[children[1] - 1]
        nodes[children[1] - 1].parent = nodes[i]
        nodes[children[1] - 1].depth = nodes[i].depth + 1

t = int(f.readline().strip())
# t = int(input().strip())

for i in range(0, t):
    k = int(f.readline().strip())
    # k = int(input().strip())
    x = list(filter(lambda x: x.depth % k == 0, nodes))
    for u in x:
        swap_children(u)
    in_order(nodes[0])
    print("")








