def read_input():
    n = int(input().strip())
    return n


def is_correct_sequence(sequence, begin, end):
    stack = []
    brace_map = {')': '(', ']': '['}
    for i in range(begin, end):
        brace = sequence[i]
        if brace == '(' or brace == '[':
            stack.append(brace)
            continue
        if not len(stack):
            return False
        if stack.pop() != brace_map[brace]:
            return False
    if len(stack):
        return False
    return True


def generate(sequence: list, n, t: int, op1, cl1, op2, cl2):
    if cl1 > op1 or cl2 > op2:
        return
    if (op1 + op2) > n // 2:
        return
    if cl1 == op1 and cl2 == op2:
        if not is_correct_sequence(sequence, 0, t):
            return
    if t == n:
        if is_correct_sequence(sequence, 0, t):
            print(*sequence, sep='')
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
    sequences(read_input())


if __name__ == '__main__':
    main()
