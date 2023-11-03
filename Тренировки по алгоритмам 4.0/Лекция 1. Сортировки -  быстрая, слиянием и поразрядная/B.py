from random import randint


def read_input():
    n = int(input())
    if n == 0:
        return 0, []
    arr = [int(x) for x in input().split()]
    return n, arr


def partition(arr: list, begin: int, end: int):
    pivot = arr[randint(begin, end)]
    equal_idx = begin
    while equal_idx <= end and arr[equal_idx] < pivot:
        equal_idx += 1
    greater_idx = equal_idx
    while greater_idx <= end and arr[greater_idx] == pivot:
        greater_idx += 1
    now = greater_idx
    while now <= end:
        if arr[now] < pivot:
            buf = arr[now]
            arr[now] = arr[greater_idx]
            arr[greater_idx] = arr[equal_idx]
            arr[equal_idx] = buf
            equal_idx += 1
            greater_idx += 1
        elif arr[now] == pivot:
            arr[now], arr[greater_idx] = arr[greater_idx], arr[now]
            greater_idx += 1
        now += 1
    return equal_idx - 1, greater_idx


def partition_sort(arr, begin, end):
    if end - begin < 1:
        return
    p1, p2 = partition(arr, begin, end)
    partition_sort(arr, begin, p1)
    partition_sort(arr, p2, end)


def sort(n, arr):
    partition_sort(arr, 0, len(arr) - 1)
    return arr


def main():
    print(*sort(*read_input()))


if __name__ == '__main__':
    main()
