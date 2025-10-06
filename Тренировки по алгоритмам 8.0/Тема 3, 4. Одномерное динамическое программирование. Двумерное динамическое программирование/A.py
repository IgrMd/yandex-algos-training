def read_input():
    n = int(input())
    return n


def ball_on_ladder(n):
    dp = [0] * (max(4, n + 1))
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n + 1):
        for j in range(-3, 0):
            dp[i] += dp[i + j]
    return dp[n]


def main():
    print(ball_on_ladder(read_input()))


if __name__ == '__main__':
    main()
