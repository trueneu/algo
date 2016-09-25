import sys


class TreeNode:
    def __init__(self, color=0, children=[]):
        self.children = children
        self.color = color

    def add_child(self, node):
        self.children.append(node)

    def set_color(self, color):
        self.color = color

    def get_children(self):
        return self.children

    def is_leaf(self):
        return len(self.children) == 0

f = open('colored_tree_input2.txt')
nmroot = f.readline().strip()
#nmroot = input().strip()

parts = nmroot.split()
n = int(parts[0])
m = int(parts[1])
root_node_index = int(parts[2])

nodes = dict()

root = None

edges = dict()

for i in range(0, n - 1):
    edge_index1, edge_index2 = [int(x) for x in f.readline().strip().split()]
    #edge_index1, edge_index2 = [int(x) for x in input().strip().split()]

    try:                edges[edge_index1].append(edge_index2)
    except KeyError:    edges[edge_index1] = [edge_index2]
    try:                edges[edge_index2].append(edge_index1)
    except KeyError:    edges[edge_index2] = [edge_index1]

nodes[root_node_index] = TreeNode(children=edges[root_node_index])
for child in nodes[root_node_index].get_children():
    edges[child].remove(root_node_index)
    nodes[child] = TreeNode(children=edges[child])

nodes_to_look_at = edges[root_node_index]

while len(nodes_to_look_at):
    new_nodes_to_look_at = list()
    for node_index in nodes_to_look_at:
        children = nodes[node_index].get_children()
        for child in children:
            edges[child].remove(node_index)
            nodes[child] = TreeNode(children=edges[child])
        new_nodes_to_look_at.extend(children)
    nodes_to_look_at = new_nodes_to_look_at

sys.exit(0)






for i in range(1, n + 1):
    color = int(f.readline().strip())
    #color = int(input().strip())
    nodes[i].set_color(color)

for i in range(0, m):
    new_root = int(f.readline().strip())
    #new_root = int(input().strip())

    colors = dict()
    nodes_to_look_at = [nodes[new_root]]
    while len(nodes_to_look_at):
        j = 0
        max_j = len(nodes_to_look_at)
        while j < max_j:
            colors[nodes_to_look_at[0].color] = 0
            children = nodes_to_look_at[0].get_children()
            if len(children):
                nodes_to_look_at.extend(children)
            nodes_to_look_at.pop(0)
            j += 1
    print(len(colors))




