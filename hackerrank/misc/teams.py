import sys


f = open('teams.txt')
n = int(f.readline().strip())
#n = int(input().strip())
n = 1
if n == 0:
    print("0")
    sys.exit(0)

for student_group in range(0, n):
#    line = [int(x) for x in input().strip().split(' ')]
#    line = [int(x) for x in f.readline().strip().split(' ')]
    line = [int(x) for x in "10 4048 4048 4050 4046 4047 4049 4048 4049 4047 4047".split()]
    m = line[0]
    s = sorted(line[1:])

    groups = list()
    prev_skill = None
    l = 0
    i = 0
    prev_overlap_degree = 0
    overlap_degree = 0
    overlap = False
    while len(s):
        if prev_skill:
            if i >= len(s):
                groups.append(l)
                if l == 1:
                    break
                i = 0
                l = 0
                prev_skill = None
                overlap = False
            elif s[i] == prev_skill + 1:
                l += 1
                prev_skill += 1
                s.pop(i)
            elif s[i] == prev_skill:
                if i + 2 < len(s):
                    if s[i + 1] > s[i] and not s[i + 1] == s[i + 2]:
                        groups.append(l)
                        if l == 1:
                            break
                        i = 0
                        l = 0
                        prev_skill = None
                        continue
                elif i + 1 < len(s):
                    if s[i + 1] > s[i]:
                        groups.append(l)
                        if l == 1:
                            break
                        i = 0
                        l = 0
                        prev_skill = None
                        continue
                i += 1
            else:
                groups.append(l)
                if l == 1:
                    break
                i = 0
                l = 0
                prev_skill = None
                overlap = False
        else:
            l += 1
            prev_skill = s[i]
            s.pop(i)
    groups.append(l)
    print(min(groups))

