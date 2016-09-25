import sys

class NotEvenAQueue:
    def __init__(self, size):
        self.data = [-sys.maxsize for _ in range(size)]
        self.size = size
        self.maximum = -sys.maxsize

    def put(self, d, i):
        if self.data[i % self.size] == self.maximum:
            self.data[i % self.size] = -sys.maxsize
            self.maximum = max(self.data)

        self.data[i % self.size] = d
        if d > self.maximum:
            self.maximum = d

    def get_maximum(self):
        return self.maximum

# class Queue:
#     def __init__(self):
#         self.data = list()
#         self.bottom = 0
#         self.maximum = -sys.maxsize
#
#     def push(self, d):
#         self.data.append(d)
#         if d > self.maximum:
#             self.maximum = d
#
#     def pop(self):
#         self.bottom += 1
#         if not self.is_empty():
#             if self.data[self.bottom - 1] == self.maximum:
#                 self.maximum = max(self.data[self.bottom:])
#         else:
#             self.maximum = -sys.maxsize
#         return self.data[self.bottom - 1]
#
#     def is_empty(self):
#         return self.bottom == len(self.data)
#
#     def get_maximum(self):
#         return self.maximum




f = open('queries_with_fixed_length_input.txt')

#n, q = map(int, input().strip().split())
n, q = map(int, f.readline().strip().split())

#a = list(map(int, input().strip().split()))
a = list(map(int, f.readline().strip().split()))

#d = [int(x) for x in [input().strip() for _ in range(q)]]
d = [int(x) for x in [f.readline().strip() for _ in range(q)]]

for offset in d:
    q = NotEvenAQueue(offset)
    m = list()
    for i in range(offset):
        q.put(a[i], i)
    min_m = q.get_maximum()

    for i in range(offset, n):
        q.put(a[i], i)
        if q.get_maximum() < min_m:
            min_m = q.get_maximum()

    print(min_m)
