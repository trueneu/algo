import sys


f = open('teams.txt')
n = int(f.readline().strip())
#n = int(input().strip())
#n = 1
if n == 0:
    print("0")
    sys.exit(0)

for student_group in range(0, n):
#    line = [int(x) for x in input().strip().split(' ')]
    line = [int(x) for x in f.readline().strip().split(' ')]
#    line = [int(x) for x in "10 4048 4048 4050 4046 4047 4049 4048 4049 4047 4047".split()]
    m = line[0]
    s = line[1:]
    ss = sorted(set(s))
    d0 = {x: s.count(x) for x in ss}
#    s = line[1:]
#    ss = list()
#    d0 = dict()
#    for skill in s:
#        try:
#            d0[skill] += 1
#        except KeyError:
#            d0[skill] = 1
#            ss.append(skill)
#    ss = sorted(ss)
    sys.exit(0)
    groups = list()
    prev_skill = None
    l = 0
    i = 0
    while len(ss):

        if i >= len(ss):
            groups.append(l)
            if l == 1:
                break
            i = 0
            l = 0
            prev_skill = None

        if i > 0:
            if prev_skill and ss[i] != prev_skill + 1:
                groups.append(l)
                if l == 1:
                    break
                i = 0
                l = 0
                prev_skill = None

            elif d0[ss[i]] > d0[ss[i - 1]]:
                l += 1
                prev_skill = ss[i]
                d0[ss[i]] -= 1
                if d0[ss[i]] == 0:
                    ss.pop(i)
                else:
                    i += 1

            else:
                groups.append(l)
                if l == 1:
                    break
                i = 0
                l = 0
                prev_skill = None

        elif i == 0:
            if prev_skill and ss[i] != prev_skill + 1:
                groups.append(l)
                if l == 1:
                    break
                i = 0
                l = 0

            l += 1
            prev_skill = ss[i]
            d0[ss[i]] -= 1

            if d0[ss[i]] == 0:
                ss.pop(i)
            else:
                i += 1

    groups.append(l)
    print(min(groups))
