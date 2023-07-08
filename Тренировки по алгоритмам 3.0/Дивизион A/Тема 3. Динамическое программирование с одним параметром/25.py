def read_input():
    n, a, b = [int(x) for x in input().split()]
    return n, a, b


def sweets(n, a, b):
    N = n + 1
    dp = [0] * N
    if n < 2:
        return dp[n]
    dp[2] = max(a, b)
    for i in range(3, N):
        min_k = N * max(a, b)
        for k in range(1, i):
            buf = max(dp[k] + a, dp[i - k] + b)
            if buf < min_k:
                min_k = buf
        dp[i] = min_k
    return dp[n]


def test():
    assert sweets(8, 1, 1) == 3
    assert sweets(10, 5, 0) == 5
    assert sweets(7, 0, 2) == 2
    assert sweets(10, 1, 2) == 6
    assert sweets(11, 1, 1) == 4
    assert sweets(3, 1, 2) == 3
    assert sweets(3, 2, 1) == 3
    assert sweets(1, 0, 0) == 0
    assert sweets(1, 0, 10000) == 0
    assert sweets(129, 10, 10) == 80
    assert sweets(930, 1, 10) == 43
    assert sweets(966, 3, 10) == 63
    # print('Tests OK')


def main():
    test()
    print(sweets(*read_input()))


if __name__ == '__main__':
    main()
