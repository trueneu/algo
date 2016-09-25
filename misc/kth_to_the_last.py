class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k, head):
    c = 1
    curr = head
    curr2 = None

    while curr.next is not None:
        if c == k:
            curr2 = head
        if curr2 is not None:
            curr2 = curr2.next
        curr = curr.next
        c += 1
    if c == k:
        curr2 = head
    return curr2


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node(5, a).value)
