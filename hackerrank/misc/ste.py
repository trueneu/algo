f = open('ste_input.txt')
#n = int(input().strip())
n = int(f.readline().strip())

undo_list = list()
s = ""
i = 0

while i < n:
    op_list = f.readline().strip().split()
    op = int(op_list[0])
    if op == 1:
        undo_list.append((1, len(op_list[1])))
        s = "".join([s, op_list[1]])
    elif op == 2:
        undo_list.append((2, s[len(s) - int(op_list[1]):]))
        s = s[:-int(op_list[1])]

    elif op == 3:
        print(s[int(op_list[1]) - 1])
    elif op == 4:
        undo_op, data = undo_list.pop()
        if undo_op == 1:
            s = s[:-data]
        elif undo_op == 2:
            s = "".join([s, data])
    i += 1