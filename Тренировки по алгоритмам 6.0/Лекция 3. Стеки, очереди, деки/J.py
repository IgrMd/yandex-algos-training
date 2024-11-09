def input_read():
    n, H = map(int, input().split())
    heights = list(map(int, input().split()))
    wides = list(map(int, input().split()))
    return n, H, heights, wides


class Queue:
    def __init__(self, cap: int):
        self.capacity = cap
        self.size = self.l = self.r = 0
        self.buf = [0] * cap

    def front(self):
        if not self.size:
            raise RuntimeError("Empty")
        return self.buf[self.l]

    def back(self):
        if not self.size:
            raise RuntimeError("Empty")
        return self.buf[self.r - 1]

    def push_back(self, item):
        if self.capacity == self.size:
            raise RuntimeError("Full")
        self.buf[self.r] = item
        self.r = (self.r + 1) % self.capacity
        self.size += 1

    def push_front(self, item):
        if self.capacity == self.size:
            raise RuntimeError("Full")
        self.l = self.l - 1 if self.l else self.capacity - 1
        self.buf[self.l] = item
        self.size += 1

    def pop_back(self):
        if not self.size:
            raise RuntimeError("Empty")
        self.r = self.r - 1 if self.r else self.capacity - 1
        self.size -= 1
        return self.buf[self.r]

    def pop_front(self):
        if not self.size:
            raise RuntimeError("Empty")
        self.l = (self.l + 1) % self.capacity
        self.size -= 1
        return self.buf[self.l - 1]

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        buf = []
        l = self.l
        for _ in range(self.size):
            buf.append(self.buf[l])
            l += 1
            l %= self.capacity
        return str(buf)


def chairs(n, H, heights: list[int], wides: list[int]):
    chair_arr = []
    for i in range(n):
        chair_arr.append((heights[i], wides[i]))
    chair_arr.sort()
    diff_queue = Queue(n)
    r = 0
    sum_w = 0
    ans = 10 ** 9
    for l in range(n):
        if r == n:
            break
        while r < n and sum_w < H:
            sum_w += chair_arr[r][1]
            r_diff = chair_arr[r][0] - chair_arr[r - 1][0] if r != l else 0
            while diff_queue and diff_queue.back() < r_diff:
                diff_queue.pop_back()
            diff_queue.push_back(r_diff)
            r += 1
        if sum_w >= H and diff_queue:
            ans = min(ans, diff_queue.front())
        if l + 1 < n:
            l_diff = chair_arr[l + 1][0] - chair_arr[l][0]
            if diff_queue and l_diff == diff_queue.front():
                diff_queue.pop_front()
        sum_w -= chair_arr[l][1]
    return ans


def test():
    pass


def main():
    # test()
    print(chairs(*input_read()))


if __name__ == '__main__':
    main()
