def input_read():
    n = int(input().strip())
    w = input().strip()
    s = input().strip()
    return n, w, s


BRACE_MAP = {
    '[': ']',
    ']': '[',
    '(': ')',
    ')': '(',
}


def generate_min_seq(sorted_orders, size):
    ans = ''
    stack = []

    def first_open():
        for c, _ in sorted_orders:
            if c == '(' or c == '[':
                return c

    def first_can_add():
        for c, _ in sorted_orders:
            if c == ']' or c == ')':
                if stack[-1] == BRACE_MAP[c]:
                    return c
            if c == '(' or c == '[':
                return c

    while len(ans) < size:
        if not stack:
            c = first_open()
            stack.append(c)
            ans += c
            continue
        if len(stack) < size - len(ans):
            c = first_can_add()
            ans += c
            if c == '(' or c == '[':
                stack.append(c)
            else:
                stack.pop()
            continue
        ans += BRACE_MAP[stack.pop()]
    return ans


def min_brace_sequence(n: int, w: str, s: str):
    orders = {}
    for i, c in enumerate(w):
        orders[c] = i
    sorted_orders = sorted(orders.items(), key=lambda x: x[1])
    stack = []
    for brace in s:
        if brace == '(' or brace == '[':
            stack.append(brace)
        else:
            stack.pop()

    def first_open():
        for c, _ in sorted_orders:
            if c == '(' or c == '[':
                return c

    def first_can_add():
        for c, _ in sorted_orders:
            if c == ']' or c == ')':
                if stack[-1] == BRACE_MAP[c]:
                    return c
            if c == '(' or c == '[':
                return c

    while len(s) < n:
        if not stack:
            c = first_open()
            s += c
            stack.append(c)
            continue
        if len(stack) < n - len(s):
            c = first_can_add()
            s += c
            if c == '(' or c == '[':
                stack.append(c)
            else:
                stack.pop()
            continue
        s += BRACE_MAP[stack.pop()]

    return s


def main():
    print(min_brace_sequence(*input_read()))


if __name__ == '__main__':
    main()
