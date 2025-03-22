def read_input():
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    return n, m, field


def turtle(n: int, m: int, field: list[list[int]]):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + field[i][j]
    path = []

    def find_path(i, j):
        if i == 0 and j == 0:
            return
        if i > 0 and dp[i][j] - dp[i - 1][j] == field[i][j]:
            path.append('D')
            return find_path(i - 1, j)
        if j > 0 and dp[i][j] - dp[i][j - 1] == field[i][j]:
            path.append('R')
            return find_path(i, j - 1)

    find_path(n - 1, m - 1)
    path.reverse()
    return dp[-1][-1], path


def main():
    dist, path = turtle(*read_input())
    print(dist)
    print(*path)


if __name__ == '__main__':
    main()
