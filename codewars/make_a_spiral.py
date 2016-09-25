class Direction:
    right = 0
    down = 1
    left = 2
    up = 3


def visualize(spiral):
    for row in spiral:
        for number in row:
            print('.' if number == 0 else '@', end='')
        print()


def spiralize(size):
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    x, y = 0, 0
    spiral[y][x] = 1
    direction = Direction.right
    loops_without_move = 0
    while loops_without_move < 2:
        next_x, next_y = x, y
        next_next_x, next_next_y = x, y
        if direction == Direction.right:
            next_x += 1
            next_next_x += 2
        elif direction == Direction.left:
            next_x -= 1
            next_next_x -= 2
        elif direction == Direction.up:
            next_y -= 1
            next_next_y -= 2
        elif direction == Direction.down:
            next_y += 1
            next_next_y += 2
        if direction == Direction.left or direction == Direction.right:
            neighbour_y1 = y - 1
            neighbour_y2 = y + 1
            neighbour_x1 = neighbour_x2 = next_x
        else:
            neighbour_x1 = x - 1
            neighbour_x2 = x + 1
            neighbour_y1 = neighbour_y2 = next_y
        if neighbour_x1 < 0 or neighbour_x1 >= size: neighbour_x1 = next_x
        if neighbour_x2 < 0 or neighbour_x2 >= size: neighbour_x2 = next_x
        if neighbour_y1 < 0 or neighbour_y1 >= size: neighbour_y1 = next_y
        if neighbour_y2 < 0 or neighbour_y2 >= size: neighbour_y2 = next_y

        if next_next_x < 0: next_next_x = size
        if next_next_y < 0: next_next_y = size
        try:
            cond = (spiral[next_next_y][next_next_x] == 1)
        except IndexError:
            cond = False

        try:
            cond2 = (spiral[neighbour_y1][neighbour_x1] == 1)
        except IndexError:
            cond2 = False

        try:
            cond3 = (spiral[neighbour_y2][neighbour_x2] == 1)
        except IndexError:
            cond3 = False

        if (next_x < 0 or next_x >= size or next_y < 0 or next_y >= size or
                cond or cond2 or cond3):
            direction = (direction + 1) % 4
            loops_without_move += 1
        else:
            x, y = next_x, next_y
            spiral[y][x] = 1
            loops_without_move = 0
    return spiral

visualize(spiralize(3))