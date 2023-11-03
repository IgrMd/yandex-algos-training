def read_input():
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    m = int(input())
    arr2 = [int(x) for x in input().split()] if m > 0 else []
    return n, arr1, m, arr2


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


def main():
    n, arr1, m, arr2 = read_input()
    buf = [0] * (n + m)
    merge(arr1, 0, n, arr2, 0, m, buf, 0)
    print(*buf)


if __name__ == '__main__':
    main()
