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


def contains_cycle(head):
    visited = set()
    n = head
    while n:
        if n in visited:
            return True
        visited.add(n)
        n = n.next
    return False


def contains_cycle2(head):
    n1 = n2 = head
    c = 0
    while n1:
        c += 1
        if c == 2:
            c = 0
            n2 = n2.next
        n1 = n1.next
        if n1 is n2:
            return True
    return False


print(contains_cycle2(a))
