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

a = BinaryTreeNode(10)
b = a.insert_left(5)
c = b.insert_right(6)
d = c.insert_right(7)
e = d.insert_right(8)
f = e.insert_right(9)

c = 0

def second_large_bst(root):
    if root.right:
        curr = root.right
        while curr.right:
            parent = curr
            curr = curr.right
        return parent.value
    else:
        curr = root.left
        if curr.right:
            while curr.right:
                curr = curr.right
            return curr.value
        else:
            return curr.value

print(second_large_bst(a))
