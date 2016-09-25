# to help with debugging
def unbleach(n):
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

def bleach(n):
    return n.replace('s', ' ').replace('t', '\t').replace('n', '\n')

class imps:
    stack = 0
    arithm = 1
    heap = 2
    io = 3
    flow = 4

class chars:
    space = ' '
    tab = '\t'
    linefeed = '\n'

class stack_ops:
    push = 0
    dup = 1
    discard_below = 2
    dup_top = 3
    swap_top = 4
    discard_top = 5

class arithm_ops:
    plus = 0
    minus = 1
    mult = 2
    div = 3
    mod = 4

class heap_ops:
    store = 0
    peek = 1

class io_ops:
    output_char = 0
    output_num = 1
    read_char = 2
    read_num = 3

class flow_ops:
    mark = 0
    call = 1
    jump = 2
    jz = 3
    jlz = 4
    ret = 5
    ext = 6

class WhitespaceInterpretationError(Exception):
    def __init__(self):
        super(WhitespaceInterpretationError, self)

class Stack(object):
    def __init__(self):
        self._data = list()

    def push(self, data):
        self._data.append(data)

    def pop(self):
        try:
            x = self._data.pop()
        except IndexError:
            raise WhitespaceInterpretationError
        return x

    def size(self):
        return len(self._data)

    def get_nth_from_top(self, n):
        if n > self.size() - 1:
            raise WhitespaceInterpretationError
        return self._data[self.size() - 1 - n]

    def discard_below_top(self, n):
        i = 0
        while i < n:
            self._data.pop(self.size() - 1 - 1)
            i += 1

    def clear(self):
        self._data.clear()






heap = dict()
stack = Stack()
ret_ptrs = Stack()
labels = dict()
inp_ptr = 0
inp_g = ""
out = ""
exc_ptr = 0
# solution

def parse_imp(line):
    if len(line) == 0:
        raise WhitespaceInterpretationError

    if line[0] == chars.space:
        return imps.stack, 1
    elif line[0] == chars.linefeed:
        return imps.flow, 1
    elif line[0] == chars.tab:
        if len(line) < 1:
            raise WhitespaceInterpretationError

        if line[1] == chars.space:
            return imps.arithm, 2
        elif line[1] == chars.tab:
            return imps.heap, 2
        elif line[1] == chars.linefeed:
            return imps.io, 2

    else:
        raise WhitespaceInterpretationError

def parse_num(line):
    if len(line) < 1:
        raise WhitespaceInterpretationError
    if line[0] == chars.tab:
        sign = -1
    elif line[0] == chars.space:
        sign = 1
    else:
        raise WhitespaceInterpretationError
    num = 0
    i = 1
    while line[i] != chars.linefeed:
        num <<= 1
        if line[i] == chars.tab:
            num += 1
        i += 1
    num *= sign
    return num, i + 1

def parse_label(line):
    if len(line) < 1:
        raise WhitespaceInterpretationError

    i = 0
    label = ''
    while line[i] != chars.linefeed:
        label += line[i]
        i += 1

    return label, i + 1

def add_label(label, ptr):
    global labels
    if label in labels.keys():
        raise WhitespaceInterpretationError
    labels[label] = ptr

def get_label_ptr(label):
    #print("Looking for label '" + unbleach(label) + "'")
    if label not in labels.keys():
        raise WhitespaceInterpretationError
    return labels[label]

def parse_stack_op(line):
    if len(line) < 1:
        raise WhitespaceInterpretationError
    if line[0] == chars.space:
        return stack_ops.push, 1
    else:
        if len(line) < 2:
            raise WhitespaceInterpretationError

    if line[0] == chars.tab:
        if line[1] == chars.space:
            return stack_ops.dup, 2
        elif line[1] == chars.linefeed:
            return stack_ops.discard_below, 2
        else:
            raise WhitespaceInterpretationError

    elif line[0] == chars.linefeed:
        if line[1] == chars.space:
            return stack_ops.dup_top, 2
        elif line[1] == chars.linefeed:
            return stack_ops.discard_top, 2
        elif line[1] == chars.tab:
            return stack_ops.swap_top, 2
        else:
            raise WhitespaceInterpretationError

def parse_arithm_op(line):
    if len(line) < 2:
        raise WhitespaceInterpretationError

    if line[0] == chars.tab:
        if line[1] == chars.space:
            return arithm_ops.div, 2
        elif line[1] == chars.tab:
            return arithm_ops.mod, 2
        else:
            raise WhitespaceInterpretationError

    elif line[0] == chars.space:
        if line[1] == chars.space:
            return arithm_ops.plus, 2
        elif line[1] == chars.linefeed:
            return arithm_ops.mult, 2
        elif line[1] == chars.tab:
            return arithm_ops.minus, 2
        else:
            raise WhitespaceInterpretationError

def parse_heap_op(line):
    if len(line) < 1:
        raise WhitespaceInterpretationError

    if line[0] == chars.tab:
        return heap_ops.peek, 1
    elif line[0] == chars.space:
        return heap_ops.store, 1
    else:
        raise WhitespaceInterpretationError

def parse_io_op(line):
    if len(line) < 2:
        raise WhitespaceInterpretationError

    if line[0] == chars.tab:
        if line[1] == chars.tab:
            return io_ops.read_num, 2
        elif line[1] == chars.space:
            return io_ops.read_char, 2
        else:
            raise WhitespaceInterpretationError
    elif line[0] == chars.space:
        if line[1] == chars.tab:
            return io_ops.output_num, 2
        elif line[1] == chars.space:
            return io_ops.output_char, 2
        else:
            raise WhitespaceInterpretationError
    else:
        raise WhitespaceInterpretationError

def parse_flow_op(line):
    if len(line) < 2:
        raise WhitespaceInterpretationError

    if line[0] == chars.tab:
        if line[1] == chars.tab:
            return flow_ops.jlz, 2
        elif line[1] == chars.space:
            return flow_ops.jz, 2
        elif line[1] == chars.linefeed:
            return flow_ops.ret, 2
        else:
            raise WhitespaceInterpretationError

    elif line[0] == chars.space:
        if line[1] == chars.tab:
            return flow_ops.call, 2
        elif line[1] == chars.space:
            return flow_ops.mark, 2
        elif line[1] == chars.linefeed:
            return flow_ops.jump, 2
        else:
            raise WhitespaceInterpretationError
    elif line[0] == chars.linefeed:
        if line[1] == chars.linefeed:
            return flow_ops.ext, 2
        else:
            raise WhitespaceInterpretationError


def process_stack(line):
    op, l = parse_stack_op(line)
    if op == stack_ops.push:
        n, l2 = parse_num(line[l:])
        stack.push(n)
        #print("Pushed to stack: " + str(n))
        return l + l2
    elif op == stack_ops.dup:
        n, l2 = parse_num(line[l:])
        m = stack.get_nth_from_top(n)
        #print("Got nth (" + str(n) + ") from to of the stack and pushed it: " + str(m))
        stack.push(m)
        return l + l2
    elif op == stack_ops.discard_below:
        n, l2 = parse_num(line[l:])
        if n < 0 or n > stack.size() - 1:
            n = stack.size() - 1
        stack.discard_below_top(n)
        #print("Discarded below stack top, elements qty: " + str(n))
        return l + l2
    elif op == stack_ops.dup_top:
        n = stack.pop()
        stack.push(n)
        stack.push(n)
        #print("Duplicated stack top")
        return l
    elif op == stack_ops.swap_top:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.push(n1)
        stack.push(n2)
        #print("Swapped top 2 stack elements")
        return l
    elif op == stack_ops.discard_top:
        n = stack.pop()
        #print("Discarded stack top")
        return l

def heap_read(addr):
    return heap[addr]

def heap_write(addr, n):
    heap[addr] = n

def read_chr():
    global inp_g, inp_ptr
    inp_ptr += 1
    return inp_g[inp_ptr - 1]

def read_num():
    global inp_g, inp_ptr
    num_str = ""
    while inp_ptr < len(inp_g) and inp_g[inp_ptr] != '\n':
        num_str += inp_g[inp_ptr]
        inp_ptr += 1
    inp_ptr += 1
    num = int(num_str)
    return num


def process_io(line):
    global out
    op, l = parse_io_op(line)
    if op == io_ops.read_char:
        c = read_chr()
        cn = ord(c)
        addr = stack.pop()
        heap_write(addr, cn)
        #print("Wrote to heap at addr " + str(addr) + " value of " + str(cn) + " (it was a char: " + c + ")")
        return l
    elif op == io_ops.read_num:
        n = read_num()
        addr = stack.pop()
        heap_write(addr, n)
        #print("Wrote to heap at addr " + str(addr) + " value of " + str(n))
        return l
    elif op == io_ops.output_char:
        c = stack.pop()
        out += chr(c)
        #print("Added to output: " + chr(c))
        return l
    elif op == io_ops.output_num:
        n = stack.pop()
        out += str(n)
        #print("Added to output: " + str(n))
        return l

def process_arithm(line):
    op, l = parse_arithm_op(line)
    a = stack.pop()
    b = stack.pop()
    r = None
    if op == arithm_ops.plus:
        r = a + b
        #print("Popped 2 values from stack, did math, " + str(a) + " + " + str(b) + " = " + str(r))
    elif op == arithm_ops.minus:
        r = b - a
        #print("Popped 2 values from stack, did math, " + str(b) + " - " + str(a) + " = " + str(r))
    elif op == arithm_ops.mult:
        r = b * a
        #print("Popped 2 values from stack, did math, " + str(a) + " * " + str(b) + " = " + str(r))
    elif op == arithm_ops.div:
        if a == 0:
            raise WhitespaceInterpretationError
        r = int(b // a)
        #print("Popped 2 values from stack, did math, " + str(b) + " / " + str(a) + " = " + str(r))
    elif op == arithm_ops.mod:
        r = b % a
        #print("Popped 2 values from stack, did math, " + str(b) + " % " + str(a) + " = " + str(r))

    stack.push(r)
    return l

def process_heap(line):
    op, l = parse_heap_op(line)
    if op == heap_ops.peek:
        a = stack.pop()
        n = heap_read(a)
        stack.push(n)
        #print("Popped heap addr " + str(a) + ", read from heap " + str(n) + ", pushed it to stack")
    elif op == heap_ops.store:
        a = stack.pop()
        b = stack.pop()
        heap_write(b, a)
        #print("Popped heap addr " + str(b) + ", popped data " + str(a) + ", wrote it to heap")
    return l

def process_flow(line, do_jumps=True):
    global exc_ptr
    op, l = parse_flow_op(line)
    if op == flow_ops.mark:
        lbl, l2 = parse_label(line[l:])
        # add_label(lbl, exc_ptr + l + l2)
        #print("Looking again at label @" + str(exc_ptr + l + l2))
        return l + l2

    elif op == flow_ops.call:
        lbl, l2 = parse_label(line[l:])
        ret_ptrs.push(exc_ptr + l + l2)

        exc_ptr = get_label_ptr(lbl)
        #print("Calling procedure @" + str(exc_ptr))
        return 0
    elif op == flow_ops.jump:
        lbl, l2 = parse_label(line[l:])

        exc_ptr = get_label_ptr(lbl)
        #print("Jumping @" + str(exc_ptr))

        return 0
    elif op == flow_ops.jz:
        lbl, l2 = parse_label(line[l:])
        n = stack.pop()
        #print("Executing jz:")
        if n == 0:
            exc_ptr = get_label_ptr(lbl)
            #print("Jumping @" + str(exc_ptr))
            return 0
        return l + l2

    elif op == flow_ops.jlz:
        lbl, l2 = parse_label(line[l:])
        n = stack.pop()
        #print("Executing jlz:")
        if n < 0:
            exc_ptr = get_label_ptr(lbl)
            #print("Jumping @" + str(exc_ptr))
            return 0
        return l + l2
    elif op == flow_ops.ret:
        exc_ptr = ret_ptrs.pop()
        #print("Returning from a procedure to @" + str(exc_ptr))
        return 0

    elif op == flow_ops.ext:
        #print("Terminating")
        return None

def code_sanitize(code):
    res = ""
    for c in code:
        if c == chars.linefeed or c == chars.space or c == chars.tab:
            res += c
    return res


def labels_search(code):
    #print("Searching for labels...")
    exc_ptr = 0

    while exc_ptr < len(code):
        #print("Execution ptr:" + str(exc_ptr))
        #print("Code remaining:" + unbleach(code[exc_ptr:]))

        imp, l = parse_imp(code[exc_ptr:])
        exc_ptr += l
        if imp == imps.io:
            _, l2 = parse_io_op(code[exc_ptr:])
            exc_ptr += l2
        elif imp == imps.stack:
            op, l2 = parse_stack_op(code[exc_ptr:])
            exc_ptr += l2
            if op == stack_ops.push or op == stack_ops.dup or op == stack_ops.discard_below:
                _, l3 = parse_num(code[exc_ptr:])
                exc_ptr += l3

        elif imp == imps.arithm:
            op, l2 = parse_arithm_op(code[exc_ptr:])
            exc_ptr += l2
        elif imp == imps.heap:
            op, l2 = parse_heap_op(code[exc_ptr:])
            exc_ptr += l2

        elif imp == imps.flow:
            op, l2 = parse_flow_op(code[exc_ptr:])
            exc_ptr += l2
            if op == flow_ops.call or op == flow_ops.jump or op == flow_ops.jz or op == flow_ops.jlz:
                lbl, l3 = parse_label(code[exc_ptr:])
                exc_ptr += l3
            elif op == flow_ops.mark:
                lbl, l3 = parse_label(code[exc_ptr:])
                exc_ptr += l3
                add_label(lbl, exc_ptr)
                #print("Added label '" + unbleach(lbl) + "' during initial label search @" + str(exc_ptr))

def whitespace(code, inp=''):
    global out, exc_ptr, heap, stack, ret_ptrs, labels, inp_ptr, inp_g
    #print(unbleach(code))
    #print(inp)
    normal_termination = False

    code = code_sanitize(code)

    heap = dict()
    labels = dict()
    stack.clear()
    ret_ptrs.clear()

    inp_ptr = 0
    inp_g = inp
    out = ""
    exc_ptr = 0

    labels_search(code)

    while exc_ptr < len(code):
        #print("Stack: " + str(stack._data))
        #print("Heap: " + str(heap))
        #print("Execution ptr:" + str(exc_ptr))
        #print("Code remaining:" + unbleach(code[exc_ptr:]))
        imp, l = parse_imp(code[exc_ptr:])
        exc_ptr += l
        if imp == imps.io:
            l2 = process_io(code[exc_ptr:])
            exc_ptr += l2
        elif imp == imps.stack:
            l2 = process_stack(code[exc_ptr:])
            exc_ptr += l2
        elif imp == imps.arithm:
            l2 = process_arithm(code[exc_ptr:])
            exc_ptr += l2
        elif imp == imps.heap:
            l2 = process_heap(code[exc_ptr:])
            exc_ptr += l2
        elif imp == imps.flow:
            l2 = process_flow(code[exc_ptr:])
            if l2 is None:
                normal_termination = True
                break
            exc_ptr += l2

    if not normal_termination:
        raise WhitespaceInterpretationError
    return out

##print(parse_num(' \t    \n'))
##print(parse_label(' \n'))
##print(whitespace('  \t\t\t\n\t\n \t\n\n\n'))
##print(whitespace('   \t    \t\t\n\t\n  \n\n\n'))
#try:
#    #print(whitespace(bleach('ssstnssstsnsssttnstnttsssssntnstnnn')))
#except WhitespaceInterpretationError:
#    pass

#try:
#    #print(whitespace(bleach('ssstnssstsnsssttnstntstssntnstnnn')))
#except WhitespaceInterpretationError:
#    pass

#try:
#    #print(whitespace(bleach('ssstnssstsnsssttnstnttsssssntnsttnstnnn')))
#except WhitespaceInterpretationError:
#    pass

#try:
#    #print(whitespace(bleach('ssstnssstsnsssttnstntstssntnsttnstnnn')))
#except WhitespaceInterpretationError:
#    pass

##print(whitespace(bleach('ssstnsssttnsssnssstsnsssnssstnnssntnstntsnnnn')))
#print(whitespace(bleach('ssstnssstsnsssttntnstnsnnnsstntnsttnstnnnnssnnsntn')))
