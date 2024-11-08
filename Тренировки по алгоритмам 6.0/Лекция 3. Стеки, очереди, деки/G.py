def input_read():
    n, b = map(int, input().split())
    clients = [int(x) for x in input().split()]
    return n, b, clients


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
        return self.buf[(self.r + 1) % self.capacity]

    def pop_front(self):
        if not self.size:
            raise RuntimeError("Empty")
        self.l = (self.l + 1) % self.capacity
        self.size -= 1
        return self.buf[self.l - 1]

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        return str(self.buf)


def order_checkout_place(n, b, clients):
    ans = 0
    queue = Queue(n)
    minute = 0
    while minute < n:
        queue.push_back((minute, clients[minute]))
        can_handle = b
        while queue and can_handle > 0:
            minute_in, count = queue.pop_front()
            clients_handled = min(can_handle, count)
            ans += (minute - minute_in + 1) * clients_handled
            can_handle -= clients_handled
            count -= clients_handled
            if count:
                queue.push_front((minute_in, count))
        minute += 1

    while queue:
        minute_in, count = queue.pop_front()
        ans += (minute - minute_in + 1) * count
    return ans


def main():
    print(order_checkout_place(*input_read()))


if __name__ == '__main__':
    main()
