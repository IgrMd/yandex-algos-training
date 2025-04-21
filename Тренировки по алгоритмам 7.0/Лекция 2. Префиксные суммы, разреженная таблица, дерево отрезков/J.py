from dataclasses import dataclass, field

X = 257
P = 10 ** 9 + 7


# X = 10
# P = 10 ** 9


@dataclass
class Segment:
    l: int
    r: int

    def __len__(self):
        return self.r - self.l + 1

    def __repr__(self):
        return f'[{self.l}, {self.r}]'


INF = float('inf')


@dataclass
class Item:
    seg: Segment
    val: int | float = field(default=0)
    prom: int = field(default=0)

    def len(self):
        return len(self.seg)

    def __repr__(self):
        return f'{self.seg}, v={self.val}'


class SegmentTree:
    def __init__(self, arr: list[int]):
        pow_of_2 = 1
        while pow_of_2 < len(arr):
            pow_of_2 *= 2
        self.n = 2 * pow_of_2 - 1
        self.displacement = pow_of_2 - 1
        self.arr: list[Item | None] = [None] * self.n
        self.x = [1] * len(arr)
        self.x_sum = [1] * len(arr)
        for i in range(1, len(arr)):
            self.x[i] = (self.x[i - 1] * X) % P
            self.x_sum[i] = (self.x_sum[i - 1] + self.x[i]) % P
        for i in range(self.n - 1, -1, -1):
            initial_i = i - self.displacement
            if initial_i >= 0:
                self.arr[i] = Item(Segment(initial_i, initial_i))
                if initial_i < len(arr):
                    self.arr[i].val = arr[initial_i]
            else:
                l_i, r_i = self._get_children_(i)
                self.arr[i] = Item(Segment(self.arr[l_i].seg.l, self.arr[r_i].seg.r))
                self.arr[i].val = (self.arr[l_i].val * self.x[self.arr[l_i].len()] + self.arr[r_i].val) % P
        pass

    def update_range(self, seg: Segment, val: int):
        self._update_range_(0, seg, val)

    def query(self,
              l: int,
              r: int,
              k: int):
        hash1 = self._query_impl_(0, Segment(l, l + k - 1))[0]
        hash2 = self._query_impl_(0, Segment(r, r + k - 1))[0]
        return hash1 == hash2

    def _touch_promise(self, i: int):
        me = self.arr[i]
        if len(me.seg) > 1:
            l_i, r_i = self._get_children_(i)
            l_c, r_c = self.arr[l_i], self.arr[r_i]
            l_c.val = r_c.val = (self.x_sum[r_c.len() - 1] * me.prom) % P
            l_c.prom = me.prom
            r_c.prom = me.prom
        me.prom = 0

    def _update_range_(self, i: int, seg: Segment, val: int):
        me = self.arr[i]
        if seg.r < me.seg.l or seg.l > me.seg.r:  # segments not crossed
            return
        if seg.l <= me.seg.l and me.seg.r <= seg.r:  # me in request range
            me.val = (self.x_sum[me.len() - 1] * val) % P
            me.prom = val
            return
        if me.prom > 0:
            self._touch_promise(i)
        l_i, r_i = self._get_children_(i)
        self._update_range_(l_i, seg, val)
        self._update_range_(r_i, seg, val)
        self.arr[i].val = (self.arr[l_i].val * self.x[self.arr[l_i].len()] + self.arr[r_i].val) % P

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _query_impl_(self,
                     i: int,
                     seg: Segment):
        me = self.arr[i]
        if seg.r < me.seg.l or seg.l > me.seg.r:  # segments not crossed
            return 0, 0
        if seg.l <= me.seg.l and me.seg.r <= seg.r:  # me in request range
            return me.val, me.len()
        if me.prom > 0:
            self._touch_promise(i)
        l_i, r_i = self._get_children_(i)
        l_ans = self._query_impl_(l_i, seg)
        r_ans = self._query_impl_(r_i, seg)
        h = (l_ans[0] * self.x[r_ans[1]] + r_ans[0]) % P
        return h, l_ans[1] + r_ans[1]


def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    q = int(input().strip())
    tree = SegmentTree(arr)
    for _ in range(q):
        t, l, r, k = map(int, input().split())
        l -= 1
        r -= 1
        if t == 0:
            tree.update_range(Segment(l, r), k)
        else:
            if tree.query(l, r, k):
                print('+', end='')
            else:
                print('-', end='')


if __name__ == '__main__':
    main()
