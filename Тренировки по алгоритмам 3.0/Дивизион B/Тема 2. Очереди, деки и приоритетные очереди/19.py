heap = []


def Insert(n):
    heap.append(n)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2


def Extract():
    # print(heappop(heap))
    if not len(heap):
        return
    if len(heap) == 1:
        return heap.pop()
    item = heap[0]
    heap[0] = heap.pop()
    pos = 0
    size = len(heap)
    while pos < size:
        c1_i = pos * 2 + 1
        c2_i = pos * 2 + 2
        if c1_i >= size:
            break
        if c2_i == size:
            if heap[pos] < heap[c1_i]:
                heap[pos], heap[c1_i] = heap[c1_i], heap[pos]
            break
        if heap[pos] >= heap[c1_i] and heap[pos] >= heap[c2_i]:
            break
        if heap[c1_i] < heap[c2_i]:
            heap[pos], heap[c2_i] = heap[c2_i], heap[pos]
            pos = c2_i
        else:
            heap[pos], heap[c1_i] = heap[c1_i], heap[pos]
            pos = c1_i
    return item


def main():
    n = int(input())
    for i in range(n):
        cmd = input().split()
        if cmd[0] == '0':
            Insert(int(cmd[1]))
        else:
            print(Extract())


if __name__ == '__main__':
    main()
