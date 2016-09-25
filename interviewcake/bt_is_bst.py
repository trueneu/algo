import sys
from typing import Tuple


class BinaryTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value: int) -> 'BinaryTreeNode':
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value: int) -> 'BinaryTreeNode':
        self.right = BinaryTreeNode(value)
        return self.right

root = BinaryTreeNode(50)
x = root.insert_left(30)
x.insert_left(20)
x.insert_right(60)
x = root.insert_right(80)
x.insert_left(70)
x.insert_right(90)


class NotBSTError(Exception):
    pass


def min_max_subtree(node: BinaryTreeNode) -> Tuple[int, int]:
    if node.left:
        left_min, left_max = min_max_subtree(node.left)
        if max(left_min, left_max) >= node.value:
            raise NotBSTError('Eat my shorts')
    else:
        left_min, left_max = sys.maxsize, -sys.maxsize

    if node.right:
        right_min, right_max = min_max_subtree(node.right)
        if min(right_min, right_max) <= node.value:
            raise NotBSTError('Eat my shorts')
    else:
        right_min, right_max = sys.maxsize, -sys.maxsize

    return min(left_min, right_min, node.value), max(left_max, right_max, node.value)


def bt_is_bst(root_node):
    try:
        min_max_subtree(root_node)
        print("it's bst")
    except NotBSTError:
        print("it's not bst")


bt_is_bst(root)