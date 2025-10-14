import sys

sys.setrecursionlimit(10 ** 6)


def read_input():
    n = int(input().strip())
    arr = [list() for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    return n, arr


INF = float('inf')
ans = INF


def from_dead_end_to_dead_end(n: int, arr: list[list[int]]):
    if n == 1:
        return 0
    if n == 2:
        return 1

    def helper(parent, cur):
        if parent in arr[cur]:
            arr[cur].remove(parent)

        if len(arr[cur]) == 0:
            return 0
        if len(arr[cur]) == 1:
            return helper(cur, arr[cur][0]) + 1
        min1, min2 = INF, INF
        for adj in arr[cur]:
            adj_min = helper(cur, adj) + 1
            if adj_min < min1:
                min2 = min1
                min1 = adj_min
            elif adj_min < min2:
                min2 = adj_min
        global ans
        ans = min(ans, min1 + min2)
        return min1

    start = 0
    while len(arr[start]) < 2:
        start += 1
    helper(-1, start)
    global ans

    return ans


def main():
    print(from_dead_end_to_dead_end(*read_input()))


if __name__ == '__main__':
    main()
