nq = "2 5"

#nq = input().strip()
parts = nq.split(' ')
n = int(parts[0])
q = int(parts[1])

instructions = ['1 0 5',
'1 1 7',
'1 0 3',
'2 1 0',
'2 1 1'
]
#instructions = [x for x in input().strip()]

last_ans = 0
seq_list = list()
for i in range(0, n):
    seq_list.append(list())

for instruction in instructions:
    parts = instruction.split(' ')
    inst_type = int(parts[0])
    op1 = int(parts[1])
    op2 = int(parts[2])

    index = (op1 ^ last_ans) % n

    if inst_type == 1:
        seq_list[index].append(op2)

    elif inst_type == 2:
        last_ans = seq_list[index][op2 % len(seq_list[index])]
        print(last_ans)

