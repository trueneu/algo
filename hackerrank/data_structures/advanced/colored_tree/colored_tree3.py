f = open('colored_tree_input1.txt')
nmroot = f.readline().strip()
#nmroot = input().strip()

parts = nmroot.split()
n = int(parts[0])
m = int(parts[1])
root_node_index = int(parts[2])

nodes = dict()
colors = dict()
tree = [None] * (2 ** (n - 1) - 2)
nodes_positions = dict()
amounts = [None] * (2 ** (n - 1) - 2)

def get_left_child(index):
    global tree
    return tree[2*index + 1]


def get_right_child(index):
    global tree
    return tree[2*index + 2]


def set_left_child(index, value):
    p = 2*index + 1
    tree[p] = value
    return p


def set_right_child(index, value):
    p = 2*index + 2
    tree[p] = value
    return p


def get_left_child_index(index):
    return 2*index + 1


def get_right_child_index(index):
    return 2*index + 2


root = None

for i in range(0, n - 1):
    node_link = [int(x) for x in f.readline().strip().split()]
    #node_link = [int(x) for x in input().strip().split()]
    link1 = node_link[0]
    link2 = node_link[1]

    try:
        nodes[link1]
    except KeyError:
        nodes[link1] = list()

    try:
        nodes[link2]
    except KeyError:
        nodes[link2] = list()

    nodes[link1].append(link2)
    nodes[link2].append(link1)

tree[0] = root_node_index
nodes_positions[root_node_index] = 0
curr_index = 0
index_stack = list()

for i in range(1, n + 1):
    color = int(f.readline().strip())
    #color = int(input().strip())
    colors[i] = color

for i in range(0, n - 1):
    for index, child in enumerate(nodes[tree[curr_index]]):
        if index == 0:
            next_index = set_left_child(curr_index, child)
        elif index == 1:
            next_index = set_right_child(curr_index, child)
        else:
            print("Achtung! The fucking tree is not binary!")
            next_index = -1

        index_stack.append(next_index)
        nodes_positions[child] = next_index
        nodes[child].remove(tree[curr_index])

    tree[curr_index] = colors[tree[curr_index]]
    curr_index = index_stack.pop()
tree[curr_index] = colors[tree[curr_index]]

# color_dict = dict()
# for index, color in enumerate(tree):
#     if color is None:
#         continue
#     color_dict[color] = 0
#     amounts[index] = len(color_dict)
#
# print(tree)
# print(amounts)


for i in range(0, m):
    color_dict = dict()
    new_root = int(f.readline().strip())
    #new_root = int(input().strip())
    j = nodes_positions[new_root]
    while j < len(tree):
        if tree[j] is None:
            j += 1
            continue
        color_dict[tree[j]] = 0
        j += 1
    print(len(color_dict))





