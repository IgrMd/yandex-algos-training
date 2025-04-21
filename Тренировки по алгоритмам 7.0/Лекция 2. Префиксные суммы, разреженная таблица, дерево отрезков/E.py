from dataclasses import dataclass


def read_input():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    return arr


@dataclass
class Segment:
    l: int
    r: int


@dataclass
class Item:
    min: int | float
    count: int
    seg: Segment


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
                self.arr[i] = Item(INF, 0, Segment(initial_i, initial_i))
            elif initial_i >= 0:
                self.arr[i] = Item(arr[initial_i], 1, Segment(initial_i, initial_i))
            else:
                l_child_i, r_child_i = self._get_children_(i)
                l_child, r_child = self.arr[l_child_i], self.arr[r_child_i]
                cur_min = min(l_child.min, r_child.min)
                seg = Segment(l_child.seg.l, r_child.seg.r)
                cur_count = 0
                for child in (l_child, r_child):
                    if child.min == cur_min:
                        cur_count += child.count
                self.arr[i] = Item(cur_min, cur_count, seg)

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _find_min_count_impl_(self, i: int, request: Segment):
        if i >= self.n:
            return INF, 0
        me = self.arr[i]
        if request.r < me.seg.l or request.l > me.seg.r:  # segments not crossed
            return INF, 0
        if request.l <= me.seg.l and me.seg.r <= request.r:  # me in request range
            return me.min, me.count
        l_i, r_i = self._get_children_(i)
        l_ans = self._find_min_count_impl_(l_i, request)
        r_ans = self._find_min_count_impl_(r_i, request)
        cur_min = min(l_ans[0], r_ans[0])
        cur_count = 0
        for ans in (l_ans, r_ans):
            if ans[0] == cur_min:
                cur_count += ans[1]
        return cur_min, cur_count

    def find_min_count(self, seg: Segment):
        return self._find_min_count_impl_(0, seg)

    def _find_k_zero_on_prefix_(self, i: int, k: int):
        me = self.arr[i]
        if me.seg.l == me.seg.r:
            return i - self.displacement
        l_i, r_i = self._get_children_(i)
        if self.arr[l_i].min != 0:
            return self._find_k_zero_on_prefix_(r_i, k)
        if self.arr[l_i].count > k:
            return self._find_k_zero_on_prefix_(l_i, k)
        else:
            return self._find_k_zero_on_prefix_(r_i, k - self.arr[l_i].count)

    def find_k_zero_on_prefix(self, k: int):
        if self.arr[0].min != 0:
            return -1
        if self.arr[0].count < k + 1:
            return -1
        return self._find_k_zero_on_prefix_(0, k)

    def find_k_zero_on_range(self, k: int, seg: Segment):
        if self.arr[0].min != 0:
            return -1
        min_on_pref, count_on_pref = 0, 0
        if seg.l > 0:
            min_on_pref, count_on_pref = self.find_min_count(Segment(0, seg.l - 1))
        if min_on_pref != 0:
            count_on_pref = 0
        pos = self.find_k_zero_on_prefix(k + count_on_pref)
        if pos > seg.r:
            return -1
        return pos

    def update_item(self, i: int, val: int):
        i += self.displacement
        self.arr[i].min = val
        parent = self._get_parent_(i)
        while parent >= 0:
            l_i, r_i = self._get_children_(parent)
            self.arr[parent].min = min(self.arr[l_i].min, self.arr[r_i].min)
            self.arr[parent].count = 0
            for c_i in (l_i, r_i):
                if self.arr[c_i].min == self.arr[parent].min:
                    self.arr[parent].count += self.arr[c_i].count
            parent = self._get_parent_(parent)


def main():
    arr = read_input()
    ans = []
    tree = SegmentTree(arr)
    for _ in range(int(input().strip())):
        cmd = input().split()
        if cmd[0] == 'u':
            i, val = map(int, cmd[1:])
            i -= 1
            tree.update_item(i, val)
        elif cmd[0] == 's':
            l, r, k = map(lambda x: int(x) - 1, cmd[1:])
            seg = Segment(l, r)
            pos = tree.find_k_zero_on_range(k, seg)
            if pos != -1:
                pos += 1
            ans.append(pos)
    print(*ans)


if __name__ == '__main__':
    main()
