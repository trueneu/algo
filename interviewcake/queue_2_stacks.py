class Stack(object):
    def __init__(self):
        self._data = list()

    def push(self, data):
        self._data.append(data)

    def pop(self):
        try:
            x = self._data.pop()
        except IndexError:
            x = None
        return x

    def size(self):
        return len(self._data)

class QueueUsing2Stacks(object):
    def __init__(self):
        self._data = Stack()
        self._temp = Stack()

    def enqueue(self, data):
        self._data.push(data)

    def dequeue(self):
        i = 0
        if self._data.size() < 1:
            return None
        sz = self._data.size()
        while i < sz - 1:
            self._temp.push(self._data.pop())
            i += 1
        x = self._data.pop()
        i = 0
        sz = self._temp.size()
        while i < sz:
            self._data.push(self._temp.pop())
            i += 1
        return x

q = QueueUsing2Stacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

