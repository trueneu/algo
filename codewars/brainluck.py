import sys

mem = [0]
mem_pointer = 0
input_index = 0
prog_output = ""

def mem_inc():
    global mem, mem_pointer
    if mem_pointer < 0:
        print("mem_pointer < 0 when incrementing")
        sys.exit(2)

    mem[mem_pointer] += 1
    if mem[mem_pointer] > 255:
        mem[mem_pointer] = 0

def mem_dec():
    global mem, mem_pointer
    if mem_pointer < 0:
        print("mem_pointer < 0 when decrementing")
        sys.exit(2)

    mem[mem_pointer] -= 1
    if mem[mem_pointer] < 0:
        mem[mem_pointer] = 255

def pnt_inc():
    global mem, mem_pointer
    mem_pointer += 1
    if len(mem) == mem_pointer:
        mem.append(0)

def pnt_dec():
    global mem, mem_pointer
    mem_pointer -= 1
    if mem_pointer < 0:
        print("mem_pointer < 0 when decrementing pointer")
        sys.exit(2)

def mem_out():
    global mem, mem_pointer, prog_output
    prog_output += chr(mem[mem_pointer])

def mem_in(value):
    global mem, mem_pointer
    mem[mem_pointer] = value

def test_is_zero():
    global mem, mem_pointer
    if mem[mem_pointer] == 0:
        return True
    else:
        return False

class Stack(object):
    def __init__(self):
        self._data = list()

    def push(self, data):
        self._data.append(data)

    def pop(self):
        try:
            x = self._data.pop()
        except IndexError:
            x = None
        return x

    def size(self):
        return len(self._data)

def find_corresponding_brackets(code):
    bracket_positions = list()
    s = Stack()
    for i, c in enumerate(code):
        bracket_positions.append(-1)
        if c == '[':
            s.push(i)
        elif c == ']':
            p = s.pop()
            bracket_positions[i] = p
            bracket_positions[p] = i
    return bracket_positions

def read_next_char_input(input):
    global input_index
    res = ord(input[input_index])
    input_index += 1
    return res

def brain_luck(code, input):
    bracket_positions = find_corresponding_brackets(code)
    global mem, mem_pointer, prog_output, input_index
    mem = [0]
    mem_pointer = 0
    input_index = 0
    prog_output = ""
    i = 0
    while i >= 0 and i < len(code):
        c = code[i]
        if c == '>':
            pnt_inc()
            i += 1
        elif c == '<':
            pnt_dec()
            i += 1
        elif c == '+':
            mem_inc()
            i += 1
        elif c == '-':
            mem_dec()
            i += 1
        elif c == '.':
            mem_out()
            i += 1
        elif c == ',':
            mem_in(read_next_char_input(input))
            i += 1
        elif c == '[':
            if test_is_zero():
                i = bracket_positions[i]
            else:
                i += 1
        elif c == ']':
            if not test_is_zero():
                i = bracket_positions[i]
            else:
                i += 1
    return prog_output


print(brain_luck('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.', 'Codewars' + chr(0)))