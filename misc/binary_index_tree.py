class BinaryIndexTree:
    def __init__(self, data):
        self.tree = self.bit_create_empty_tree(len(data) + 1)
        for i, d in enumerate(data):
            self.bit_update(i + 1, d)

    @staticmethod
    def bit_get_parent(index):
        return index - (index & (-index))

    @staticmethod
    def bit_get_next(index):
        return index + (index & (-index))

    @staticmethod
    def bit_create_empty_tree(length):
        return [0] * length

    def bit_update(self, index, difference):
        curr_index = index
        while curr_index < len(self.tree):
            self.tree[curr_index] += difference
            curr_index = self.bit_get_next(curr_index)

    def bit_sum_until_index(self, index):
        curr_index = index
        s = 0
        while curr_index > 0:
            s += self.tree[curr_index]
            curr_index = self.bit_get_parent(curr_index)
        return s


data = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
bit = BinaryIndexTree(data)
print(bit.bit_sum_until_index(4))