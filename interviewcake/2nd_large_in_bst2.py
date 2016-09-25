from typing import Tuple


class BinaryTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None  # type: BinaryTreeNode
        self.right = None  # type: BinaryTreeNode

    def insert_left(self, value: int) -> 'BinaryTreeNode':
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value: int) -> 'BinaryTreeNode':
        self.right = BinaryTreeNode(value)
        return self.right

root = BinaryTreeNode(50)
x = root.insert_left(30)
x.insert_left(20)
x.insert_right(40)
# x = root.insert_right(80)
# x.insert_left(70)
# x = x.insert_right(90)
# x = x.insert_left(85)
# x.insert_right(88)


def largest_and_parent(root_node: BinaryTreeNode) -> Tuple[BinaryTreeNode, BinaryTreeNode]:
    node = root_node
    parent = None
    while node.right:
        parent = node
        node = node.right
    return node, parent


def second_large(root_node: BinaryTreeNode) -> BinaryTreeNode:
    largest, parent = largest_and_parent(root_node)
    if largest.left:
        return largest_and_parent(largest.left)[0]
    else:
        return parent

print(second_large(root).value)
