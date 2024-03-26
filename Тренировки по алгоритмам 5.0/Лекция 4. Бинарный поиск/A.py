def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    k = int(input())
    requests = [list(map(int, input().split())) for _ in range(k)]

    return n, arr, k, requests


def cmp_gt(i, target, arr):
    return arr[i] > target


def cmp_le(i, target, arr):
    return arr[i] >= target


def upper_bound(l, r, cmp, params):
    r -= 1
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    if not cmp(l, *params):
        return l + 1
    return l


def lower_bound(l, r, cmp, params):
    r -= 1
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    if not cmp(l, *params):
        return l + 1
    return l


def execute(n, arr, k, requests):
    for L, R in requests:
        ans = upper_bound(0, n, cmp_gt, (R, arr)) - upper_bound(0, n, cmp_le, (L, arr))
        print(ans, end=' ')


if __name__ == '__main__':
    execute(*read_input())
