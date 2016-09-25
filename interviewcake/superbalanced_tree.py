class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def tree_traversal(q):
    if not q:
        return
    for node in q:
        if node:
            print(node.value, end=' ')
        else:
            print('x', end=' ')
    newq = []
    for node in q:
        if node:
            newq.append(node.left)
            newq.append(node.right)
    print()
    tree_traversal(newq)


def bfs(q, depth=0, first_leaf_depth=None):
    if not q:
        if abs(depth - first_leaf_depth) <= 2:
            return True
        else:
            return False
    newq = []
    for node in q:
        if node.left:
            newq.append(node.left)
        if node.right:
            newq.append(node.right)
        if not node.left and not node.right and not first_leaf_depth:
            first_leaf_depth = depth
    return bfs(newq, depth + 1, first_leaf_depth)


def bfs_iterative(root):
    q = [root]
    depth = 0
    first_leaf_depth = None
    while q:
        newq = []
        for node in q:
            if node.left:
                newq.append(node.left)
            if node.right:
                newq.append(node.right)
            if not node.left and not node.right and not first_leaf_depth:
                first_leaf_depth = depth
        q = newq
        depth += 1

    if abs(depth - first_leaf_depth) <= 2:
        return True
    else:
        return False

root = BinaryTreeNode(0)
x = root.insert_left(1)
x = x.insert_left(2)
x.insert_left(3)
x = root.insert_right(4)

tree_traversal([root])

print(bfs([root]))

print(bfs_iterative(root))