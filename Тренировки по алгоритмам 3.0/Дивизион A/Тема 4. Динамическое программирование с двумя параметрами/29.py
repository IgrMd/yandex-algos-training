def read_input():
    m, n = [int(x) for x in input().split()]
    return m, n


def signs(m, n):
    dp = [[1] * (n + 1) for _ in range(m + 1)]
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + dp[i - 1][j - 1]
    return dp[m][n]


def main():
    print(signs(*read_input()))


if __name__ == '__main__':
    main()
