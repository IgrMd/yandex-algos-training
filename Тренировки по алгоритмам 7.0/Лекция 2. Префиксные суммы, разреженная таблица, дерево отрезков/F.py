from dataclasses import dataclass, field
import random


def read_input():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    commands = []
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        commands.append((cmd, a - 1, b))
    return n, m, arr, commands


@dataclass
class Segment:
    l: int
    r: int


@dataclass
class Item:
    seg: Segment
    val: int | float


INF = float('inf')


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
            if initial_i >= len(arr):
                self.arr[i] = Item(Segment(initial_i, initial_i), -INF)
            elif initial_i >= 0:
                self.arr[i] = Item(Segment(initial_i, initial_i), arr[initial_i])
            else:
                l_i, r_i = self._get_children_(i)
                l_child, r_child = self.arr[l_i], self.arr[r_i]
                seg = Segment(l_child.seg.l, r_child.seg.r)
                self.arr[i] = Item(seg, max(l_child.val, r_child.val))

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _upper_bound_(self,
                      i: int,
                      start: int,
                      x: int) -> int:
        me = self.arr[i]
        if me.val < x:
            return -1
        if me.seg.r < start:
            return -1
        if me.seg.l == me.seg.r:
            return me.seg.l
        l_i, r_i = self._get_children_(i)
        ans = -1
        if self.arr[l_i].seg.r >= start:
            ans = self._upper_bound_(l_i, start, x)
        if ans == -1:
            ans = self._upper_bound_(r_i, start, x)
        return ans

    def upper_bound(self, start: int, x: int):
        return self._upper_bound_(0, start, x)

    def update_item(self, i: int, val: int):
        i += self.displacement
        self.arr[i].val = val
        parent = self._get_parent_(i)
        while parent >= 0:
            l_i, r_i = self._get_children_(parent)
            self.arr[parent].val = max(self.arr[l_i].val, self.arr[r_i].val)
            parent = self._get_parent_(parent)


def check_update(arr: list, tree: SegmentTree):
    for i in range(len(arr)):
        if arr[i] != tree.arr[i + tree.displacement].val:
            assert arr[i] == tree.arr[i + tree.displacement].val


def check_upper_bound(arr: list,
                      tree: SegmentTree,
                      start,
                      x):
    pos = tree.upper_bound(start, x)
    ans = -1
    for i in range(start, len(arr)):
        if arr[i] >= x:
            ans = i
            break
    if ans != pos:
        t = SegmentTree(arr)
        t.upper_bound(start, x)
        assert ans == pos


def test():
    while True:
        N = 10  # Размер списка
        K = 100  # Верхняя граница случайных чисел
        arr = [random.randint(0, K) for _ in range(N)]
        cmd_n = random.randint(0, N * 2)
        commands = []
        for _ in range(cmd_n):
            cmd = random.randint(0, 1)
            a = random.randint(0, N - 1)
            b = random.randint(0, N)
            commands.append((cmd, a, b))
        process(0, 0, arr, commands)


def process(n, m, arr, commands):
    ans = []
    tree = SegmentTree(arr)
    for cmd, a, b in commands:
        if cmd == 0:
            tree.update_item(a, b)
            arr[a] = b
            # check_update(arr, tree)
        elif cmd == 1:
            pos = tree.upper_bound(a, b)
            # check_upper_bound(arr, tree, a, b)
            if pos != -1:
                pos += 1
            ans.append(pos)
    print(*ans, sep='\n')


def main():
    # return test()
    process(*read_input())


if __name__ == '__main__':
    main()
