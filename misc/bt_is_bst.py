import sys

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

a = BinaryTreeNode(10)
b = a.insert_left(5)
c = a.insert_right(15)
d = b.insert_left(1)
e = b.insert_right(9)
f = c.insert_left(11)
g = c.insert_right(20)

def bt_is_bst(root, lm, rm):
    if not (lm <= root.value < rm):
        return False
    if root.left:
        l = bt_is_bst(root.left, lm, root.value)
    else:
        l = True

    if root.right:
        r = bt_is_bst(root.right, root.value, rm)
    else:
        r = True

    if r and l:
        return True
    else:
        return False



print(bt_is_bst(a, -sys.maxsize, sys.maxsize))