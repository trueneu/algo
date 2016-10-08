class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')

a.next = a
b.next = c
c.next = d
# d.next = b


def contains_cycle(head):
    visited = set()
    n = head
    while n:
        if n in visited:
            return True
        visited.add(n)
        n = n.next
    return False

print(contains_cycle(a))
