symbols = '!^&|()'
priorities = {'(': -1, '|': 0, '^': 0, '&': 1, '!': 2}


def to_tokens(s):
    tokens = []
    for c in s:
        if c in symbols:
            tokens.append(c)
            continue
        if c == '0':
            tokens.append(0)
        if c == '1':
            tokens.append(1)
    return tokens


def to_polish_notation(tokens):
    stack = []
    notation = []
    for token in tokens:
        if type(token) == int:
            notation.append(token)
            continue
        if token in '!^|&':
            while len(stack) and priorities[token] <= priorities[stack[-1]]:
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
    binary_opers = {'&': lambda x1, x2: x1 & x2,
                    '|': lambda x1, x2: x1 | x2,
                    '^': lambda x1, x2: x1 ^ x2}
    if notation is None:
        return 'WRONG'
    stack = []
    for token in notation:
        if token in binary_opers:
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(binary_opers[token](x1, x2))
            continue
        if token == '!':
            x = stack.pop()
            stack.append(int(not x))
            continue
        stack.append(int(token))
    return stack.pop()

assert calculate(to_polish_notation(to_tokens('!1'))) == 0
assert calculate(to_polish_notation(to_tokens('1|(0&0^1)'))) == 1
assert calculate(to_polish_notation(to_tokens('!1|!(0&0^1)'))) == 0


def main():
    s = input()
    print(calculate(to_polish_notation(to_tokens(s))))


if __name__ == '__main__':
    main()
