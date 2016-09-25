from math import inf


class Stack:
    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_item = -inf

    def push(self, item):
        self.max_item = max(self.max_item, item)
        super().push(item)

    def pop(self):
        if len(self.items) == 1:
            self.max_item = -inf
        if self.peek() == self.max_item:
            self.max_item = max(self.items[:-1])
        return super().pop()


class MaxStack2:
    def __init__(self):
        self.stack = Stack()
        self.maxs_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if not self.maxs_stack.peek() or item >= self.maxs_stack.peek():  # this line was completely broken
            self.maxs_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.maxs_stack.peek():  # remove redundant pars
            self.maxs_stack.pop()
        return item

    def get_max(self):
        return self.maxs_stack.peek()

st = MaxStack2()
st.push(0)
st.push(4)
st.push(3)
st.push(5)

print(st.get_max())
st.pop()
print(st.get_max())
st.pop()
print(st.get_max())
st.pop()
print(st.get_max())
st.pop()
print(st.get_max())
