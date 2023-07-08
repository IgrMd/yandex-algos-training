def input_read():
    n, m = [int(x) for x in input().split()]
    table = [[int(x) for x in input().split()] for _ in range(n)]
    return n, m, table


def weight(n, m, table):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = table[0][0]
    for j in range(1, m):
        dp[0][j] += table[0][j] + dp[0][j - 1]
    for i in range(1, n):
        dp[i][0] += table[i][0] + dp[i - 1][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j] + table[i][j], dp[i][j - 1] + table[i][j])
    return dp[n - 1][m - 1]


def main():
    print(weight(*input_read()))


if __name__ == '__main__':
    main()
