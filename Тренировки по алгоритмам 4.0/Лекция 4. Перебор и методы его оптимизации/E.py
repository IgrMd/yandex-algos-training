import datetime


def read_input():
    n = int(input().strip())
    return n


BRACE_MAP = {')': '(', ']': '['}


def is_correct_sequence(sequence, begin, end):
    stack = []
    for i in range(begin, end):
        brace = sequence[i]
        if brace == '(' or brace == '[':
            stack.append(brace)
            continue
        if not len(stack):
            return False
        if stack.pop() != BRACE_MAP[brace]:
            return False
    if len(stack):
        return False
    return True


def generate(sequence: list, n, t: int, op1, cl1, op2, cl2):
    if (op1 + op2) == n // 2:
        stack = []
        for i in range(t):
            brace = sequence[i]
            if brace == '(' or brace == '[':
                stack.append(brace)
                continue
            if not len(stack):
                return
            if stack.pop() != BRACE_MAP[brace]:
                return
        while len(stack):
            sequence[t] = ')' if stack.pop() == '(' else ']'
            t += 1
        return print(*sequence, sep='')
        # return
    if cl1 > op1 or cl2 > op2:
        return
    if cl1 == op1 and cl2 == op2:
        if not is_correct_sequence(sequence, 0, t):
            return
    sequence[t] = '('
    generate(sequence, n, t + 1, op1 + 1, cl1, op2, cl2)
    sequence[t] = '['
    generate(sequence, n, t + 1, op1, cl1, op2 + 1, cl2)
    sequence[t] = ')'
    generate(sequence, n, t + 1, op1, cl1 + 1, op2, cl2)
    sequence[t] = ']'
    generate(sequence, n, t + 1, op1, cl1, op2, cl2 + 1)


def sequences(n):
    if n % 2:
        return
    sequence = [None for _ in range(n)]
    generate(sequence, n, 0, 0, 0, 0, 0)


def main():
    # start = datetime.datetime.now()
    sequences(read_input())
    # print(datetime.datetime.now() - start)


if __name__ == '__main__':
    main()
