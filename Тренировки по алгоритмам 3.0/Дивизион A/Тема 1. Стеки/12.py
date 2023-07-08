symbols = '1234567890+-*() '


def to_tokens(s):
    brace_balance = 0
    if not len(s):
        return None
    tokens = []
    i = 0
    while i < len(s):
        if s[i] not in symbols:
            return None
        if s[i] == ' ':
            i += 1
            continue
        if s[i] == '(':
            if len(tokens) and str(tokens[-1]) not in '(*-+':
                return None
            brace_balance += 1
            tokens.append(s[i])
            i += 1
            continue
        if s[i] == ')':
            brace_balance -= 1
            if brace_balance < 0:
                return None
            if str(tokens[-1]) in '(*-+':
                return None
            tokens.append(s[i])
            i += 1
            continue
        if s[i] in '+-*':
            if str(tokens[-1]) in '(+-*':
                return None
            tokens.append(s[i])
            i += 1
            continue
        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        if len(num):
            if len(tokens) and type(tokens[-1]) == int:
                return None
            if len(tokens) and tokens[-1] not in '(*-+':
                return None
            tokens.append(int(num))
            num = ''
            continue
    if brace_balance > 0:
        return None
    if str(tokens[-1]) in '-+*':
        return None
    return tokens


def to_polish_notation(tokens):
    if tokens is None or not len(tokens):
        return None
    stack = []
    notation = []
    for token in tokens:
        if type(token) == int:
            notation.append(token)
            continue
        if token in '+-*':
            if token == '-' or token == '+':
                while len(stack) and stack[-1] != '(':
                    notation.append(stack.pop())
                stack.append(token)
                continue
            if token == '*':
                while len(stack) and stack[-1] == '*':
                    notation.append(stack.pop())
                stack.append(token)
                continue
        if token == '(':
            stack.append(token)
            continue
        if token == ')':
            while len(stack) and stack[-1] != '(':
                notation.append(stack.pop())
            stack.pop()
            continue
    while len(stack):
        notation.append(stack.pop())
    return notation


def calculate(notation):
    opers = {'+': lambda x1, x2: x2 + x1,
             '-': lambda x1, x2: x2 - x1,
             '*': lambda x1, x2: x2 * x1}
    if notation is None:
        return 'WRONG'

    stack = []
    for c in notation:
        if c == '+' or c == '-' or c == '*':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(opers[c](x1, x2))
            continue
        stack.append(int(c))
    return stack.pop()


a = '(1+(7+8)-(3-4*5)*(2*4)+(9)-(16728)*(123*9+2)+((2)))+((((((0-19283))))))'
assert calculate(to_polish_notation(to_tokens(a))) == -18570472
assert calculate(to_polish_notation(to_tokens('1 1 + 2'))) == 'WRONG'
assert calculate(to_polish_notation(to_tokens('1+a+1'))) == 'WRONG'
assert calculate(to_polish_notation(to_tokens('1+(2*2 - 3)'))) == 2
assert calculate(to_polish_notation(to_tokens('1*2*3+(*4*5*6*7+8*9)'))) == 'WRONG'


def main():
    s = input()
    print(calculate(to_polish_notation(to_tokens(s))))


if __name__ == '__main__':
    main()
