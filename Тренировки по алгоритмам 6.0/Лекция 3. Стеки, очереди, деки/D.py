def input_read():
    return input().split()


OPERATORS = {
    '-': lambda x1, x2: x1 - x2,
    '+': lambda x1, x2: x1 + x2,
    '*': lambda x1, x2: x1 * x2,
}


def calc(tokens):
    stack = []
    for token in tokens:
        if token in OPERATORS:
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(OPERATORS[token](x1, x2))
            continue
        stack.append(int(token))

    return stack[0]


def main():
    print(calc(input_read()))


if __name__ == '__main__':
    main()
