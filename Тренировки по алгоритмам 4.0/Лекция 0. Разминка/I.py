def read_input():
    return input().strip()


def is_correct_sequence(sequence):
    stack = []
    brace_map = {')': '(', ']': '[', '}': '{'}
    for brace in sequence:
        if brace == '(' or brace == '[' or brace == '{':
            stack.append(brace)
            continue
        if not len(stack):
            return False
        if stack.pop() != brace_map[brace]:
            return False
    if len(stack):
        return False
    return True


def main():
    print('yes' if is_correct_sequence(read_input()) else 'no')


if __name__ == '__main__':
    main()
