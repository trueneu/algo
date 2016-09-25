class LinkedListNode:
    def __init__(self, value, next=None):
        self.data = value
        self.next  = next

class Node:
    def __init__(self, value, next=None, prev=None):
        self.data = value
        self.next  = next
        self.prev  = prev

a = LinkedListNode(1)
b = LinkedListNode(3)
c = LinkedListNode(6)
d = LinkedListNode(7)

e = LinkedListNode(2)
f = LinkedListNode(3)
g = LinkedListNode(4)

a.next = b
b.next = c
c.next = d

e.next = f
f.next = g

def ll_has_cycle(head):
    visited = []
    curr = head
    while curr.next:
        if curr in visited:
            return True
        visited.append(curr)
        curr = curr.next
    return False

def merge(headA, headB):
    if not headA:
        return headB
    if not headB:
        return headA

    c_a = headA
    c_b = headB
    if c_a.data <= c_b.data:
        prev_node = c_a
        new_head = headA
        c_a = c_a.next
    else:
        prev_node = c_b
        new_head = headB
        c_b = c_b.next

    while c_a and c_b:
        if c_a.data <= c_b.data:
            prev_node.next = c_a
            prev_node = c_a
            c_a = c_a.next
        else:
            prev_node.next = c_b
            prev_node = c_b
            c_b = c_b.next

    if c_a:
        prev_node.next = c_a
    elif c_b:
        prev_node.next = c_b

    return new_head

def get_node(head, position):
    length = 0
    l = -position
    if head is None or l > 0:
        return None

    c = head
    n = None

    while c:
        c = c.next
        if l == 0:
            n = head
        if l > 0:
            n = n.next
        length += 1
        l += 1

    if n:
        return n.data
    else:
        return None

def Delete(head, position):
    if head:
        c = head
        i = 0
        prev_c = None
        while i < position:
            prev_c = c
            c = c.next
            i += 1
        if c.next is not None and prev_c:
            prev_c.next = c.next
            return head
        elif prev_c is None:
            return c.next
        elif c.next is None:
            prev_c.next = None
            return head
    else:
        return head

def remove_duplicates(head):
    if not head:
        return head
    c = head
    prev_node = None
    i = 0
    while c:
        if prev_node and prev_node.data == c.data:
            c = prev_node
            head = Delete(head, i)
            i -= 1
        prev_node = c
        c = c.next
        i += 1
    return head

def FindMergeNode(headA, headB):
    visited = []
    if not headA or not headB:
        return None
    curr = headA
    while curr:
        visited.append(curr)
        curr = curr.next
    curr = headB
    while curr:
        if curr in visited:
            return curr.data
        curr = curr.next

def SortedInsert(head, data):
    if not head:
        return Node(data)
    curr = head
    prev = None
    while curr.data < data:
        prev = curr
        curr = curr.next
        if curr is None:
            n = Node(data, None, prev)
            prev.next = n
            return head
    n = Node(data, curr, prev)
    curr.prev = n
    if prev:
        prev.next = n
        return head
    else:
        return n

def Reverse(head):
    if not head:
        return None
    curr = head
    prev = None
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        prev = curr
        curr = curr.prev
    return prev

def print_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


a = Node(1, None, None)
b = Node(2, None, a)
c = Node(3, None, b)
d = Node(3, None, c)
e = Node(4, None, d)
f = Node(6, None, e)
g = Node(7, None, f)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

#merged = merge(a, e)
#print(get_node(merged, -1))
#remove_duplicates(merged)
#print_list(a)
#SortedInsert(None, 0)
print_list(Reverse(a))