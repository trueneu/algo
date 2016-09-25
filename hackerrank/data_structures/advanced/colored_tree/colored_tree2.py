class TreeNode:
    def __init__(self, index):
        self.children = list()
        self.color = None
        self.parent = None
        self.index = index
        self.color_amount = None

    def add_child(self, node):
        self.children.append(node)

    def rm_child(self, node):
        self.children.remove(node)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def has_one_child(self):
        return len(self.children) == 1

    def is_leaf(self):
        return len(self.children) == 0

    def set_color_amount(self, amount):
        self.color_amount = amount

    def get_color_amount(self):
        return self.color_amount

#f = open('colored_tree_input2.txt')
#nmroot = f.readline().strip()
nmroot = input().strip()

parts = nmroot.split()
n = int(parts[0])
m = int(parts[1])
root_node_index = int(parts[2])

nodes = dict()
leafs = list()

root = None

for i in range(0, n - 1):
    #node_link = [int(x) for x in f.readline().strip().split()]
    node_link = [int(x) for x in input().strip().split()]
    index1 = node_link[0]
    index2 = node_link[1]
    try:
        nodes[index1]
    except KeyError:
        nodes[index1] = TreeNode(index1)
    try:
        nodes[index2]
    except KeyError:
        nodes[index2] = TreeNode(index2)

    nodes[index1].add_child(nodes[index2])
    nodes[index2].add_child(nodes[index1])

root = nodes[root_node_index]
node_stack = [root]
while len(node_stack):
    curr_node = node_stack.pop()
    if not len(curr_node.get_children()):
        leafs.append(curr_node)

    for child in curr_node.get_children():
        child.set_parent(curr_node)
        child.rm_child(curr_node)
        node_stack.append(child)


for i in range(1, n + 1):
    #color = int(f.readline().strip())
    color = int(input().strip())
    nodes[i].set_color(color)

sets = [set() for _ in leafs]
next_nodes = list()
next_leaves = leafs
while len(next_leaves):
    next_leaves_new = list()
    sets_new = list()
    next_leaves_counter = 0
    parent_to_set_index = dict()

    for i, leaf in enumerate(next_leaves):
        sets[i].add(leaf.get_color())
        leaf.set_color_amount(len(sets[i]))
        curr_node = leaf.get_parent()

        while curr_node and curr_node.has_one_child():
            sets[i].add(curr_node.get_color())
            curr_node.set_color_amount(len(sets[i]))
            curr_node = curr_node.get_parent()
        if curr_node is None:
            break
        sets[i].add(curr_node.get_color())

        if curr_node not in parent_to_set_index.keys():
            parent_to_set_index[curr_node] = next_leaves_counter
            next_leaves_new.append(curr_node)
            sets_new.append(sets[i])
        else:
            sets_new[parent_to_set_index[curr_node]] = sets_new[parent_to_set_index[curr_node]].union(sets[i])

        curr_node.set_color_amount(sets_new[parent_to_set_index[curr_node]])

    next_leaves = next_leaves_new
    sets = sets_new

for i in range(0, m):
    #new_root = int(f.readline().strip())
    new_root = int(input().strip())
    print(nodes[new_root].get_color_amount())

