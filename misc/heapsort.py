heap = ['x', 2, 3, 1, 10, 6, 2, 7, 8, 22, 7, 4, 5, 10, 7, 2, 4, 9, 7, 4]


def heap_left(index):
    return 2*index


def heap_right(index):
    return 2*index + 1


def heap_parent(index):
    return int(index / 2)


def max_heapify(array, index, heapsize):
    new_index = -1
    if heap_left(index) > heapsize:
        return
    if array[index] < array[heap_left(index)]:
        if heap_right(index) > heapsize:
            new_index = heap_left(index)
        elif array[index] < array[heap_right(index)]:
            if array[heap_left(index)] < array[heap_right(index)]:
                new_index = heap_right(index)
            else:
                new_index = heap_left(index)
        else:
            new_index = heap_left(index)
    elif heap_right(index) <= heapsize and array[index] < array[heap_right(index)]:
        new_index = heap_right(index)

    if not new_index == -1:
        array[index], array[new_index] = array[new_index], array[index]
        max_heapify(array, new_index, heapsize)


def build_max_heap(array):
    i = int((len(array) - 1) / 2)
    while i >= 1:
        max_heapify(array, i, len(array) - 1)
        i -= 1

def heap_sort(max_heap):
    i = len(max_heap) - 1
    heapsize = i
    while heapsize >= 2:
        max_heap[1], max_heap[i] = max_heap[i], max_heap[1]
        heapsize -= 1
        max_heapify(max_heap, 1, heapsize)
        i -= 1

build_max_heap(heap)
print(heap)
heap_sort(heap)
print(heap)