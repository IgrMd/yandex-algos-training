import time
from dataclasses import dataclass, field


def read_input():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    m = int(input().strip())
    commands = []
    for _ in range(m):
        cmd, a, b = input().split()
        if cmd[0] == 'Q':
            commands.append((cmd[0], int(a) - 1, int(b) - 1))
        else:
            commands.append((cmd[0], int(a) - 1, int(b)))
    return n, m, arr, commands


@dataclass
class Segment:
    l: int
    r: int

    def __len__(self):
        return self.r - self.l + 1

    def __repr__(self):
        return f'[{self.l}, {self.r}]'


@dataclass
class Item:
    seg: Segment
    val: int | float = field(default=0)
    prf: int = field(default=0)
    suf: int = field(default=0)

    def __repr__(self):
        return f'{self.seg}, v={self.val}, p={self.prf}, s={self.suf}]'


INF = float('inf')


class SegmentTree:
    def __init__(self, arr: list[int]):
        self._init_buffer_(arr)

    def _init_buffer_(self, arr: list[int]):
        pow_of_2 = 1
        while pow_of_2 < len(arr):
            pow_of_2 *= 2
        self.n = 2 * pow_of_2 - 1
        self.displacement = pow_of_2 - 1
        self.arr: list[Item | None] = [None] * self.n
        for i in range(self.n - 1, -1, -1):
            initial_i = i - self.displacement
            if initial_i >= len(arr):
                self.arr[i] = Item(Segment(initial_i, initial_i))
            elif initial_i >= 0:
                self.arr[i] = Item(Segment(initial_i, initial_i))
                if arr[initial_i] == 0:
                    self.arr[i].val = self.arr[i].prf = self.arr[i].suf = 1
            else:
                l_i, r_i = self._get_children_(i)
                self.arr[i] = Item(Segment(self.arr[l_i].seg.l, self.arr[r_i].seg.r))
                self._update_item_(i)

    def _update_item_(self, i: int):
        me = self.arr[i]
        l_i, r_i = self._get_children_(i)
        l_c, r_c = self.arr[l_i], self.arr[r_i]
        me.val = max(l_c.val, r_c.val)
        if len(l_c.seg) == l_c.val and len(r_c.seg) == r_c.val:
            me.val = me.prf = me.suf = len(me.seg)
        elif len(l_c.seg) == l_c.val:
            me.prf = l_c.val + r_c.prf
            me.suf = r_c.suf
        elif len(r_c.seg) == r_c.val:
            me.suf = r_c.val + l_c.suf
            me.prf = l_c.prf
        else:
            me.prf = l_c.prf
            me.suf = r_c.suf
        me.val = max(me.val, me.suf, me.prf, l_c.suf + r_c.prf)

    def update_item(self, i: int, val: int):
        i += self.displacement
        self.arr[i].val = self.arr[i].prf = self.arr[i].suf = int(val == 0)
        parent = self._get_parent_(i)
        while parent >= 0:
            self._update_item_(parent)
            parent = self._get_parent_(parent)

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _query_impl_(self,
                     i: int,
                     seg: Segment):
        if i >= self.n:
            return 0, 0, 0
        me = self.arr[i]
        if seg.r < me.seg.l or seg.l > me.seg.r:  # segments not crossed
            return 0, 0, 0
        if seg.l <= me.seg.l and me.seg.r <= seg.r:  # me in request range
            return me.val, me.prf, me.suf
        l_i, r_i = self._get_children_(i)
        l_c, r_c = self.arr[l_i], self.arr[r_i]
        l_val, l_prf, l_suf = self._query_impl_(l_i, seg)
        r_val, r_prf, r_suf = self._query_impl_(r_i, seg)
        val = max(l_val, r_val)
        prf = l_val + r_prf if len(l_c.seg) == l_val else l_prf
        suf = r_val + l_suf if len(r_c.seg) == r_val else r_suf
        val = max(val, prf, suf, l_suf + r_prf)
        return val, prf, suf

    def query(self, seg: Segment):
        return self._query_impl_(0, seg)[0]


def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    m = int(input().strip())
    tree = SegmentTree(arr)
    for _ in range(m):
        cmd, a, b = input().split()
        if cmd[0] == 'Q':
            seg = Segment(int(a) - 1, int(b) - 1)
            print(tree.query(seg))
        else:
            tree.update_item(int(a) - 1, int(b))


if __name__ == '__main__':
    main()
