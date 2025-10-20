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
        self._h = self._w = None

    def precompute(self):
        self.left.precompute()
        hl, wl = self.left.h(), self.left.w()
        self.right.precompute()
        hr, wr = self.right.h(), self.right.w()
        self._h = max(hl, hr) + 2
        self._w = wl + wr + 5

    def h(self):
        return self._h

    def w(self):
        return self._w

    def print(self, field, level=0, start=0):
        row = field[level * 2]
        l = self.left.print(field, level + 1, start)
        r = self.right.print(field, level + 1, start + self.left.w() + 5)
        for i in range(l, r):
            row[i] = '-'
        row[l] = row[r] = '.'
        me = start + self.left.w() + 2
        row[me - 1] = '['
        row[me + 1] = ']'
        row[me] = self.op
        if level > 0:
            field[level * 2 - 1][me] = '|'
        return me


class Var:
    def __init__(self, val):
        self.val = val

    def h(self):
        return 1

    def w(self):
        return 1

    def precompute(self):
        pass

    def print(self, field, level=0, start=0):
        row = field[level * 2]
        row[start] = self.val
        if level > 0:
            field[level * 2 - 1][start] = '|'
        return start


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
    root.precompute()
    field = [[' '] * root.w() for i in range(root.h())]
    root.print(field)
    for r in field:
        print(''.join(r))


if __name__ == '__main__':
    syntax_tree(input().strip())
