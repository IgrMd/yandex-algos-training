def read_input():
    n = int(input().strip())
    buy_time = [list(map(int, input().split())) for _ in range(n)]
    return n, buy_time


def tickets(n: int, buy_time: list[list[int]]):
    dp = [0] * n
    max_t = 10 ** 9
    for _ in range(2):
        buy_time.append([max_t, max_t, max_t])
        dp.append(max_t)
    buy_time.append([0, 0, 0])
    dp.append(0)
    a, b, c = 0, 1, 2
    for i in range(n):
        t_a = dp[i - 1] + buy_time[i][a]
        t_b = dp[i - 2] + buy_time[i - 1][b]
        t_c = dp[i - 3] + buy_time[i - 2][c]
        dp[i] = min(t_a, t_b, t_c)
    return dp[n - 1]


def main():
    print(tickets(*read_input()))


if __name__ == '__main__':
    main()
