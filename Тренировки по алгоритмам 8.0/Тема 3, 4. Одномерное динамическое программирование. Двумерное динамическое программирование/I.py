import sys

sys.setrecursionlimit(1000001)


def read_input():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    return n, m, table


def chain_in_table(n, m, table: list[list]):
    dp = [[-1] * m for _ in range(n)]
    diffs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def helper(i2, j2):
        dp[i2][j2] = 1
        for di2, dj2 in diffs:
            adj_i2 = i2 + di2
            adj_j2 = j2 + dj2
            if adj_i2 == n or adj_i2 < 0 or adj_j2 == m or adj_j2 < 0:
                continue
            curr2 = table[i2][j2]
            adj2 = table[adj_i2][adj_j2]
            if curr2 - adj2 == 1:
                if dp[adj_i2][adj_j2] == -1:
                    dp[i2][j2] = max(dp[i2][j2], helper(adj_i2, adj_j2) + 1)
                else:
                    dp[i2][j2] = max(dp[i2][j2], dp[adj_i2][adj_j2] + 1)
        return dp[i2][j2]

    for i in range(n):
        for j in range(m):
            curr = table[i][j]
            if dp[i][j] != -1:
                continue
            dp[i][j] = 1
            for di, dj in diffs:
                adj_i = i + di
                adj_j = j + dj
                if adj_i == n or adj_i < 0 or adj_j == m or adj_j < 0:
                    continue
                adj = table[adj_i][adj_j]
                if curr - adj == 1:
                    if dp[adj_i][adj_j] == -1:
                        dp[i][j] = max(dp[i][j], helper(adj_i, adj_j) + 1)
                    else:
                        dp[i][j] = max(dp[i][j], dp[adj_i][adj_j] + 1)

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, dp[i][j])
    return ans


def main():
    print(chain_in_table(*read_input()))


if __name__ == '__main__':
    main()
