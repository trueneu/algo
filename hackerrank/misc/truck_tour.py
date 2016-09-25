f = open('truck_tour.txt')
#n = int(input().strip())
n = int(f.readline().strip())

stations = [[int(s) for s in f.readline().strip().split()] for i in range(n)]
#stations = [[int(s) for s in input().strip().split()] for i in range(n)]

start = g_delta = l_delta = 0
for i in range(n):
    l_delta = stations[i][0] - stations[i][1]
    if g_delta + l_delta < 0:
        if l_delta >= 0:
            start = i
            g_delta = l_delta
        else:
            start = i + 1
            g_delta = 0
    else:
        g_delta += l_delta

print(start)
