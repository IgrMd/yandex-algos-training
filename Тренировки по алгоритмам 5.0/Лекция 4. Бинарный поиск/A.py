from bisect import bisect_left, bisect_right


def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    k = int(input())
    requests = [list(map(int, input().split())) for _ in range(k)]

    return n, arr, k, requests


def execute(n, arr, k, requests):
    result = []
    for L, R in requests:
        ans = bisect_right(arr, R) - bisect_left(arr, L)
        result.append(ans)
    return result


if __name__ == '__main__':
    print(*execute(*read_input()))
