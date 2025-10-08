def read_input():
    n = int(input().strip())
    return n


def ladders(n: int):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        j = n
        while j >= i:
            dp[j] += dp[j - i]
            j -= 1
    return dp[n]


def main():
    print(ladders(read_input()))


if __name__ == '__main__':
    main()
