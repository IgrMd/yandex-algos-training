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
    val: int | float = field(default=INF)

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
                self.arr[i].val = 0

    def update_range(self, rng: Range, add: int):
        self._update_range_(0, rng, add)

    def _update_range_(self, i: int, rng: Range, add: int):
        if i >= self.n:
            return
        me = self.arr[i]
        if rng.r < me.rng.l or rng.l > me.rng.r:  # ranges not crossed
            return
        if rng.l <= me.rng.l and me.rng.r <= rng.r:  # me in request range
            me.val += add
            return
        l_i, r_i = self._get_children_(i)
        self._update_range_(l_i, rng, add)
        self._update_range_(r_i, rng, add)

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _query_impl_(self,
                     i: int,
                     g: int):
        me = self.arr[i]
        if i - self.displacement == g:
            return me.val
        l_i, r_i = self._get_children_(i)
        l_c, r_c = self.arr[l_i], self.arr[r_i]
        l_c.val += me.val
        r_c.val += me.val
        me.val = 0
        if g <= l_c.rng.r:
            return self._query_impl_(l_i, g)
        if g >= r_c.rng.l:
            return self._query_impl_(r_i, g)

    def query(self, g: int):
        return self._query_impl_(0, g)


def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    m = int(input().strip())
    tree = SegmentTree(arr)
    for _ in range(m):
        cmd = input().split()
        if cmd[0] == 'g':
            print(tree.query(int(cmd[1]) - 1))
        else:
            tree.update_range(Range(int(cmd[1]) - 1, int(cmd[2]) - 1), int(cmd[3]))


if __name__ == '__main__':
    main()
