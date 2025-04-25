import sys


class FenwickCube:
    def __init__(self, n):
        self.t = [[[0] * n for _ in range(n)] for __ in range(n)]
        self.n = n

    def _pref_sum_(self,
                   x: int, y: int, z: int):
        ans = 0
        xi = x
        while xi >= 0:
            yi = y
            while yi >= 0:
                zi = z
                while zi >= 0:
                    ans += self.t[xi][yi][zi]
                    zi = (zi & (zi + 1)) - 1
                yi = (yi & (yi + 1)) - 1
            xi = (xi & (xi + 1)) - 1
        return ans

    def sum(self,
            x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
        s1 = self._pref_sum_(x2, y2, z2)
        s2 = self._pref_sum_(x2, y2, z1 - 1)
        s3 = self._pref_sum_(x2, y1 - 1, z2)
        s4 = self._pref_sum_(x1 - 1, y2, z2)
        s5 = self._pref_sum_(x1 - 1, y1 - 1, z2)
        s6 = self._pref_sum_(x1 - 1, y2, z1 - 1)
        s7 = self._pref_sum_(x2, y1 - 1, z1 - 1)
        s8 = self._pref_sum_(x1 - 1, y1 - 1, z1 - 1)
        return s1 - s2 - s3 - s4 + s5 + s6 + s7 - s8

    def update(self,
               x: int, y: int, z: int, val: int):
        xi = x
        while xi < self.n:
            yi = y
            while yi < self.n:
                zi = z
                while zi < self.n:
                    self.t[xi][yi][zi] = max(val + self.t[xi][yi][zi], 0)
                    zi |= zi + 1
                yi |= yi + 1
            xi |= xi + 1


def main():
    # n = int(input().strip())
    n = int(sys.stdin.readline().strip())
    tree = FenwickCube(n)
    while True:
        # request = input().split()
        request = sys.stdin.readline().split()
        if request[0] == '1':
            x, y, z, val = map(int, request[1:])
            tree.update(x, y, z, val)
        if request[0] == '2':
            print(tree.sum(*map(int, request[1:])))
        if request[0] == '3':
            break


if __name__ == '__main__':
    main()
