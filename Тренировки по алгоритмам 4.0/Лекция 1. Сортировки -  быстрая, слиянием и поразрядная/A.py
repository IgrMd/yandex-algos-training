def read_input():
    n = int(input().strip())
    arr = [int(x) for x in input().split()]
    pivot = int(input().strip())
    return n, arr, pivot


def partition(arr, begin, end, pivot):
    equal_idx = begin
    while equal_idx < end and arr[equal_idx] < pivot:
        equal_idx += 1
    greater_idx = equal_idx
    while greater_idx < end and arr[greater_idx] == pivot:
        greater_idx += 1
    now = end - 1
    while now > greater_idx:
        if arr[now] < pivot:
            buf = arr[now]
            arr[now] = arr[greater_idx]
            if greater_idx != equal_idx:
                arr[greater_idx] = arr[equal_idx]
            arr[equal_idx] = buf
            equal_idx += 1
            greater_idx += 1
        elif arr[now] == pivot:
            arr[now], arr[greater_idx] = arr[greater_idx], arr[now]
            greater_idx += 1
        now -= 1
    return equal_idx


def less_than_pivot(n, arr, pivot):
    p = partition(arr, 0, n, pivot)
    return p, n - p


def main():
    print(*less_than_pivot(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
