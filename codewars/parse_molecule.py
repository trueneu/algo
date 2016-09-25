import string
from copy import deepcopy

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


atoms = dict()

braces = ['(', ')']
left_braces = ['(']
right_braces = [')']
precedence = {'*': 3, '+': 2, '(': 1}


def tokenize_formula(formula):
    tokens = list()
    unpushed_char = ''
    prev_token_is_atom = False
    prev_token_is_digit = False
    prev_token_is_right_brace = False
    i = 0
    while i < len(formula):
        c = formula[i]
        if c in string.ascii_lowercase:
            if prev_token_is_right_brace or prev_token_is_digit:
                tokens.append('+')
            tokens.append(unpushed_char + c)
#            if prev_token_is_atom or prev_token_is_digit:
#                tokens.append('+')
            unpushed_char = ''
            prev_token_is_atom = True
            prev_token_is_digit = False
            prev_token_is_right_brace = False
        elif c in string.ascii_uppercase:
            if unpushed_char:
                if prev_token_is_right_brace or prev_token_is_digit:
                    tokens.append('+')
                tokens.append(unpushed_char)
                tokens.append('+')
                prev_token_is_atom = False
                prev_token_is_digit = False
                prev_token_is_right_brace = False
            if i == len(formula) - 1:
                tokens.append('+')
                tokens.append(c)
                unpushed_char = ''
            else:
                unpushed_char = c
        else:
            if unpushed_char:
                if prev_token_is_atom or prev_token_is_digit:
                    tokens.append('+')
                tokens.append(unpushed_char)
                unpushed_char = ''
                prev_token_is_atom = True
                prev_token_is_digit = False
                prev_token_is_right_brace = False
            if c in string.digits:
                num_str = c
                i += 1
                while i < len(formula) and formula[i] in string.digits:
                    num_str += formula[i]
                    i += 1
                i -= 1
                tokens.append('*')
                tokens.append(num_str)
                prev_token_is_digit = True
                prev_token_is_right_brace = False
            if c in left_braces:
                if prev_token_is_atom or prev_token_is_digit or prev_token_is_right_brace:
                    tokens.append('+')
                tokens.append(c)
                prev_token_is_digit = False
                prev_token_is_right_brace = False
            if c in right_braces:
                tokens.append(c)
                prev_token_is_digit = False
                prev_token_is_right_brace = True
            prev_token_is_atom = False
        i += 1
    if unpushed_char:
        tokens.append(unpushed_char)
    return tokens

def infix_to_postfix(tokens):
    ops = ['+', '-', '/','*']
    prec = {'+': 0, '-': 0, '/': 1, '*': 1, '(': -1}
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


def sanitize_braces(formula):
    return formula.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')

def postfix_to_molecule(expression):
    stack = Stack()
    for token in expression:
        if token[0] in string.ascii_letters:
            stack.push({token: 1})
        elif token[0] in string.digits:
            stack.push(int(token))
        elif token == '*':
            mult = stack.pop()
            atoms = stack.pop()
            for k in atoms.keys():
                atoms[k] *= mult
            stack.push(atoms)
        elif token == '+':
            atom1 = stack.pop()
            atom2 = stack.pop()
            r = deepcopy(atom2)
            for k in atom1.keys():
                if k in atom2.keys():
                    r[k] = atom1[k] + atom2[k]
                else:
                    r[k] = atom1[k]
            stack.push(r)
    return stack.pop()


def parse_molecule(formula):
    print(formula)
    return postfix_to_molecule(infix_to_postfix(tokenize_formula(sanitize_braces(formula))))

#parse_molecule("HHO")
print(parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3"))


#parse_molecule("H2O")
#parse_molecule("Mg(OH)2")
#parse_molecule("K4[ON(SO3)2]2")