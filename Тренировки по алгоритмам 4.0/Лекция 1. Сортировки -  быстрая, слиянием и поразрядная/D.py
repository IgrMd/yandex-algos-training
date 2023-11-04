def read_input():
    n = int(input())
    arr = [int(x) for x in input().split()] if n > 0 else []
    return n, arr


def merge(arr1, i, n, arr2, j, m, arr, k):
    while i < n and j < m:
        if arr2[j] < arr1[i]:
            arr[k] = arr2[j]
            j += 1
        else:
            arr[k] = arr1[i]
            i += 1
        k += 1
    while i < n:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < m:
        arr[k] = arr2[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr, begin, end):
    if end - begin <= 0:
        return []
    if end - begin == 1:
        return [arr[begin]]
    mid = (begin + end) // 2
    arr1 = merge_sort(arr, begin, mid)
    arr2 = merge_sort(arr, mid, end)
    buf = [0] * (end - begin)
    merge(arr1, 0, len(arr1), arr2, 0, len(arr2), buf, 0)
    return buf


def sort(n, arr):
    return merge_sort(arr, 0, len(arr))


def main():
    print(*sort(*read_input()))


if __name__ == '__main__':
    main()
