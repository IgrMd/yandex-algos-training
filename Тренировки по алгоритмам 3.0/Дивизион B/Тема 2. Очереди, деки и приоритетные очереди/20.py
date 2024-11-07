def heap_push(n, heap):
    heap.append(n)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] < heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2


def sift_down(pos, heap):
    size = len(heap)
    while pos < size:
        c1_i = pos * 2 + 1
        c2_i = pos * 2 + 2
        if c1_i >= size:
            break
        if c2_i == size:
            if heap[pos] > heap[c1_i]:
                heap[pos], heap[c1_i] = heap[c1_i], heap[pos]
            break
        if heap[c1_i] < heap[c2_i] and heap[c1_i] < heap[pos]:
            heap[pos], heap[c1_i] = heap[c1_i], heap[pos]
            pos = c1_i
        elif heap[c2_i] < heap[pos]:
            heap[pos], heap[c2_i] = heap[c2_i], heap[pos]
            pos = c2_i
        else:
            break


def heap_pop(heap):
    if not len(heap):
        return
    if len(heap) == 1:
        return heap.pop_front()
    item = heap[0]
    heap[0] = heap.pop_front()
    pos = 0
    sift_down(pos, heap)
    return item


def heap_sort(lst):
    heap = []
    for i in lst:
        heap_push(i, heap)
    ans = [heap_pop(heap) for i in range(len(lst))]
    return ans


def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(*heap_sort(lst))


if __name__ == '__main__':
    main()
