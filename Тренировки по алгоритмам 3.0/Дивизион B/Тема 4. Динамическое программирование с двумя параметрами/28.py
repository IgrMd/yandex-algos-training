def input_read():
    n, m = [int(x) for x in input().split()]
    return n, m


def paths(n, m):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            way1 = dp[i - 2][j - 1] if i > 1 and j > 0 else 0
            way2 = dp[i - 1][j - 2] if i > 0 and j > 1 else 0
            dp[i][j] = way1 + way2
    return dp[n - 1][m - 1]


def main():
    print(paths(*input_read()))


if __name__ == '__main__':
    main()
