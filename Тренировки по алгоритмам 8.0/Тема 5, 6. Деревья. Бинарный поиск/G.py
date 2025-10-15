import random
from bisect import bisect_right, bisect_left


def read_input():
    n = int(input().strip())
    a = list(map(int, input().split()))
    m = int(input().strip())
    b = list(map(int, input().split()))
    return n, a, m, b


BJJ = 0
BJ = 1
J = 2


def superstring_gravity(n: int, a: list[int], m: int, b: list[int]):
    b_sorted = [(b[j], j + 1) for j in range(m)]
    b_sorted.sort()
    prefs = [(0, 0, 0)]
    for bj, j in b_sorted:
        prev = prefs[-1]
        prefs.append((prev[BJJ] + bj * j, prev[BJ] + bj, prev[J] + j))
    ans = 0
    bjj_l, bj_l, j_l = prefs[-1]
    for i, ai in enumerate(a, 1):
        j = bisect_left(a=b_sorted, x=ai, lo=0, hi=len(b_sorted), key=lambda x: x[0])
        count_lt = j
        count_ge = m - j
        sum1 = count_lt * ai * i - i * prefs[j][BJ] - ai * prefs[j][J] + prefs[j][BJJ]
        sum2 = -count_ge * ai * i + i * (bj_l - prefs[j][BJ]) + ai * (j_l - prefs[j][J]) - (bjj_l - prefs[j][BJJ])
        ans += sum1 + sum2
    return ans


def superstring_gravity_naive(n: int, a: list[int], m: int, b: list[int]):
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += (i - j) * abs(a[i] - b[j])
    return ans


def test():
    n_max = 100
    while True:
        n = random.randint(1, n_max)
        m = random.randint(1, n_max)
        a = [random.randint(1, n_max) for _ in range(n)]
        b = [random.randint(1, n_max) for _ in range(m)]
        ans1 = superstring_gravity(n, a, m, b)
        ans2 = superstring_gravity(n, a, m, b)
        if ans1 != ans2:
            print(f'{ans1} != {ans2}')
            print(n)
            print(*a)
            print(m)
            print(*b)


def main():
    print(superstring_gravity(*read_input()))


if __name__ == '__main__':
    # test()
    main()
