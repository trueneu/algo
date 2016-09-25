import sys
from collections import Counter
from itertools import takewhile


class TempTracker:
    def __init__(self):
        self._temperatures_counter = Counter()
        self._temperatures_min = sys.maxsize
        self._temperatures_max = -sys.maxsize
        self._temperatures_sum = 0
        self._temperatures_count = 0
        self._temperatures_mode = []

    def insert(self, temperature):
        try:
            self._temperatures_counter[temperature] += 1
        except KeyError:
            self._temperatures_counter[temperature] = 1

        self._temperatures_max = max(temperature, self._temperatures_max)
        self._temperatures_min = min(temperature, self._temperatures_min)

        self._temperatures_sum += temperature
        self._temperatures_count += 1

        self._temperatures_mode = [x[0] for x in takewhile(
            lambda x: x[1] == self._temperatures_counter.most_common(1)[0][1],
            self._temperatures_counter.most_common())]

    @property
    def mode(self):
        return self._temperatures_mode

    @property
    def min(self):
        return self._temperatures_min

    @property
    def max(self):
        return self._temperatures_max

    @property
    def mean(self):
        return self._temperatures_sum / self._temperatures_count


if __name__ == '__main__':
    t = TempTracker()
    t.insert(1)
    t.insert(2)
    t.insert(-1)
    print(t.mean)
    print(t.mode)
    print(t.min)
    print(t.max)
