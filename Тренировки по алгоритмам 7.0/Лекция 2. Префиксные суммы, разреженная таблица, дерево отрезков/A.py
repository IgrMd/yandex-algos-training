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
    count: int
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
                self.arr[i] = Item(-INF, 0, Segment(initial_i, initial_i))
            elif initial_i >= 0:
                self.arr[i] = Item(arr[initial_i], 1, Segment(initial_i, initial_i))
            else:
                l_child_i, r_child_i = self._get_children_(i)
                l_child, r_child = self.arr[l_child_i], self.arr[r_child_i]
                cur_max = max(l_child.max, r_child.max)
                seg = Segment(l_child.seg.l, r_child.seg.r)
                cur_count = 0
                for child in (l_child, r_child):
                    if child.max == cur_max:
                        cur_count += child.count
                self.arr[i] = Item(cur_max, cur_count, seg)

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    def _handle_request_impl_(self, i: int, request: Segment):
        if i >= self.n:
            return -INF, 0
        me = self.arr[i]
        if request.r < me.seg.l or request.l > me.seg.r:
            return -INF, 0
        if request.l <= me.seg.l and me.seg.r <= request.r:
            return me.max, me.count
        l_child_i, r_child_i = self._get_children_(i)
        l_ans = self._handle_request_impl_(l_child_i, request)
        r_ans = self._handle_request_impl_(r_child_i, request)
        cur_max = max(l_ans[0], r_ans[0])
        cur_count = 0
        for ans in (l_ans, r_ans):
            if ans[0] == cur_max:
                cur_count += ans[1]
        return cur_max, cur_count

    def handle_request(self, seg: Segment):
        return self._handle_request_impl_(0, seg)


def main():
    tree = read_input()
    for _ in range(int(input().strip())):
        request = Segment(*map(int, input().split()))
        request.l -= 1
        request.r -= 1
        print(*tree.handle_request(request))


if __name__ == '__main__':
    main()
