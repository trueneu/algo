import re
import string

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


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

def infix_to_postfix(tokens):
    ops = ['+', '-', '/', '*', '=', '%']
    prec = {'+': 0, '-': 0, '/': 1, '*': 1, '(': -1, '=': -2, '%': 1}
    left_parenthesis = ['(']
    right_parenthesis = [')']
    opstack = Stack()
    output = list()
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


class InterpreterError(Exception):
    def __init__(self):
        super(InterpreterError, self)

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def convert_var_if_needed(self, token):
        if type(token) is str:
            if token[0] in string.ascii_letters:
                if token in self.vars.keys():
                    return self.vars[token]
                else:
                    raise InterpreterError
            else:
                return int(token)
        else:
            return token

    def do_the_math(self, postfix):
        stack = Stack()
        output = ""
        for token in postfix:
            if token[0] in string.ascii_letters or token[0] in string.digits:
                stack.push(token)
            elif token == '+':
                a = self.convert_var_if_needed(stack.pop())
                b = self.convert_var_if_needed(stack.pop())
                stack.push(a + b)
            elif token == '-':
                a = self.convert_var_if_needed(stack.pop())
                b = self.convert_var_if_needed(stack.pop())
                stack.push(b - a)
            elif token == '*':
                a = self.convert_var_if_needed(stack.pop())
                b = self.convert_var_if_needed(stack.pop())
                stack.push(a * b)
            elif token == '/':
                a = self.convert_var_if_needed(stack.pop())
                b = self.convert_var_if_needed(stack.pop())
                stack.push(b // a)
            elif token == '%':
                a = self.convert_var_if_needed(stack.pop())
                b = self.convert_var_if_needed(stack.pop())
                stack.push(b % a)
            elif token == '=':
                a = self.convert_var_if_needed(stack.pop())
                b = stack.pop()
                if b[0] in string.ascii_letters:
                    self.vars[b] = a
                    output = a
                else:
                    raise InterpreterError
        if stack.size():
            output = self.convert_var_if_needed(stack.pop())
        if stack.size():
            raise InterpreterError
        return output


    def input(self, expression):
        tokens = tokenize(expression)
        postfix = infix_to_postfix(tokens)
        return self.do_the_math(postfix)

interpreter = Interpreter()
print(interpreter.input("x = 13 + (y = 3)"))
print(interpreter.input("x"))
print(interpreter.input("y"))
print(interpreter.input("z = x + y"))
print(interpreter.input("z"))


