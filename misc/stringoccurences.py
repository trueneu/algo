n_str = "4"

n_str = input().strip()
n = int(n_str)

strs = dict()

for i in range(0, n):
    s = input().strip()
    if s in strs.keys():
        strs[s] += 1
    else:
        strs[s] = 1

q_str = input().strip()
q = int(q_str)

for i in range(0, q):
    s = input().strip()
    if s in strs.keys():
        print(strs[s])
    else:
        print(0)