from typing import List, Optional
import random

l = sorted([random.randint(0, 30) for _ in range(10)])


def bin_check(l: List[int], x: int) -> Optional[int]:
    left = 0
    right = len(l)
    while right - left > 1:
        middle = (left + right) // 2
        if l[middle] > x:
            right = middle
        elif l[middle] < x:
            left = middle
        else:
            return middle
    return left if l[left] == x else None

print(l)
print(bin_check(l, 10))
