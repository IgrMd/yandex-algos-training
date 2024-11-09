from collections import defaultdict


def input_read():
    n = int(input().strip())
    a, b = map(int, input().split())
    rovers = [list(map(int, input().split())) for _ in range(n)]
    return n, a, b, rovers


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


OPPOSITE = {1: 3, 3: 1, 2: 4, 4: 2}
RIGHT = {1: 4, 2: 1, 3: 2, 4: 3}
LEFT = {1: 2, 2: 3, 3: 4, 4: 1}
MAX_TIME = 201


def rover_queue(n, a: int, b: int, rovers: list[list[int]]):
    def is_main(x: int) -> bool:
        return x == a or x == b

    def other_main(x: int) -> int:
        return a if x == b else b

    # rovers.sort(key=lambda x: (x[1], x[0]))
    events = defaultdict(list)
    for i in range(n):
        road_, time_ = rovers[i]
        events[time_].append((i, road_))
    ans = []
    queues = {
        1: Queue(n),
        2: Queue(n),
        3: Queue(n),
        4: Queue(n)
    }
    for t in range(MAX_TIME):
        if t in events:
            for i, r in events[t]:
                queues[r].push_back(i)
        rovers_to_pass = []
        for road in [1, 2, 3, 4]:
            if not queues[road]:
                continue
            if is_main(road):
                main2 = other_main(road)
                if main2 == OPPOSITE[road]:
                    rovers_to_pass.append(road)
                    continue
                if main2 == RIGHT[road] and queues[main2]:
                    continue
                rovers_to_pass.append(road)
            else:
                if queues[RIGHT[road]]:
                    continue
                if queues[LEFT[road]] and is_main(LEFT[road]):
                    continue
                if queues[OPPOSITE[road]] and is_main(OPPOSITE[road]):
                    continue
                rovers_to_pass.append(road)
        for rover in rovers_to_pass:
            ans.append((t, queues[rover].pop_front()))
    ans.sort(key=lambda x: x[1])
    return [x[0] for x in ans]


def test():
    assert rover_queue(4, 1, 3, [(1, 1), (2, 1), (3, 1), (4, 1)]) == [1, 2, 1, 2]
    assert rover_queue(1, 1, 3, [(1, 66)]) == [66]
    assert rover_queue(1, 1, 3, [(2, 66)]) == [66]
    assert rover_queue(1, 1, 3, [(3, 66)]) == [66]
    assert rover_queue(1, 1, 3, [(4, 66)]) == [66]
    assert rover_queue(4, 1, 2, [(1, 100), (2, 100), (3, 100), (4, 100)]) == [100, 101, 102, 103]
    assert rover_queue(7, 2, 3, [(4, 5), (1, 4), (4, 6), (2, 4), (3, 9), (3, 4), (2, 7)]) == [6, 10, 8, 4, 9, 5, 7]
    assert rover_queue(4, 1, 3, [(1, 1), (3, 1), (2, 1), (2, 2)]) == [1, 1, 2, 3]
    assert rover_queue(4, 1, 2, [(1, 1), (2, 1), (3, 1), (4, 1)]) == [1, 2, 3, 4]
    assert rover_queue(1, 1, 4, [(1, 1)]) == [1]
    assert rover_queue(2, 1, 4, [(1, 1), (3, 1)]) == [1, 2]
    assert rover_queue(10, 1, 4, [(3, 1), (4, 1), (2, 1), (1, 1), (2, 4), (1, 5), (4, 5), (2, 5), (1, 6), (2, 9)]) == [
        10, 1, 3, 2, 4, 6, 5, 8, 7, 9]
    print('tests pass')


def main():
    # test()
    print(*rover_queue(*input_read()), sep='\n')


if __name__ == '__main__':
    main()
