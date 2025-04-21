from dataclasses import dataclass


def read_input():
    n = int(input().strip())
    table = SegmentTree(list(map(int, input().split())))
    return table


@dataclass
class Segment:
    l: int
    r: int


@dataclass
class Item:
    max: int | float
    # count: int
    seg: Segment


INF = float('inf')


class SegmentTree:
    def __init__(self, arr: list[int]):
        self._init_buffer_(arr)
        pass

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
                self.arr[i] = Item(-INF, Segment(initial_i, initial_i))
            elif initial_i >= 0:
                self.arr[i] = Item(arr[initial_i], Segment(initial_i, initial_i))
            else:
                l_child_i, r_child_i = self._get_children_(i)
                l_child, r_child = self.arr[l_child_i], self.arr[r_child_i]
                cur_max = max(l_child.max, r_child.max)
                seg = Segment(l_child.seg.l, r_child.seg.r)
                self.arr[i] = Item(cur_max, seg)

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    @staticmethod
    def _get_parent_(i: int):
        return (i - 1) // 2 if i != 0 else -1

    def _handle_request_impl_(self, i: int, request: Segment):
        if i >= self.n:
            return -INF
        me = self.arr[i]
        if request.r < me.seg.l or request.l > me.seg.r:
            return -INF
        if request.l <= me.seg.l and me.seg.r <= request.r:
            return me.max
        l_child_i, r_child_i = self._get_children_(i)
        l_ans = self._handle_request_impl_(l_child_i, request)
        r_ans = self._handle_request_impl_(r_child_i, request)
        return max(l_ans, r_ans)

    def handle_request(self, seg: Segment):
        return self._handle_request_impl_(0, seg)

    def update_item(self, i: int, val: int):
        i += self.displacement
        self.arr[i].max = val
        parent = self._get_parent_(i)
        while parent >= 0:
            l_child_i, r_child_i = self._get_children_(parent)
            self.arr[parent].max = max(self.arr[l_child_i].max, self.arr[r_child_i].max)
            parent = self._get_parent_(parent)


def main():
    tree = read_input()
    ans = []
    for _ in range(int(input().strip())):
        cmd, a, b = input().split()
        if cmd == 'u':
            tree.update_item(int(a) - 1, int(b))
        elif cmd == 's':
            ans.append(tree.handle_request(Segment(int(a) - 1, int(b) - 1)))
    print(*ans)


if __name__ == '__main__':
    main()
