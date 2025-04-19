from dataclasses import dataclass, field


@dataclass
class Range:
    l: int
    r: int

    def __len__(self):
        return self.r - self.l + 1

    def __repr__(self):
        return f'[{self.l}, {self.r}]'


INF = float('inf')


@dataclass
class Item:
    rng: Range
    val: int | float = field(default=-INF)
    prom: int = field(default=0)

    def __repr__(self):
        return f'{self.rng}, v={self.val}'


class SegmentTree:
    def __init__(self, arr: list[int]):
        self._init_buffer_(arr)

    def _init_buffer_(self, arr: list[int]):
        k = 0
        while 2 ** k < len(arr):
            k += 1
        pow_of_2: int = 2 ** k
        self.n = 2 * pow_of_2 - 1
        self.displacement = pow_of_2 - 1
        self.arr: list[Item | None] = [None] * self.n
        for i in range(self.n - 1, -1, -1):
            initial_i = i - self.displacement
            if initial_i >= 0:
                self.arr[i] = Item(Range(initial_i, initial_i))
                if initial_i < len(arr):
                    self.arr[i].val = arr[initial_i]
            else:
                l_i, r_i = self._get_children_(i)
                self.arr[i] = Item(Range(self.arr[l_i].rng.l, self.arr[r_i].rng.r))
                self.arr[i].val = max(self.arr[l_i].val, self.arr[r_i].val)

    def update_range(self, rng: Range, add: int):
        self._update_range_(0, rng, add)

    def query(self, rng: Range):
        return self._query_impl_(0, rng)

    def _touch_promise(self, i: int):
        me = self.arr[i]
        if len(me.rng) > 1:
            l_i, r_i = self._get_children_(i)
            l_c, r_c = self.arr[l_i], self.arr[r_i]
            l_c.val += me.prom
            l_c.prom += me.prom
            r_c.val += me.prom
            r_c.prom += me.prom
        me.prom = 0

    def _update_range_(self, i: int, rng: Range, add: int):
        me = self.arr[i]
        if rng.r < me.rng.l or rng.l > me.rng.r:  # ranges not crossed
            return me.val
        if rng.l <= me.rng.l and me.rng.r <= rng.r:  # me in request range
            me.val += add
            me.prom += add
            return me.val
        if me.prom > 0:
            self._touch_promise(i)
        l_i, r_i = self._get_children_(i)
        l_max = self._update_range_(l_i, rng, add)
        r_max = self._update_range_(r_i, rng, add)
        me.val = max(l_max, r_max)
        return me.val

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _query_impl_(self,
                     i: int,
                     rng: Range):
        me = self.arr[i]
        if rng.r < me.rng.l or rng.l > me.rng.r:  # ranges not crossed
            return -INF
        if rng.l <= me.rng.l and me.rng.r <= rng.r:  # me in request range
            return me.val
        if me.prom > 0:
            self._touch_promise(i)
        l_i, r_i = self._get_children_(i)
        l_max = self._query_impl_(l_i, rng)
        r_max = self._query_impl_(r_i, rng)
        return max(l_max, r_max)


def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    m = int(input().strip())
    tree = SegmentTree(arr)
    for _ in range(m):
        cmd = input().split()
        rng = Range(int(cmd[1]) - 1, int(cmd[2]) - 1)
        if cmd[0] == 'm':
            print(tree.query(rng), end=' ')
        else:
            tree.update_range(rng, int(cmd[3]))


if __name__ == '__main__':
    main()
