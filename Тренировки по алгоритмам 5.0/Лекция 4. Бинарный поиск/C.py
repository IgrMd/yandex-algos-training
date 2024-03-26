def read_input():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    requests = [list(map(int, input().split())) for _ in range(m)]
    return n, arr, m, requests


def check_reg(i, l, s, pref_sums):
    p_sum = pref_sums[i + l] - pref_sums[i]
    return p_sum >= s


def upper_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    return l


def regiment_count(n, arr, m, requests):
    ans = []
    pref_sums = [0] * (n + 1)
    for i in range(n):
        pref_sums[i + 1] = pref_sums[i] + arr[i]
    for l, s in requests:
        index = upper_bound(0, n - l, check_reg, (l, s, pref_sums))
        p_sum = pref_sums[index + l] - pref_sums[index]
        ans.append(index + 1 if p_sum == s else - 1)
    return ans


if __name__ == '__main__':
    print(*regiment_count(*read_input()), sep='\n')
