enqueue_stack = []
dequeue_stack = []


def enqueue(v):
    global enqueue_stack, dequeue_stack
    enqueue_stack.append(v)


def dequeue():
    global enqueue_stack, dequeue_stack
    if not dequeue_stack:
        while enqueue_stack:
            dequeue_stack.append(enqueue_stack.pop())
    return dequeue_stack.pop()


enqueue(0)
enqueue(1)
print(dequeue())
enqueue(2)
print(dequeue())
enqueue(3)
print(dequeue())
print(dequeue())
