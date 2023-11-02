def read_input():
    n, m = [int(x) for x in input().split()]
    field = []
    for _ in range(n):
        field.append([int(x) for x in input().split()])
    return n, m, field


def rabbit(n, m, field):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for y in range(n):
        for x in range(m):
            if field[y][x]:
                dp[y][x] = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) + 1
    max_carrots = 0
    for y in range(n):
        for x in range(m):
            max_carrots = max(dp[y][x], max_carrots)
    return max_carrots


def main():
    print(rabbit(*read_input()))


if __name__ == '__main__':
    main()
