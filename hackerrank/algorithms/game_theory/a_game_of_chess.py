from collections import deque


def check_winning_position_reachable(x, y, winner_map):
    dx = -2
    for dy in [-1, 1]:
        if check_boundaries(x, y, dx, dy, winner_map) and winner_map[y + dy][x + dx] == 2:
            return True

    dy = -2
    for dx in [-1, 1]:
        if check_boundaries(x, y, dx, dy, winner_map) and winner_map[y + dy][x + dx] == 2:
            return True

    return False


def check_boundaries(x, y, dx, dy, winner_map):
    return 0 <= x + dx < len(winner_map[0]) and 0 <= y + dy < len(winner_map)


def build_winner_map2(width, height):
    if width < 3 or height < 3:
        return None
    winner_map = [[0] * width for _ in range(height)]
    winner_map[0][0] = winner_map[1][0] = winner_map[0][1] = winner_map[1][1] = 2
    q = deque([(0, 0), (1, 0), (0, 1), (1, 1)])
    while q:
        x, y = q.pop()
        winner = winner_map[y][x]
        if winner == 2:
            dx = 2
            for dy in [-1, 1]:
                if check_boundaries(x, y, dx, dy, winner_map):
                    winner_map[y + dy][x + dx] = 1
                    q.appendleft((x + dx, y + dy))
            dy = 2
            for dx in [-1, 1]:
                if check_boundaries(x, y, dx, dy, winner_map):
                    winner_map[y + dy][x + dx] = 1
                    q.appendleft((x + dx, y + dy))

        elif winner == 1:
            dx = 2
            for dy in [-1, 1]:
                if (check_boundaries(x, y, dx, dy, winner_map) and
                        not check_winning_position_reachable(x + dx, y + dy, winner_map)):
                    winner_map[y + dy][x + dx] = 2
                    q.appendleft((x + dx, y + dy))
            dy = 2
            for dx in [-1, 1]:
                if (check_boundaries(x, y, dx, dy, winner_map) and
                        not check_winning_position_reachable(x + dx, y + dy, winner_map)):
                    winner_map[y + dy][x + dx] = 2
                    q.appendleft((x + dx, y + dy))

    return winner_map

winner_map = build_winner_map2(15, 15)

t = int(input())
for _ in range(t):
    x, y = map(int, input().strip().split())
    print("First" if winner_map[y - 1][x - 1] == 1 else "Second")
