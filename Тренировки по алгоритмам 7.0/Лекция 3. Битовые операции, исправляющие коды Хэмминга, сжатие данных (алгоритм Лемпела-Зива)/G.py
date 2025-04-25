import sys


class FenwickTree:
    def __init__(self, n):
        self.arr = [0] * n
        self.t = [0] * n
        self.n = n

    @staticmethod
    def _f_(i: int):
        return i & (i + 1)

    def _pref_sum_(self, i):
        ans = 0
        while i >= 0:
            ans += self.t[i]
            i = self._f_(i) - 1
        return ans

    def sum(self, l: int, r: int):
        return self._pref_sum_(r) - self._pref_sum_(l - 1)

    def update(self, i: int, val: int):
        add = val - self.arr[i]
        self.arr[i] = val
        while i < self.n:
            self.t[i] += add
            i |= i + 1


def main():
    n, k = map(int, input().split())
    # n, k = map(int, sys.stdin.readline().split())
    tree = FenwickTree(n)
    for _ in range(k):
        request = input().split()
        # request = sys.stdin.readline().split()
        if request[0] == 'A':
            i, x = map(int, request[1:])
            i -= 1
            tree.update(i, x)
        else:
            l, r = map(int, request[1:])
            l -= 1
            r -= 1
            print(tree.sum(l, r))


if __name__ == '__main__':
    main()
