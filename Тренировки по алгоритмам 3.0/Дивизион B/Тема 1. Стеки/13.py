opers = {'+': lambda x1, x2: x2 + x1,
         '-': lambda x1, x2: x2 - x1,
         '*': lambda x1, x2: x2 * x1}


def solve(sequence):
    stack = []
    for c in sequence:
        if c == '+' or c == '-' or c == '*':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(opers[c](x1, x2))
            continue
        stack.append(int(c))
    return stack.pop()


def main():
    print(solve(input().split()))


if __name__ == '__main__':
    main()
