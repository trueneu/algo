import sys

f = open('no_prefix_set.txt')

#n = int(input().strip())
n = int(f.readline().strip())

db = dict()
s = [f.readline().strip() for _ in range(n)]

for st in s:
    if st in db.keys():
        print("BAD SET")
        print(st)
        sys.exit(0)
    db[st] = 1


for st in s:
    i = 0
    while i < len(st):
        if st[:i] in db.keys():
            print("BAD SET")
            print(st)
            sys.exit(0)
        i += 1

print("GOOD SET")


