class Node:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data

f = Node(None, None, 6)
e = Node(None, None, 4)
d = Node(None, None, 1)
c = Node(f, None, 2)
b = Node(d, e, 5)
a = Node(b, c, 3)

def is_leaf(c):
    return c.left is None and c.right is None

class Queue:
    def __init__(self):
        self.q = []
        self.out = 0
    def push(self, seq):
        self.q.append(seq)
    def pop(self):
        k = self.q[self.out]
        self.out += 1
        return k
    def __len__(self):
        return len(self.q) - self.out

def preOrder(root):
    print(root.data)
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def height(root, h):
    h1 = h2 = 0
    if root.left:
        h1 = height(root.left, h + 1)
    if root.right:
        h2 = height(root.right, h + 1)
    return max(h1, h2, h)



print(height(a, 0))

