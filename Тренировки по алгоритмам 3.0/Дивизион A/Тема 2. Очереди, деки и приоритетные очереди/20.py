import sys
from collections import deque


def read_input():
    n, k, p = [int(x) for x in input().split()]  # n - кол-во машинок, k - кол-во машинок на полу, p - кол-во запросов
    requests = list(map(int, sys.stdin.readlines()))
    car_to_requests = [deque() for _ in range(n + 1)]
    for i, x in enumerate(requests):
        car_to_requests[int(x)].append(i)
    for i in range(1, n + 1):
        car_to_requests[i].append(p)
    return n, k, p, requests, car_to_requests


def sift_up(pos, heap, heap_dict):
    while 0 < pos and heap[(pos - 1) // 2][1] < heap[pos][1]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        heap_dict[heap[(pos - 1) // 2][0]] = (pos - 1) // 2
        heap_dict[heap[pos][0]] = pos
        pos = (pos - 1) // 2


def heap_push(car: list, heap, heap_dict):
    heap.append(car)
    pos = len(heap) - 1
    heap_dict[car[0]] = pos
    sift_up(pos, heap, heap_dict)


def sift_down(pos, heap, heap_dict):
    size = len(heap)
    while pos < size:
        c1_i = pos * 2 + 1
        c2_i = pos * 2 + 2
        if size < c2_i:
            break
        if c2_i == size:
            if heap[pos][1] < heap[c1_i][1]:
                heap[pos], heap[c1_i] = heap[c1_i], heap[pos]
                heap_dict[heap[c1_i][0]] = c1_i
                heap_dict[heap[pos][0]] = pos
            break
        if heap[c2_i][1] < heap[c1_i][1] and heap[pos][1] < heap[c1_i][1]:
            heap[pos], heap[c1_i] = heap[c1_i], heap[pos]
            heap_dict[heap[c1_i][0]] = c1_i
            heap_dict[heap[pos][0]] = pos
            pos = c1_i
        elif heap[pos][1] < heap[c2_i][1]:
            heap[pos], heap[c2_i] = heap[c2_i], heap[pos]
            heap_dict[heap[c2_i][0]] = c2_i
            heap_dict[heap[pos][0]] = pos
            pos = c2_i
        else:
            break


def heap_pop(heap: list, heap_dict: dict):
    if not len(heap):
        return
    if len(heap) == 1:
        return heap.pop()
    item = heap[0]
    heap[0] = heap.pop()
    pos = 0
    heap_dict.pop(item[0])
    sift_down(pos, heap, heap_dict)
    return item


def operations(n, k, p, requests, car_to_requests: list[deque()]):
    opers = 0
    cars_on_floor = []
    carnum_to_heap_index = dict()
    for i, car in enumerate(requests):
        car_to_requests[car].popleft()
        next_car_request = car_to_requests[car][0]
        if car in carnum_to_heap_index:
            index_in_heap = carnum_to_heap_index[car]
            cars_on_floor[index_in_heap][1] = next_car_request
            sift_up(index_in_heap, cars_on_floor, carnum_to_heap_index)
        elif len(cars_on_floor) < k:
            heap_push([car, next_car_request], cars_on_floor, carnum_to_heap_index)
            opers += 1
        else:
            car_popped = heap_pop(cars_on_floor, carnum_to_heap_index)
            heap_push([car, next_car_request], cars_on_floor, carnum_to_heap_index)
            opers += 1
    return opers


def main():
    print(operations(*read_input()))


if __name__ == '__main__':
    main()
