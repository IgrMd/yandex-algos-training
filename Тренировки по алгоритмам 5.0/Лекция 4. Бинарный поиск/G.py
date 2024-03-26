def read_input():
    n, m = map(int, input().split())
    field = [list(input().strip()) for _ in range(n)]
    return n, m, field


def sub_sum(p1, p2, pref_sums):
    i1, j1 = p1
    i2, j2 = p2
    # sum1 = pref_sums[i2][j2]
    # sum2 = pref_sums[i2][j1 - 1]
    # sum3 = pref_sums[i1 - 1][j2]
    # sum4 = pref_sums[i1 - 1][j1 - 1]
    # s_sum = sum1 - sum2 - sum3 + sum4
    # return s_sum
    return pref_sums[i2][j2] - pref_sums[i2][j1 - 1] - pref_sums[i1 - 1][j2] + pref_sums[i1 - 1][j1 - 1]


def check_plus(k, n, m, pref_sums):
    if 3 * k > n or 3 * k > m:
        return False
    for i in range(n - 3 * k + 1):
        for j in range(m - 3 * k + 1):
            sum1 = sub_sum((i, j + k), (i + 3 * k - 1, j + 2 * k - 1), pref_sums)
            sum2 = sub_sum((i + k, j), (i + 2 * k - 1, j + 3 * k - 1), pref_sums)
            if sum1 == sum2 == 3 * k * k:
                return True
    return False


def upper_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    if not cmp(l, *params):
        l += 1
    return l


def lower_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r + 1) // 2
        if cmp(mid, *params):
            l = mid
        else:
            r = mid - 1
    return l


def plus(n, m, field):
    pref_sums = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            pref_sums[i][j] = pref_sums[i - 1][j] + pref_sums[i][j - 1] - pref_sums[i - 1][j - 1]
            pref_sums[i][j] += field[i][j] == '#'
    ans = lower_bound(1, min(n, m), check_plus, (n, m, pref_sums))
    return ans


if __name__ == '__main__':
    print(plus(*read_input()))
