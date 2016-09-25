import sys

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

    def bit_sum_from_a_to_b(self, a, b):
        if a > b:
            return 0
        return self.bit_sum_until_index(b) - self.bit_sum_until_index(a)

READ_FROM_FILE = True
DEBUG = True

if READ_FROM_FILE:
    f = open('input.txt')
    inp = f.readline
else:
    inp = input

t = int(inp().strip())

for _ in range(t):
    n = int(inp().strip())
    data_by_distance = sorted(zip(map(int, inp().strip().split()), map(int, inp().strip().split())),
                  key=lambda x: x[0])  # sorted by distance from 0
    data_by_population = sorted(data_by_distance, reverse=True, key=lambda x: x[1])  # by population

    coords = [x[0] for x in data_by_distance]
    populations = [x[1] for x in data_by_population]

    bit_count = BinaryIndexTree([1] * n)  # count of cities
    bit_coords = BinaryIndexTree(coords)  # coords of cities

    population_to_index_in_coords = {}
    for i, city in enumerate(data_by_distance):
        if city[1] in population_to_index_in_coords:
            population_to_index_in_coords[city[1]].append(i)
        else:
            population_to_index_in_coords[city[1]] = [i]

    cable_length = 0
    for population in populations:
        index_in_coords = population_to_index_in_coords[population].pop()
        index_in_tree = index_in_coords + 1
        coord = coords[index_in_coords]

        count_left = bit_count.bit_sum_until_index(index_in_tree - 1)
        count_right = bit_count.bit_sum_from_a_to_b(index_in_tree, n)

        sum_of_coords_left = bit_coords.bit_sum_until_index(index_in_tree - 1)
        sum_of_coords_right = bit_coords.bit_sum_from_a_to_b(index_in_tree, n)

        cable_length += (count_left * coord - sum_of_coords_left) * population + \
                        (sum_of_coords_right - count_right * coord) * population

        bit_count.bit_update(index_in_tree, -1)
        bit_coords.bit_update(index_in_tree, -coord)
    cable_length %= 1000000007



    print(cable_length)






