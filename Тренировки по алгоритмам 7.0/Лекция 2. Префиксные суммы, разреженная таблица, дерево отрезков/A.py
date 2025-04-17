from dataclasses import dataclass


def read_input():
    n = int(input().strip())
    table = SegmentTree(list(map(int, input().split())))
    return table


@dataclass
class Range:
    l: int
    r: int


@dataclass
class Item:
    max: int | float
    max_count: int
    rng: Range


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
        self.initial_i = pow_of_2 - 1
        self.arr: list[Item | None] = [None] * self.n
        for i in range(len(arr)):
            self_index: int = i + self.initial_i
            self.arr[self_index] = Item(arr[i], 1, Range(i, i))
        for i in range(self.initial_i + len(arr), self.n):
            self.arr[i] = Item(-INF, 1, Range(i - self.initial_i, i - self.initial_i))
        for i in range(self.initial_i - 1, -1, -1):
            l_child_i, r_child_i = self._get_children_(i)
            l_child, r_child = self.arr[l_child_i], self.arr[r_child_i]
            cur_max = max(l_child.max, r_child.max)
            rng = Range(l_child.rng.l, r_child.rng.r)
            max_count = 0
            for child in (l_child_i, r_child_i):
                if cur_max == self.arr[child].max:
                    max_count += self.arr[child].max_count
            self.arr[i] = Item(cur_max, max_count, rng)

    @staticmethod
    def _get_children_(i: int):
        return 2 * i + 1, 2 * i + 2

    def _handle_request_impl_(self, i: int, request: Range):
        if i >= self.n:
            return -INF, 0
        me = self.arr[i]
        if request.r < me.rng.l or request.l > me.rng.r:
            return -INF, 0
        if request.l <= me.rng.l and me.rng.r <= request.r:
            return me.max, me.max_count
        child_l, child_r = self._get_children_(i)
        max_l, max_count_l = self._handle_request_impl_(child_l, request)
        max_r, max_count_r = self._handle_request_impl_(child_r, request)
        max_ans = max(max_l, max_r)
        count_ans = 0
        if max_ans == max_l:
            count_ans += max_count_l
        if max_ans == max_r:
            count_ans += max_count_r
        return max_ans, count_ans

    def handle_request(self, rng: Range):
        return self._handle_request_impl_(0, rng)


def main():
    table = read_input()
    for _ in range(int(input().strip())):
        request = Range(*map(int, input().split()))
        request.l -= 1
        request.r -= 1
        print(*table.handle_request(request))


if __name__ == '__main__':
    main()
