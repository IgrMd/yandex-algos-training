def read_input():
    n = int(input())
    return n


def s(n):
    if n < 3:
        return 0
    if n == 3:
        return 1
    dp = [0, 0, 1]
    for i in range(3, n):
        dp_i = 2 ** (i - 2) + dp[i - 3] + dp[i - 2] + dp[i - 1]
        dp.append(dp_i)
    return dp[-1]


def three_ones_in_row(n):
    return 2 ** n - s(n)


def main():
    print(three_ones_in_row(read_input()))


if __name__ == '__main__':
    main()
