import operator


class Heap:
    def __init__(self, cmp=None):
        if cmp:
            self.cmp = cmp
        else:
            self.cmp = operator.lt
        self.heap = []

    def add(self, k):
        self.heap.append(k)
        self._seed_up_(len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._seed_down_(0)
        return item

    def top(self):
        return self.heap[0]

    def _seed_down_(self, i):
        ci_l = i * 2 + 1
        ci_r = i * 2 + 2
        if ci_l >= len(self.heap) and ci_r >= len(self.heap):
            return
        min_ci = ci_r if ci_r < len(self.heap) and self.cmp(self.heap[ci_r], self.heap[ci_l]) else ci_l
        if self.cmp(self.heap[min_ci], self.heap[i]):
            self.heap[min_ci], self.heap[i] = self.heap[i], self.heap[min_ci]
            self._seed_down_(min_ci)

    def _seed_up_(self, i):
        parent = (i - 1) // 2
        if parent < 0:
            return
        if self.cmp(self.heap[i], self.heap[parent]):
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._seed_up_(parent)


def handle_heap():
    n = int(input().strip())
    heap = Heap(operator.gt)
    for _ in range(n):
        request = input().split()
        if request[0] == '0':
            heap.add(int(request[1]))
        else:
            print(heap.pop())


def main():
    handle_heap()


if __name__ == '__main__':
    main()
