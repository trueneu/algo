class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(n, head):
    n -= 1
    if n < 0:
        return None
    to_head = head
    to_kth = None
    counter = 0
    while to_head:
        if counter >= n:
            if to_kth is None:
                to_kth = head
            else:
                to_kth = to_kth.next
        to_head = to_head.next
        counter += 1
    return to_kth

print(kth_to_last_node(5, a).value)