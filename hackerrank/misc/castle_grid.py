import sys

def grid_out():
    global grid
    for row in grid:
        print(row)

class Queue:
    def __init__(self):
        self.data = list()
        self.bottom = 0
    def push(self, d):
        self.data.append(d)
    def pop(self):
        self.bottom += 1
        return self.data[self.bottom - 1]
    def is_empty(self):
        return self.bottom == len(self.data)


def flood(grid, x1, y1, x2, y2):
    q = Queue()
    q.push((x1, y1))
    x = y = -1
    while x != x2 or y != y2:
        x, y = q.pop()
        cell_curr = grid[y][x]
        for dx in [-1, 1]:
            if not 0 <= x + dx < len(grid[y]):
                continue
            cell = grid[y][x + dx]
            if cell == 0:
                grid[y][x + dx] = cell_curr + 1
                q.push((x + dx, y))

        for dy in [-1, 1]:
            if not 0 <= y + dy < len(grid):
                continue
            cell = grid[y + dy][x]
            if cell == 0:
                grid[y + dy][x] = cell_curr + 1
                q.push((x, y + dy))
        # print(q.data, q.bottom)
        # grid_out()
        # print("")

def flood2(grid, x1, y1, x2, y2):
    q = Queue()
    q.push((x1, y1))
    x = y = -1
    while x != x2 or y != y2:
        x, y = q.pop()
        cell_curr = grid[y][x]
        for new_x in range(x, -1, -1):
            cell = grid[y][new_x]
            if cell == -1:
                break  # NO WAY
            if cell == 0:
                grid[y][new_x] = cell_curr + 1
                q.push((new_x, y))

        for new_x in range(x, len(grid[y])):
            cell = grid[y][new_x]
            if cell == -1:
                break  # NO WAY
            if cell == 0:
                grid[y][new_x] = cell_curr + 1
                q.push((new_x, y))

        for new_y in range(y, -1, -1):
            cell = grid[new_y][x]
            if cell == -1:
                break  # NO WAY
            if cell == 0:
                grid[new_y][x] = cell_curr + 1
                q.push((x, new_y))

        for new_y in range(y, len(grid)):
            cell = grid[new_y][x]
            if cell == -1:
                break  # NO WAY
            if cell == 0:
                grid[new_y][x] = cell_curr + 1
                q.push((x, new_y))
        # print(q.data, q.bottom)
        # grid_out()
        # print("")
    return grid[y][x] - 1

def shortest_square_path(grid, x1, y1, x2, y2):
    # path = list()
    x, y = x2, y2
    # path.append((x, y))
    first_move = True
    prev_hor = False
    prev_vert = False

    angles = 0

    while x != x1 or y != y1:
        changed_x_y = False
        cell_curr = grid[y][x]
        for dx in [-1, 1]:
            if not 0 <= x + dx < len(grid[y]):
                continue
            cell = grid[y][x + dx]
            if cell == cell_curr - 1 and (prev_hor or first_move):
                prev_hor = True
                prev_vert = False
                changed_x_y = True
                x += dx

        for dy in [-1, 1]:
            if not 0 <= y + dy < len(grid):
                continue
            cell = grid[y + dy][x]
            if cell == cell_curr - 1 and (prev_vert or first_move):
                prev_hor = False
                prev_vert = True
                changed_x_y = True
                y += dy

        if not changed_x_y:
            if prev_hor:
                for dy in [-1, 1]:
                    if not 0 <= y + dy < len(grid):
                        continue
                    cell = grid[y + dy][x]
                    if cell == cell_curr - 1:
                        prev_hor = False
                        prev_vert = True
                        changed_x_y = True
                        y += dy
            elif prev_vert:
                for dx in [-1, 1]:
                    if not 0 <= x + dx < len(grid[y]):
                        continue
                    cell = grid[y][x + dx]
                    if cell == cell_curr - 1:
                        prev_hor = True
                        prev_vert = False
                        changed_x_y = True
                        x += dx
            angles += 1
        # path.append((x, y))
        first_move = False
        # print(path)
    return angles

f = open('castle_grid.txt')

#n = int(input().strip())
n = int(f.readline().strip())

grid = list()
for i in range(0, n):
    #grid_row_raw = input().strip()
    grid_row_raw = f.readline().strip()
    grid_row = [0 if c == '.' else -1 for c in grid_row_raw]
    grid.append(grid_row)

y1, x1, y2, x2 = [int(x) for x in f.readline().strip().split()]

grid[y1][x1] = 1  # starting point

# flood(grid, x1, y1, x2, y2)
# grid_out()
# print(shortest_square_path(grid, x1, y1, x2, y2) + 1)
print(flood2(grid, x1, y1, x2, y2))


