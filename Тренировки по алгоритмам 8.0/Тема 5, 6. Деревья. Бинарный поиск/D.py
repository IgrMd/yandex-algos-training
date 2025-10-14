import bisect


def read_input():
    n, p = map(int, input().split())
    signs = list(map(int, input().split()))
    return n, p, signs


INF = float('inf')


def currency_exchange(n: int, p: int, signs: list[int]):
    sorted = []
    for j, s in enumerate(signs):
        sorted.append((s, j + 1))
    sorted.sort()
    best_delta = INF
    i_mem, j_mem = 1, 0
    for j in range(n):
        i = bisect.bisect_right(sorted, sorted[j][0] * p, key=lambda x: x[0])
        buf = [i, i - 1]
        if i == n:
            buf.remove(i)
        if i - 1 == j:
            buf.remove(j)
        for i in buf:
            if abs(sorted[i][0] / sorted[j][0] - p) < best_delta:
                best_delta = abs(sorted[i][0] / sorted[j][0] - p)
                i_mem, j_mem = i, j
    return sorted[i_mem][1], sorted[j_mem][1]


def main():
    print(*currency_exchange(*read_input()))


if __name__ == '__main__':
    main()
