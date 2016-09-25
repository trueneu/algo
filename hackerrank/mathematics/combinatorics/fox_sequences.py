READ_FROM_STDIN = False
if READ_FROM_STDIN:
    t = int(input().strip())
else:
    f = open('fox_sequences_input1.txt', 'r')
    t = int(f.readline().strip())

for _ in range(t):
    if READ_FROM_STDIN:
        n, lo, hi = map(int, input().strip().split())
    else:
        n, lo, hi = map(int, f.readline().strip().split())
    total_sequences = 0
    sequences_by_length = [0]
    for seq_length in range(1, n + 1):
        pass