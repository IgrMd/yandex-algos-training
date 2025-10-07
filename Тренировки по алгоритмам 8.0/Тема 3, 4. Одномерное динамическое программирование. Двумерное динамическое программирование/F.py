import sys

sys.setrecursionlimit(10 ** 4)


def read_input():
    n = int(input().strip())
    road = []
    for i in range(n):
        row = input().strip()
        road.append(row)
    return len(road), road


def gathering_coins(n: int, road: list[str]):
    if n == 0:
        return 0

    reachable = [[False] * 3 for _ in range(n)]
    for i in range(3):
        reachable[0][i] = road[0][i] != 'W'

    for i in range(n - 1):
        for j in range(3):
            if not reachable[i][j]:
                continue
            reachable[i + 1][j] = road[i + 1][j] != 'W'
            if j > 0:
                reachable[i + 1][j - 1] = road[i + 1][j - 1] != 'W'
            if j < 2:
                reachable[i + 1][j + 1] = road[i + 1][j + 1] != 'W'

    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        dp[0][i] = int(road[0][i] == 'C')

    for i in range(1, n):
        for j in range(3):
            if not reachable[i][j]:
                continue
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
            if j < 2:
                dp[i][j] = max(dp[i][j], dp[i - 1][j + 1])
            dp[i][j] += int(road[i][j] == 'C')
    return max(map(max, dp))


def main():
    print(gathering_coins(*read_input()))


if __name__ == '__main__':
    main()
