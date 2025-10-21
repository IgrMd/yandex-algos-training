from bisect import bisect_left

SUM_SA = 0
SUM_A = 1


def planning_series(n: int, s: list[int], a: list[int]):
    sa_sorted = []
    for i in range(n):
        sa_sorted.append((s[i], a[i]))
    sa_sorted.sort()
    prefs = [(0, 0)]
    for si, ai in sa_sorted:
        prev = prefs[-1]
        prefs.append((si * ai + prev[SUM_SA], ai + prev[SUM_A]))
    ans_e, ans_cost = float('inf'), float('inf')

    for e in range(1, max(s) + 1):
        j = bisect_left(a=sa_sorted, x=e, lo=0, hi=n, key=lambda x: x[0])
        curr = 2 * e * prefs[j][SUM_A] - 2 * prefs[j][SUM_SA] + prefs[-1][SUM_SA] - e * prefs[-1][SUM_A]
        if curr < ans_cost:
            ans_cost = curr
            ans_e = e
    return ans_e, ans_cost


def main():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')
    n = int(input().strip())
    s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(*planning_series(n, s, a))


if __name__ == '__main__':
    main()
