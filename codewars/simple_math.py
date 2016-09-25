class Stack(object):
    def __init__(self):
        self._data = list()

    def push(self, data):
        self._data.append(data)

    def pop(self):
        try:
            x = self._data.pop()
        except IndexError:
            return None
        return x

    def size(self):
        return len(self._data)

def infix_to_postfix(expression):
    ops = ['+', '-', '/','*']
    prec = {'+': 0, '-': 0, '/': 1, '*': 1, '(': -1}
    left_parenthesis = ['(']
    right_parenthesis = [')']
    opstack = Stack()
    output = list()
    tokens = expression.split()
    for token in tokens:
        if token in ops:
            n = opstack.pop()
            if n:
                while prec[n] >= prec[token]:
                    output.append(n)
                    n = opstack.pop()
                    if not n:
                        break
            if n:
                opstack.push(n)
            opstack.push(token)

        elif token in left_parenthesis:
            opstack.push(token)
        elif token in right_parenthesis:
            n = opstack.pop()
            if n:
                while n not in left_parenthesis:
                    output.append(n)
                    n = opstack.pop()
                    if not n:
                        break
        else:
            output.append(token)

    n = opstack.pop()
    while n:
        output.append(n)
        n = opstack.pop()
    return output


def evaluate(expression):
    pass

print(infix_to_postfix("( ( A + B ) * C + D * E )"))