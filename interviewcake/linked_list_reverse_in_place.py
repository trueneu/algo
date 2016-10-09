class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')

a.next = b
b.next = c
c.next = d
d.next = None


def reverse_in_place(head):
    if head is None:
        return None
    prev_n = None
    n = head
    next_n = n.next
    while next_n:
        n.next = prev_n
        prev_n = n
        n = next_n
        next_n = n.next
    n.next = prev_n
    return n


def traverse(head):
    n = head
    print(n.value)
    while n.next:
        n = n.next
        print(n.value)


traverse(reverse_in_place(a))

