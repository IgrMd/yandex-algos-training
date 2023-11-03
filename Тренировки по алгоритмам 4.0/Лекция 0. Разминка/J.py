def read_input():
    t = int(input().strip())
    cases = [[int(x) for x in input().split()] for _ in range(t)]
    return cases


def can_form_groups(n, a, b):
    group_count = n // a
    rest = n % a
    if rest % group_count == 0:
        if rest // group_count <= b - a:
            return True
        else:
            return False
    else:
        if rest // group_count + 1 <= b - a:
            return True
        else:
            return False


def groups(cases):
    for n, a, b in cases:
        print('YES' if can_form_groups(n, a, b) else 'NO')


def main():
    groups(read_input())


if __name__ == '__main__':
    main()
