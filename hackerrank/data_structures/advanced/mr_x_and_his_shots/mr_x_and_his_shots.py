READ_FROM_FILE = True
DEBUG = True

if READ_FROM_FILE:
    f = open('input.txt')
    inp = f.readline
else:
    inp = input

n, m = [int(x) for x in inp().strip().split()]

""" BRUTE FORCE
shots = [[int(x), int(y)] for x, y in [inp().strip().split() for _ in range(n)]]
players = [[int(x), int(y)] for x, y in [inp().strip().split() for _ in range(m)]]

if DEBUG:
    print(shots)
    print(players)


c = 0
for player in players:
    p1, p2 = player
    for shot in shots:
        s1, s2 = shot
        if (s1 <= p1 <= s2 or s1 <= p2 <= s2) or (p1 < s1 and p2 > s2):
            c += 1
print(c)
"""

class ptype:
    shot_begin = 0
    shot_end = 1
    player_begin = 2
    player_end = 3

shots_begins = []
shots_ends = []
for _ in range(n):
    x, y = map(int, inp().strip().split())
    shots_begins.append((x, ptype.shot_begin))
    shots_ends.append((y, ptype.shot_end))

players_begins = []
players_ends = []
for _ in range(m):
    x, y = map(int, inp().strip().split())
    players_begins.append((x, ptype.player_begin))
    players_ends.append((y, ptype.player_end))

all_points = []
all_points.extend(players_begins)
all_points.extend(shots_begins)
all_points.extend(players_ends)
all_points.extend(shots_ends)

all_points = sorted(all_points, key=lambda x: x[0])
if DEBUG:
    print(all_points)

shots = players = c = 0
for point in all_points:
    if point[1] == ptype.shot_begin:
        shots += 1
        c += players
    elif point[1] == ptype.shot_end:
        shots -= 1
    elif point[1] == ptype.player_begin:
        players += 1
        c += shots
    elif point[1] == ptype.player_end:
        players -= 1

print(c)

