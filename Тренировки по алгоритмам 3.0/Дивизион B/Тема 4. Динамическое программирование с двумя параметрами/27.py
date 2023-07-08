def input_read():
    n, m = [int(x) for x in input().split()]
    table = [[int(x) for x in input().split()] for _ in range(n)]
    return n, m, table


def cost_path(n, m, table):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = table[0][0]
    answer = []
    for j in range(1, m):
        dp[0][j] += table[0][j] + dp[0][j - 1]
    for i in range(1, n):
        dp[i][0] += table[i][0] + dp[i - 1][0]
    for i in range(1, n):
        for j in range(1, m):
            down = dp[i - 1][j] + table[i][j]
            right = dp[i][j - 1] + table[i][j]
            if down > right:
                dp[i][j] = down
            else:
                dp[i][j] = right
    i, j = n - 1, m - 1
    while i > 0 or j > 0:
        if j > 0 and dp[i][j] == dp[i][j - 1] + table[i][j]:
            answer.append('R')
            j -= 1
            continue
        if i > 0 and dp[i][j] == dp[i - 1][j] + table[i][j]:
            answer.append('D')
            i -= 1
            continue
    return dp[n - 1][m - 1], answer[::-1]


def main():
    cost, path = cost_path(*input_read())
    print(cost)
    print(*path)


if __name__ == '__main__':
    main()
