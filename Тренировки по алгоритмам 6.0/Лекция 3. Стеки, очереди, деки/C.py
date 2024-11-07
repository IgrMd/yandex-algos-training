def input_read():
    n, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    return n, k, nums


class Queue:
    def __init__(self, cap: int):
        self.capacity = cap
        self.size = self.l = self.r = 0
        self.buf = [0] * cap

    def front(self) -> int:
        if not self.size:
            raise RuntimeError("Empty")
        return self.buf[self.l]

    def back(self) -> int:
        if not self.size:
            raise RuntimeError("Empty")
        return self.buf[self.r - 1]

    def push(self, item: int):
        if self.capacity == self.size:
            raise RuntimeError("Full")
        self.buf[self.r] = item
        self.r = (self.r + 1) % self.capacity
        self.size += 1

    def pop_back(self) -> int:
        if not self.size:
            raise RuntimeError("Empty")
        self.r = self.r - 1 if self.r else self.capacity - 1
        self.size -= 1
        return self.buf[(self.r + 1) % self.capacity]

    def pop_front(self) -> int:
        if not self.size:
            raise RuntimeError("Empty")
        self.l = (self.l + 1) % self.capacity
        self.size -= 1
        return self.buf[self.l - 1]

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        return str(self.buf)


def window_min(n, k, nums):
    ans = []
    queue = Queue(k)
    r = 0
    for l in range(n):
        while r < n and r - l < k:
            while queue and queue.back() > nums[r]:
                queue.pop_back()
            queue.push(nums[r])
            r += 1
        if r - l == k:
            ans.append(queue.front())
        if queue and queue.front() == nums[l]:
            queue.pop_front()
    return ans


def main():
    print(*window_min(*input_read()), sep='\n')


if __name__ == '__main__':
    main()
