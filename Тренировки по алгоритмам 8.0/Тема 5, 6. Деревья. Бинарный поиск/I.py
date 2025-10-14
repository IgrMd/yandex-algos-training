VARS = set([chr(x) for x in range(ord('a'), ord('z') + 1)])
OPS = {'+', '-', '^', '*', '/'}
OPS1 = {'^'}
OPS2 = {'*', '/'}
OPS3 = {'+', '-'}


def to_polish_notation(s: str):
    stack = []
    ans = []
    for c in s:
        if c == '(':
            stack.append(c)
        if c == ')':
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        if c in OPS3:
            while stack and stack[-1] in OPS:
                ans.append(stack.pop())
            stack.append(c)
        if c in OPS2:
            while stack and (stack[-1] in OPS2 or stack[-1] in OPS1):
                ans.append(stack.pop())
            stack.append(c)
        if c in OPS1:
            stack.append(c)
        if c in VARS:
            ans.append(c)
    while stack:
        ans.append(stack.pop())
    return ''.join(ans)


class Node:
    def __init__(self, left, right, op):
        self.left = Var(left) if isinstance(left, str) else left
        self.right = Var(right) if isinstance(right, str) else right
        self.op = op
        self.is_var = False
        self._h = self._w = None

    def _traverse_(self):
        hl, wl = self.left.h(), self.left.w()
        hr, wr = self.right.h(), self.right.w()
        self._h = max(hl, hr) + 2
        self._w = wl + wr + 5

    def h(self):
        if self._h is None:
            self._traverse_()
        return self._h

    def w(self):
        if self._w is None:
            self._traverse_()
        return self._w

    def __repr__(self):
        return f'{self.left}{self.op}{self.right}'


class Var:
    def __init__(self, val):
        self.val = val
        self.is_var = True

    def __repr__(self):
        return str(self.val)

    def h(self):
        return 1

    def w(self):
        return 1


def syntax_tree(s: str):
    polish = to_polish_notation(s)
    if len(polish) == 1:
        return print(polish)
    stack = []
    for c in polish:
        if c in VARS:
            stack.append(c)
        if c in OPS:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(left, right, c))
    assert len(stack) == 1
    root = stack[0]
    field = [[' '] * root.w() for i in range(root.h())]

    def print_node(curr,
                   level,
                   start):
        row = field[level * 2]
        if curr.is_var:
            row[start] = curr.val
            if level > 0:
                field[level * 2 - 1][start] = '|'
            return start
        l = print_node(curr.left, level + 1, start)
        r = print_node(curr.right, level + 1, start + curr.left.w() + 5)
        for i in range(l, r):
            row[i] = '-'
        row[l] = row[r] = '.'
        me = start + curr.left.w() + 2
        row[me - 1] = '['
        row[me + 1] = ']'
        row[me] = curr.op
        if level > 0:
            field[level * 2 - 1][me] = '|'
        return me

    print_node(root, 0, 0)
    for r in field:
        print(*r, sep='')


if __name__ == '__main__':
    syntax_tree(input().strip())
