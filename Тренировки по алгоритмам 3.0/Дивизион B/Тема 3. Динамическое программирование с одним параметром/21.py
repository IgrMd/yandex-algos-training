def input_read():
    N = int(input())
    return N


def sequence_count(N):
    n = 8 if N <= 7 else N + 1
    dp = [0] * n
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7
    for i in range(4, n):
        if i <= 6:
            dp[i] = dp[i - 1] * 2 - 2 ** (i - 4)
        else:
            dp[i] = dp[i - 1] * 2 - dp[i - 4]
    return dp[N]


def main():
    print(sequence_count(input_read()))


if __name__ == '__main__':
    main()
