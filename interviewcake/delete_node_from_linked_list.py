from copy import deepcopy

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

head = a


def delete_node_linear_with_head(node):
    global head
    prev_node = None
    n = head
    while n:
        if n is node:
            break
        prev_node = n
        n = n.next
    else:
        print("Couldn't find the node")
        return None
    next_node = n.next
    if prev_node:
        prev_node.next = next_node
    else:
        head = next_node


def delete_node(node):
    try:
        node.next, node.value = node.next.next, node.next.value
    except AttributeError:
        node.value = None



def traverse(head):
    n = head
    print(n.value)
    while n.next:
        n = n.next
        print(n.value)

traverse(head)
